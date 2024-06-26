"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('book/<pk>', BookDetailView.as_view(), name='book_detail'),
    path('create-book', BookFormView.as_view(), name='create_book'),
    path('sign-in', SignInView.as_view(), name='sign_in'),
    path('sign-up', SignUpView.as_view(), name='sign_up'),
    path('sign-out', SignOutView.as_view(), name='sign_out'),
    path('book/<pk>/status/<status>', update_book_status, name='update_book_status'),
    path('book/<pk>/delete', delete_book, name='delete_book')
]
