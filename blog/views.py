from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Post 1',
        'content': 'first post content',
        'date_posted': '10/9/2019'
    },
    {
        'author': 'Daniel X',
        'title': 'Post 2',
        'content': 'second post content',
        'date_posted': '10/11/2019'
    },
]



def home(request):

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):

    context = {
        'title': 'About'
    }

    return render(request, 'blog/about.html', context)

