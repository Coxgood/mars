from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
#from .forms import PostForm

# Create your views here.



def index(request):
    return render(request, 'articles/index.html')

def article(request):
    articles = Articles.objects.all()
    return render(request, 'articles/article.html', context={'articles': articles})

def article_detail(request, id):
    article = Articles.objects.get(id = str(id))
    return render(request, 'articles/article_detail.html', context={'article': article})

def properties(request):
    properties = Properties.objects.all()
    return render(request, 'articles/properties.html', context={'properties': properties})

def reviews(request):
    #reviews = reversed(Reviews.objects.all()[:5])
    reviews = Reviews.objects.all()
    pager = Paginator(reviews,4)
    page_number = request.GET.get('page', 1)
    page = pager.get_page(page_number)
    current_page = int(page_number)

    if request.user.is_authenticated:
        user = request.user
    else:
        user = 'guest'
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'reviews': page.object_list,
               'user': user,
               'pager': pager,
               'current_page': current_page,
               'next_url': next_url,
               'prev_url': prev_url,
               }
    return render(request, 'articles/reviews.html', context=context)


def review_add(request):
    if request.user.is_authenticated:
        user = str(request.user)
    else:
        user = 'guest'
    reviews = Reviews.objects.all()
    max_id = 0
    for review in reviews:
        if max_id < review.id:
            max_id = review.id
    if request.POST:
        text = request.POST["text"]
        if len(text) > 2:
            new_review = Reviews(id=int(max_id + 1), author=user, text=text)
            new_review.save()
            message = 'пустое сообщение'
    message = None

    return redirect('reviews')


def office(request):
    if request.user.is_authenticated:
        user = str(request.user)
        reviews = reversed(Reviews.objects.filter(author=user))
    else:
        return redirect('home')
    return render(request, 'articles/office.html', context={'reviews': reviews})