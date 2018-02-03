"""hatome messaging URL Configuration
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mailbox),
    url(r'^new$', views.create_message),
]
