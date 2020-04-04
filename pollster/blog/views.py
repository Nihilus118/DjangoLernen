from django.shortcuts import render

from .models import Post


# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()[:10]
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')
