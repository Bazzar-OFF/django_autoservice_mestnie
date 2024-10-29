from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('car_wash', car_wash, name='car_wash'),
    path('mainenance', mainenance, name='mainenance'),
    path('tire_service', tire_service, name='tire_service'),
    path('reviews', reviews, name='reviews'),
    path('add_review', add_review, name='add_review'),

    path('form', views.form, name='form'),

]