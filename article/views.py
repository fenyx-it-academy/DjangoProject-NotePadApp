from django.shortcuts import render, HttpResponse, redirect,get_object_or_404, reverse
from .forms import ArticleForm,FormNologin
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from urllib.parse import quote_plus 
from django import forms



def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles":articles})

    articles = Article.objects.all()

    context = {
        'articles':articles,
    }

    return render(request, "articles.html", context)


def index(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if request.user.is_authenticated:
        notes = Article.objects.filter(author = request.user)
        # articles = get_object_or_404(Article,author=request.user)  

        # count = User.objects.count()
        context = {
            "notes": notes,
            # "count": count,
            "form" : form
        }
        return render(request,"index.html", context)
    else:
        context = {
            # "count": count,
            "form" : form
        }
        return render(request,"index.html", context)


def about(request):
    return render(request, "about.html")

@login_required(login_url = "user:login")        # user disinda birinin linklere girmesiyle yonlendirilecek sayfa icin
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user

        article.save()

        messages.success(request, "Article successfully created.")
        return redirect("/")

    return render(request, "addarticle.html", {"form": form})

def detail(request, id):
    article = get_object_or_404(Article,id=id)
    share_string = quote_plus(article.content)
    context = {
        'article':article,
        'share_string':share_string,
    }
    
    return render(request, "detail.html", context)
    
@login_required(login_url = "user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id= id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article successfully updated.")
        return redirect("/")            # article altindaki dashboard url sine git demek istiyoruz

    return render(request, "update.html", {"form":form})

@login_required(login_url = "user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id= id)

    article.delete()

    messages.success(request, "Article successfully deleted.")

    return redirect("/")            # article altindaki dashboard url sine git demek istiyoruz


def nologin(request):

    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        title = form.cleaned_data['title']
        content =form.cleaned_data['content']    
        dongu_sayisi = [1]           
        args ={"title":title, "content":content, "form": form, "dongu_sayisi":dongu_sayisi}   
    
        return render(request,"nologin.html", {"args":args})
        # return redirect("/", {"args":args})
    
    # return render(request,"index.html",{"form": form})
    return redirect("/")
        


