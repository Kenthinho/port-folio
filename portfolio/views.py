from django.shortcuts import render
from .models import Contact
# from django.core.mail import send_mail
# Create your views here.


def home_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contact_list = Contact.objects.create(
            name=name, email=email, message=message)
        context['contact'] = contact_list

        return render(request, 'index.html', context)
    return render(request, 'index.html')
