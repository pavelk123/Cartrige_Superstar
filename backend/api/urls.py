from django.urls import path

from . import views

urlpatterns = [
    path('',views.api_home),#'http://127.0.0.1:8000/api/'
    path('create_printer_producer/',views.api_create_printer_producer)
]