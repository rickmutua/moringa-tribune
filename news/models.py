from django.db import models
from tinymce.models import HTMLField

import datetime as dt

# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()


class Tags(models.Model):

    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Articles(models.Model):

    title = models.CharField(max_length = 60)
    post = HTMLField()

    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tags)

    pub_date = models.DateTimeField(auto_now_add = True)

    article_image = models.ImageField(upload_to = 'articles/')

    def save_article(self):
        self.save()

    @classmethod
    def todays_news(cls):

        today = dt.date.today()

        news = cls.objects.filter(pub_date__date = today)

        return news

    @classmethod
    def days_news(cls, date):

        news = cls.objects.filter(pub_date__date = date)

        return news

    @classmethod
    def search_by_article(cls, search_term):

        news = cls.objects.filter(title__icontains=search_term)

        return news


class NewsLetterRecipients(models.Model):

    name = models.CharField(max_length=65)

    email = models.EmailField()


class MoringaMerch(models.Model):

    name = models.CharField(max_length=40)

    description = models.TextField()

    price = models.DecimalField(decimal_places=2, max_digits=20)


