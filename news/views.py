from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

import datetime as dt

from .models import Articles


# Create your views here.

def welcome(request):

    return render(request, 'welcome.html')


def news_of_day(request):

    date = dt.date.today()

    return HttpResponse()


def news_today(request):

    date = dt.date.today()

    news = Articles.todays_news()

    return render(request, 'all-news/todays-news.html', {"date": date,"news":news})

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

    if 'articles' in request.GET and request.GET['articles']:

        search_term = request.GET.get('articles')

        searched_articles = Articles.search_by_title(search_term)

        message = f'{search_term}'

        return render(request, 'all-news/search.html', {'message':message, 'articles':searched_articles})

    else:

        message = "You haven't searched for any article"

        return render(request, 'all-news/search.html', {'message':message})


def article(request, article_id):

    try:
        articles = Articles.objects.get(id - article_id)

    except:
        raise Http404()

    return render(request, 'all-news/article.html', {'articles':articles})


