from __future__ import unicode_literals

import warnings

from django import forms
from django.forms.util import flatatt
from django.template import loader
from django.utils.datastructures import SortedDict
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    email = forms.EmailField(label=_("Email"), max_length=100)
    password = forms.CharField(label=_("Password"), max_length=128)

    error_messages = {
        'invalid_login': _("Please enter a correct %(email)s and password. "
                           "Note that both fields may be case-sensitive."),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        # Set the label for the "username" field.
        UserModel = get_user_model()

        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': self.username_field.verbose_name},
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                )
        return self.cleaned_data

    def check_for_test_cookie(self):
        warnings.warn("check_for_test_cookie is deprecated; ensure your login "
                "view is CSRF-protected.", DeprecationWarning)

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


    def get_formatted_errors(self, override_msg=None):

        formatted_errors = {
            'count': 0,
            'form': [],
            'fields': {}
        }
        if override_msg is None:
            if self.errors.get('__all__') is not None:
                formatted_errors['form'] += self.errors.get('__all__')
                formatted_errors['count'] = len(formatted_errors['form'])
            for name, field in self.fields.items():
                formatted_errors['fields'][name] = []
                if self.errors.get(name) is not None:
                    formatted_errors['fields'][name] += self.errors.get(name)
                    formatted_errors['count'] += len(formatted_errors['fields'][name])
        else:
            formatted_errors['form'] = [override_msg]
            formatted_errors['count'] = 1

        return formatted_errors
