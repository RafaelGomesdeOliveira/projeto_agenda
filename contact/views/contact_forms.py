from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


from contact.models import Contact

# Create your views here.

app_name = 'contact'

def create(request):

    contact_list = Contact.objects.all().filter(show=True).order_by('-id')




    # contacts = Contact.objects.all().filter(show=True).order_by('-id') #Tenho que me atentar aos filtros que uso e colocalos em todos as views
    context = {

        'site_title': 'Create Contact - '
    }

    return render(
        request,
        'contact/create.html',
        context
    )
