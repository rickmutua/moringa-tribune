from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

import datetime as dt

from .models import Articles, NewsLetterRecipients
from .forms import NewsLetterForm, NewArticleForm
from .emails import send_welcome_email


from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import MerchSerializer

from rest_framework import status


# Create your views here.

def welcome(request):

    return render(request, 'welcome.html')

#
# def news_of_day(request):
#
#     date = dt.date.today()
#
#     return HttpResponse()


def news_today(request):

    date = dt.date.today()

    news = Articles.todays_news()

    form = NewsLetterForm()

    return render(request, 'all-news/todays-news.html', {"date": date, "news": news, "letterForm": form})



# def convert_dates(dates):
#
#     # function that gets the number for the date of the weekday
#     day_number = dt.date.weekday(dates)
#
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
#     # function that returns the actual day of the week
#     day = days[day_number]
#
#     return day


def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Articles.days_news(date)
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})


def search_results(request):

    if 'articles' in request.GET and request.GET["articles"]:
        search_term = request.GET.get("articles")
        searched_articles = Articles.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html', {"message": message, "articles": searched_articles})

    else:
        message = "You havent searched for any term"
        return render(request, 'all-news/search.html', {"message": message})


@login_required(login_url='/accounts/login')
def article(request, article_id):

    try:
        article = Articles.objects.get(id = article_id)

    except DoesNotExist:
        raise Http404()

    return render(request,"all-news/article.html", {"articles": article})


@login_required(login_url='/accounts/login/')
def new_article(request):

    current_user = request.user

    if request.method == 'POST':

        form = NewArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()

    else:

        form = NewArticleForm()

    return render(request, 'new_article.html', {"form": form})


def  newsletter(request):

    name = request.POST.get('your name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()

    send_welcome_email(name, email)

    data = {'success': 'You have been successfully added to our mailing list'}

    return JsonResponse(data)


class MerchList(APIView):

    def get(self, request, format=None):

        all_merch = MoringaMerch.objects.all()

        serializers = MerchSerializer(all_merch, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):

        serializers = MerchSerializer(data=request.data)

        if serializers.is_valid():

            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




