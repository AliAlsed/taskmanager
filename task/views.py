
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Review
from .models import Task, Profile, News
from .forms import ReviewForm
# Create your views here.


def index(request):
    print(request.user)
    # get for one value
    profile = Profile.objects.get(user=request.user)
    # filter use dor more than one value s
    tasks = Task.objects.filter(user=request.user).all()
    context = {
        'all_task': tasks,
        'profile': profile
    }
    print(profile.image.url)
    return render(request, 'index.html', context)


def detail(request, id):
    task = Task.objects.get(pk=id)
    reviewlist = Review.objects.filter(task=task).all()
    newinstance = Review(task=task, user=request.user)
    form = ReviewForm(request.POST or None, instance=newinstance)
    if request.method == "POST" and form.is_valid:
        form.save()
        return redirect('index')
    context = {
        'task': task,
        'reviews': reviewlist,
        'form': form
    }
    return render(request, 'detail.html', context)


def newshome(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'newstemp.html', context)


def newsdetail(request, id):
    news = News.objects.get(pk=id)
    context = {
        'news': news
    }
    return render(request, 'newsdetailtemp.html', context)


def tasks(request):
    tasks = Task.objects.all()
    context = {
        'alltask': tasks
    }
    return render(request, 'alltask.html', context)
