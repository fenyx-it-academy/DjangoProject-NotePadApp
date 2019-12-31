from django.shortcuts import render, HttpResponse, redirect,get_object_or_404, reverse
import operator
from ckeditor.fields import RichTextField
from .forms import NologinForm


# Create your views here.
def nologin(request): 
    form = NologinForm(request.POST or None, request.FILES or None)   
    return render(request, 'nologin.html',{"form": form})
  
