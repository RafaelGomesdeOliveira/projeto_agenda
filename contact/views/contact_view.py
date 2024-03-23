from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


from contact.models import Contact

# Create your views here.

app_name = 'contact'

def index(request):

    contact_list = Contact.objects.all().filter(show=True).order_by('-id')
    paginator = Paginator(contact_list, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page" )
    page_obj = paginator.get_page(page_number)

    # contacts = Contact.objects.all().filter(show=True).order_by('-id') #Tenho que me atentar aos filtros que uso e colocalos em todos as views
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, id):

    single_contact = get_object_or_404(Contact.objects.filter(pk=id, show=True)) #Posso ou não usar o .objects
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
 
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }

    return render(
        request,
        'contact/contact.html',
        context
    )


def search(request,):

    search_value = request.GET.get('q', '').strip() #É como se fosse um dicionário
    if search_value == '': #Se é uma string vazia ele retorna para a index
        return redirect('contact:index')

    contacts = Contact.objects.all().filter(show=True).filter(

        Q(first_name__icontains=search_value) | 
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) | 
        Q(email__icontains=search_value) 
        
        ).order_by('-id') 
    
    paginator = Paginator(contacts, 10)  # Show 25 contacts per page.

    page_number = request.GET.get("page" )
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'contacts': contacts,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )