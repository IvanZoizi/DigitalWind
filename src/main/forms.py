from cProfile import label

from django import forms
from .models import Posts

class FormPost(forms.ModelForm):
    description = forms.CharField(max_length=1000, label='Описание', widget=forms.Textarea)
    class Meta:
        model = Posts
        fields = ["title", "image", "description"]