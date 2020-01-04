from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]

class FormNologin(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    created_date = forms.DateTimeField()