from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('input_page',views.user_check, name='input_page'),
    path('result_page',views.show_result, name='result_page'),
]