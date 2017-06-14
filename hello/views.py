from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def say_hello(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html',{'contacts_list': contacts})


def add_Contact(request):
    if request.method == "POST":
        new = Contact()
        new.first_name = request.POST.get('first_name')
        new.mobile = request.POST.get('mobile_number')
        new.email = request.POST.get('email_address')

        new.save()
        






        return render(request, 'contactsadded.html', {'contact': new})
    else:
        return render(request, 'addcontact.html')
      

