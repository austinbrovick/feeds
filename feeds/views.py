from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FeedForm



def index(request):
    form = FeedForm()
    return render(request, 'feeds/index.html', {'form': form})


def create_feed(request):
    form = FeedForm(request.POST)
    if form.is_valid():
        print("hello world")
        return redirect('index')
