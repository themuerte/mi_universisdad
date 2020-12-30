from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def formularioContacto(request):
    return render(request, "formulario.html")

def contactar(request):
    if request.method == 'POST':
        asunto = request.POST['txt_asunto']
        mensaje = request.POST['txt_mensaje'] + "/Email" + request.POST['txt_email']
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["ganvito1999tuna@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contacto_exito.html")
    else:
        return render(request, "formulario.html")

    