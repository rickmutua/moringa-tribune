from django import forms


class NewsLetterForm(forms.Form):

    your_name = forms.CharField(label='Name',max_length=65)

    email = forms.EmailField(label='Email')

