__author__ = 'jared'

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Test Response.</h1>")