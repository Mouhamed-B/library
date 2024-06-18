from django import forms
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
