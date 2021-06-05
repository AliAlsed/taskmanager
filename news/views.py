from django.shortcuts import redirect, render
from .forms import CategoryForm, NewsForm
from .models import Category
# Create your views here.


def newsindex(request):
    pass


def create(request):
    pass


def category_index(request):
    Categories = Category.objects.all()
    return render(request, 'category/index.html', {'categories': Categories})


def Create_Category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CategoryForm()
        return redirect('category_index')
    return render(request, 'category/create.html', {'form': form})
