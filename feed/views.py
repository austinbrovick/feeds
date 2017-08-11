from django.shortcuts import render


def index(request, feed):

    return render(request, 'feed/index.html', {'feed_name': feed})
