from django.forms import ModelForm
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):

        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter Review title...'})
        self.fields['content'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter Content here...'})
