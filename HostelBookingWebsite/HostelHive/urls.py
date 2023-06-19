from django.contrib import admin
from django.urls import path 
from HostelHive import views
urlpatterns = [
    path('', views.index,name='HostelHive'),
    path('home/', views.home,name='Home'),
    path('about/', views.about,name='About'),
    path('booknow/', views.booknow,name='booknow'),
    path('pricing/', views.pricing,name='pricing'),

    # path('Reviews', views.Reviews,name='Reviews'),
    # path('Faq', views.Faq,name='Faq'),
    # path('khubaib/', views.khubaib,name='Khubaib'),
]
