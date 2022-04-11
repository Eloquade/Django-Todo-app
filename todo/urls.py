from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.submit, name='submit'),
    path('list/',views.list, name='list'),

    path('updatetodo/<str:pk>/', views.updatetodo, name='updatetodo')
]
