"""book_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    # 出版社相关的对应关系
    url(r'^publisher_list/$', views.publisher_list, name='publisher_list'),
    url(r'^add_publisher/$', views.AddPublisher.as_view(), name='add_publisher'),
    # url(r'^add_publisher/', views.add_publisher, name='add_publisher'),
    url(r'^delete_publisher/([0-9]+)/$', views.delete_publisher, name='delete_publisher'),
    url(r'^edit_publisher/([0-9]+)/$', views.edit_publisher, name='edit_publisher'),

    # 书相关的对应关系
    url(r'^book_list/$', views.book_list, name='book_list'),
    url(r'^add_book/$', views.add_book, name='add_book'),
    url(r'^delete_book/([0-9]+)/$', views.delete_book, name='delete_book'),
    url(r'^edit_book/([0-9]+)/$', views.edit_book, name='edit_book'),

    # 作者相关的对应关系
    url(r'^author_list/$', views.author_list, name='author_list'),
    url(r'^add_author/$', views.add_author, name='add_author'),
    url(r'^delete_author/([0-9]+)/$', views.delete_author, name='delete_author'),
    url(r'^edit_author/([0-9]+)/$', views.edit_author, name='edit_author'),
]
