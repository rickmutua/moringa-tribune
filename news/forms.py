from django import forms
from .models import Articles


class NewsLetterForm(forms.Form):

    your_name = forms.CharField(label='Name',max_length=65)

    email = forms.EmailField(label='Email')


class NewArticleForm(forms.ModelForm):

    class Meta:

        model = Articles

        exclude = ['user', 'pub_date']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

