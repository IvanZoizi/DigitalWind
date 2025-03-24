from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from utils import DataMixin
from .models import Posts
from .forms import FormPost


class IndexView(DataMixin, ListView):
    template_name = 'index.html'
    model = Posts

    def get_context_data(self, **kwargs):
        contect = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='')
        return dict(list(contect.items()) + list(c_def.items()))


def get_form_data(request):
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            post = Posts(title=data['title'], image=data['image'], description=data['description'])
            post.save()
            return redirect('home')
    else:
        form = FormPost()
    return render(request, 'form.html', {"form": form})