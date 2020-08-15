from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Article, Category

# Create your views here.
def home(request,page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list,6)
    articles = paginator.get_page(page)
    context = {
        "articles" : articles,
    }
    return render(request, "blog/home.html", context)

def detail(request,slug): 
    
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug=slug),

    }
    return render(request, "blog/detail.html", context)

def category(request,slug,page=1):
    category = get_object_or_404(Category.objects.active(), slug=slug)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list,6)
    articles = paginator.get_page(page)
    context = {
        "category": category, 
        "articles": articles,
    }
    return render(request, "blog/category.html", context)

def author(request,username,page=1):
    author = get_object_or_404(User, username=username)
    articles_list = author.articles.published()
    paginator = Paginator(articles_list,5)
    articles = paginator.get_page(page)
    context = {
        "author": author, 
        "articles": articles,
    }
    return render(request, "blog/author_list.html", context)

    # class AuthorList(ListView):
#     Paginate_by = 5
#     template_name='blog/author_list.html'
    
#     def get_queryset(self):
#         global author
#         username = self.kwargs.get('username')
#         author = get_object_or_404(User,username=username)
#         return author.articles.published

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["author"] = author
#         return context
