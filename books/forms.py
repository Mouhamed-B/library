from django import forms
from django.contrib.auth.models import User
from .models import Book

class BookForm(forms.ModelForm):    
    class Meta:
        model = Book
        exclude = ('checked_out_by',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget = forms.Textarea()
        self.fields['description'].widget.attrs.update({'class': 'form-control'})


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs.update({'class': 'form-control'})