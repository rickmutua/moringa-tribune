from django.test import TestCase
from .models import Editor, Articles, Tags

import datetime as dt

# Create your tests here.


class EditorTestCase(TestCase):

    def setUp(self):

        self.erick = Editor(first_name = 'Erick', last_name = 'Mutua', email = 'rick@mutua.com')


    def test_instance(self):

        self.assertTrue(isinstance(self.erick, Editor))


    def test_save_method(self):

        self.erick.save_editor()

        editors = Editor.objects.all()

        self.assertTrue(len(editors) > 0 )


class ArticlesTestCase(TestCase):

    def setUp(self):

        self.erick = Editor(first_name='Erick', last_name='Mutua', email='rick@mutua.com')
        self.erick.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name='testing')
        self.new_tag.save()

        self.new_article = Articles(title='The Holiday', post='The long awaited holiday is finally here!', editor=self.erick)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Articles.objects.all().delete()


    def test_get_news_today(self):

        today_news = Articles.todays_news()

        self.assertTrue(len(today_news) > 0 )

    def test_get_news_by_date(self):

        test_date = '2017-11-04'

        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()

        news_by_date = Articles.days_news(date)

        self.assertTrue(len(news_by_date) == 0)
