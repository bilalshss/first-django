from django.urls import path
from . import views

app_name='amstream'

urlpatterns=[
    path('',views.index, name="index"),
]