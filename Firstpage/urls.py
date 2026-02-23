from django.urls import path
from Firstpage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appeal/<int:pk>/', views.appeal_detail, name='appeal_detail'),
]
