from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone']

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro',
                code='Invalid'
            )
            )
        self.add_error(
            None,
            ValidationError(
                'Mensagem de erro 2',
                code='Invalid'
            )

        )

        return super().clean()



app_name = 'contact'

def create(request):
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST),
            'site_title': 'Create Contact - ',
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'site_title': 'Create Contact - ',
    }

    return render(
        request,
        'contact/create.html',
        context
    )