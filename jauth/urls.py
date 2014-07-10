from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'login-email-submit', 'jauth.views.login_email_submit'),
)
