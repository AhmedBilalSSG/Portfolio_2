from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from app import *

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_view', views.contact_view, name='contact_view')
]