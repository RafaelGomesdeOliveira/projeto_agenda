from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from contact.models import Contact
from contact.forms import ContactForm


app_name = 'contact'




@login_required(login_url='contact:login ')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'site_title': 'Create Contact - ',
            'form_action': form_action,
        }

        if form.is_valid():
            #contact = form.save(commit=False)
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            
            return redirect('contact:update', id=contact.id)

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

@login_required(login_url='contact:login ')
def update(request, id):
    contact = get_object_or_404(Contact, id=id, show=True, owner=request.user)

    form_action = reverse('contact:update', args=(id,)) #Aqui eu passo os valores dinâmicos da urls

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'site_title': 'Create Contact - ',
            'form_action': form_action,
        }

        if form.is_valid():
            #contact = form.save(commit=False)
            contact = form.save()
            contact.save()
            
            return redirect('contact:update', id=contact.id)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(instance=contact),
        'site_title': 'Create Contact - ',
    }

    return render(
        request,
        'contact/create.html',
        context
    )


@login_required(login_url='contact:login ')
def delete(request, id):
    contact = get_object_or_404(Contact, id=id, show=True, owner=request.user)


    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render (
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )