from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from blog.forms import ContactForms
from blog.models import *
from .utils import paginate


@csrf_exempt
# @cache_page(60 * 1)
def home(request):
    posts = Post.objects.all().order_by('-created')

    page = request.GET.get('page')
    q = request.GET.get('q')
    if q:
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(tag__name__icontains=q)
        ).distinct()
    posts = paginate(posts, page, 5)

    ctx = {
        'posts': posts
    }
    return render(request, 'blog/index.html', ctx)


# @cache_page(60 * 1)
def tag(request, key):
    posts = Post.objects.filter(tag__slug__iexact=key).order_by('-created')

    page = request.GET.get('page')
    posts = paginate(posts, page, 5)

    ctx = {
        'posts': posts
    }
    return render(request, 'blog/index.html', ctx)


# @cache_page(60 * 1)
def detail(request, key):
    post = get_object_or_404(Post, slug=key)
    ctx = {
        'post': post
    }
    return render(request, 'blog/detail.html', ctx)


def about(request):
    setting = Setting.objects.first()
    ctx = {
        'setting': setting
    }
    return render(request, 'blog/about.html', ctx)


@csrf_exempt
# @cache_page(60 * 1)
def contact(request):
    back_message = None
    form = ContactForms(request.POST or None)
    if form.is_valid():
        form.save()
        back_message = 'Your message sent successfully!'
        form = None

    ctx = {
        'back_message': back_message,
        'form': form,
    }
    return render(request, 'blog/contact.html', ctx)
