from django.shortcuts import render, redirect
from django.urls      import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

# Create your views here.
def contact(request):
    contactForm = ContactForm()

    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)

        if contactForm.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            print(f'[{name}][{email}][{message}]')

            # Enviamos el correo y redireccionamos...
            emailMessage = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                f'De { name } <{ email }>\n\nEscribió:\n\n{ message }',
                'no-reply@inbox.mailtrap.io',
                ['estebandbarrios@hotmail.com'],
                reply_to=[email]
            )

            try:
                emailMessage.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')

    return render(request, 'contact/contact.html', { 'form': contactForm })
