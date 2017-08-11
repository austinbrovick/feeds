from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FeedForm
from .models import Feed


def index(request):
    form = FeedForm()
    feeds = Feed.objects.all()
    return render(request, 'feeds/index.html', {'form': form, 'feeds': feeds})


def create_feed(request):
    form = FeedForm(request.POST)
    if form.is_valid():
        try:
            feed = Feed.objects.get(name=form.cleaned_data['name'])
        except Feed.DoesNotExist:
            feed = Feed.objects.create(name=form.cleaned_data['name'])
            feed.save()
            print("saved {}".format(feed))
    return redirect('index')
