from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        return context
    

class BookFormView(LoginRequiredMixin,FormView):
    login_url = '/sign_in'
    template_name = 'books/create_book.html'
    form_class = BookForm
    success_url = '/create-book?success=true'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        return context
    


class SignInView(LoginView):
    template_name = 'books/sign_in.html'
    next_page = '/'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        return context


class SignOutView(LogoutView):
    next_page = '/'


class SignUpView(FormView):
    template_name = 'books/sign_up.html'
    form_class = SignupForm
    success_url = '/sign-in'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        User.objects.create_user(**form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_authenticated'] = self.request.user.is_authenticated
        return context


@login_required(login_url='/sign-in')
def update_book_status(request,pk,status):
    status = int(status)
    pk = int(pk)
    if request.method == 'POST' and (status == '0' or status == 1):
        print('here')
        try:
            book = Book.objects.get(pk=pk);
            book.checked_out_by = None if status == 0 else request.user
            book.save()
        except Book.DoesNotExist:
            pass
    return redirect(f"/book/{pk}")


@login_required(login_url='/sign-in')
def delete_book(request,pk):
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=pk);
            book.delete()
        except Book.DoesNotExist:
            pass
    return redirect('/')