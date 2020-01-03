from django import forms
from .models import Article
# from ckeditor.fields import RichTextField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content","article_image"]

class FormNologin(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    created_date = forms.DateTimeField()
    article_image = forms.FileField()
 