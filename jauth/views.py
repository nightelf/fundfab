from django.shortcuts import render
from django.http import HttpResponse, request
from jauth.forms import AuthenticationForm
from django.utils.http import base36_to_int, is_safe_url, urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.conf import settings
import logging
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
    resp = {
        'error': {
            'form': [],
            'email': [],
            'password': [],
        },
        'success': []
    }
    if request.method == "POST" and request.is_ajax():

        data = json.loads(str(request.body, 'utf-8'))
        form = AuthenticationForm(request, data)
        #import ipdb; ipdb.set_trace()
        try:
            if form.is_valid():
                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())
                user = form.get_user()
                if user is not None:
                    # the password verified for the user
                    if user.is_active:
                        resp['success'].append("User is valid, active and authenticated")
                        resp['csrfCookie'] = request.META.get('CSRF_COOKIE')
                    else:
                        resp['error']['form'].append("The password is valid, but the account has been disabled!")
                else:
                    # the authentication system was unable to verify the username and password
                    resp['error']['form'].append("The username and password were incorrect.")
            else:
                if form.errors.get('__all__') is not None:
                    resp['error']['form'] += form.errors.get('__all__')
                if form.errors.get('email') is not None:
                    resp['error']['email'] += form.errors.get('email')
                if form.errors.get('password') is not None:
                    resp['error']['password'] += form.errors.get('password')

        except Exception as e:
            resp['error'] = ["An error occurred. Please contact the system admin."]
    resp['redirect_to'] = redirect_to

    response = HttpResponse(json.dumps(resp))
    response['Content-Type'] = 'application/json'
    return response
