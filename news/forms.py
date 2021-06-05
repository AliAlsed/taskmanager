from django import forms
from .models import Category,News
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','description']
    
    
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','description','short_description','Author','Image']