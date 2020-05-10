from django.shortcuts import render

posts = [
    {'author': 'John Doe',
     'title': 'Blog Post One',
     'content': 'Post Content',
     'date_posted': 'May 20, 2020'
     },
    {'author': 'John Devil',
     'title': 'Blog Post Two',
     'content': 'Post Two Content',
     'date_posted': 'May 10, 2020'
     },
    {'author': 'Akash Michele',
     'title': 'Blog Post Three',
     'content': 'Post Three Content',
     'date_posted': 'May 11, 2020'
     }
]


# Create your views here.

def home(request):
    # pass a posts data as dictionary
    return render(request, 'blog/home.html', {'post_dict': posts})


def about(request):
    return render(request, 'blog/about.html')
