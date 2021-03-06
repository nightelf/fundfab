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
        'error': {},
        'success': {'pass': False, 'message': ''},
        'redirect_to': redirect_to,
        'csrfCookie': None
    }
    override_msg = None
    if request.method == "POST" and request.is_ajax():

        data = json.loads(str(request.body, 'utf-8'))
        form = AuthenticationForm(request, data)
        #import ipdb; ipdb.set_trace()
        try:
            if form.is_valid():
                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    resp['redirect_to'] = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())
                user = form.get_user()
                if user is not None:
                    # the password verified for the user
                    if user.is_active:
                        resp['success']['pass'] = True
                        resp['success']['message'] = "Welcome."
                        # remove once cookie catch is done.
                        resp['csrfToken'] = request.META.get('CSRF_COOKIE')

        except Exception as e:
            override_msg = "An error occurred. Please contact the system admin."
        resp['error'] = form.get_formatted_errors(override_msg=override_msg)

    response = HttpResponse(json.dumps(resp))
    response['Content-Type'] = 'application/json'
    return response
