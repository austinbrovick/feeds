from django import forms

class FeedForm(forms.Form):
    name = forms.CharField(label='Feed Name', max_length=100)
