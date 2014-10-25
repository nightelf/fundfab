from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    """
    index page
    :param request:
    :return:
    """
    template = loader.get_template('mainapp/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
