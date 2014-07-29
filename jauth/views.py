from django.shortcuts import render
from django.http import HttpResponse, request
from jauth.forms import AuthenticationForm
from django.utils.http import base36_to_int, is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.conf import settings
import sys
import jauth.models
import json

import json

# Create your views here.

def login_email_submit(request, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    index page
    :param request:
    :return:
    """

    #Displays the login form and handles the login action.
    redirect_to = request.REQUEST.get(redirect_field_name, '')
    resp = {}
    if request.method == "POST" and request.is_ajax():

        data = json.loads(str(request.body, 'utf-8'))
        form = AuthenticationForm(request, data)

        try:
            if form.is_valid():

                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())
        except Exception as e:
            resp['error'] = e.args
    resp['redirect_to'] = redirect_to

    response = HttpResponse(json.dumps(resp))
    response['Content-Type'] = 'application/json'
    return response
