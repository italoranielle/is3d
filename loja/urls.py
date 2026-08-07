# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:54:36 2021

@author: pc_lab
"""

from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
     path('', views.index, name = 'index'),
     path('loja', views.loja, name = 'loja'),
     path('produto/<int:pk>', views.ProdutoDetail.as_view(), name = 'produto'),
     path('produto/novo', views.ProdutoNovo.as_view(), name = 'produtonovo'),
     path('produto/edit/<int:pk>', views.ProdutoEdit.as_view(), name = 'produtoedit'),
     path('produto/addImage/<int:pk>', views.addImage, name = 'addImage'),

    ]

