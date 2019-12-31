from django import forms
from .models import NologinForm


class NologinForm(forms.ModelForm):
    class Meta:
        model = NologinForm
        fields = ["title", "content","article_image"]