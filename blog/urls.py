from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    path('post/new/$', views.post_new, name='post_new'),
]

