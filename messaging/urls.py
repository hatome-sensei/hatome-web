"""hatome messaging URL Configuration
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mailbox, name = 'mailbox'),
    url(r'^new$', views.create_message, name = 'new'),
]

