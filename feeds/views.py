from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FeedForm
from .models import Feed



def index(request):
    form = FeedForm()
    return render(request, 'feeds/index.html', {'form': form})


def create_feed(request):
    # form = FeedForm(request.POST)
    # if form.is_valid():
        # try:
        # feed = Feed.objects.get(name=form.cleaned_data['name']
        # except Feed.DoesNotExist:
        #     print("yup")
        #     feed = Feed.objects.create(name=form.cleaned_data['name'])
        #     feed.save()
    form = FeedForm(request.POST)
    if form.is_valid():
        try:
            feed = Feed.objects.get(name=form.cleaned_data['name'])
        except Feed.DoesNotExist:
            feed = Feed.objects.create(name=form.cleaned_data['name'])
            feed.save()
            print("saved {}".format(feed))
    return redirect('index')
