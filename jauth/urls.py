from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'login-email-submit', 'jauth.views.login_email_submit'),
)
