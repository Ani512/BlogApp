from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Anirudh Umarji',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Rahul Raj',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'November 5, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')
