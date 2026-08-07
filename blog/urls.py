# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:17:49 2021

@author: pc_lab
"""

from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #path('', views.index, name = 'home'),
    path('posts/<int:pg>', views.postList, name = 'postList'),
    path('posts/search/', views.postSearch, name = 'postSearchList'),
    path('posts/<slug:slug>', views.PostDetail.as_view(), name = 'postDetail'),
    path('newpost', views.PostCreate.as_view(), name = 'postCreate'),
    path('editpost/<int:pk>', views.PostEdit.as_view(), name = 'postEdit'),
    ]