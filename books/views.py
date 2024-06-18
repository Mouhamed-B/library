from typing import Any
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
# Create your views here.

class BookListView(ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        return context


class BookDetailView(DetailView):
    model = Book
    

class BookFormView(LoginRequiredMixin,FormView):
    login_url = '/sign-in/'
    template_name = 'books/create_book.html'
    form_class = BookForm
    success_url = '/create_book?success=true'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form)
        form.save()
        return super().form_valid(form)


class SignInView(LoginView):
    template_name = 'books/sign_in.html'
    next_page = '/'
    redirect_authenticated_user = True