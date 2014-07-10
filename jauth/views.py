from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def login_email_submit(request):
    """
    index page
    :param request:
    :return:
    """
    resp = {
        'error': 'this is an error',
    }
    response = HttpResponse(json.dumps(resp))
    response['Content-Type'] = 'application/json'
    return response
