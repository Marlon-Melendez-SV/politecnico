from  django.shortcuts import render,redirect
from django.core.mail import send_mail

from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

def correo(request):
    return render(request,'correo.html')

def enviar_correo(request):
    if request.method=='POST':
        destinario=request.POST.get('destinatario')
        asunto=request.POST.get('asunto')
        mensaje=request.POST.get('mensaje')

        try:
            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, {destinario}, fail_silently=False)
            messages.success(request,'Mensaje Enviado con Exito.')
        
        except Exception as e:
            messages.error(request, f'El mensaje No se pudo enviar:  {e}')
    
    return redirect('/correo')

def enviar_correo_dos(request):
    if request.method=='POST':
        destinario=request.POST.get('destinatario')
        asunto=request.POST.get('asunto')
        mensaje=request.POST.get('mensaje')
        adjunto=request.FILES.get('anexa_archivo')

        try:
            correo=EmailMessage(asunto, mensaje, settings.EMAIL_HOST_USER, {destinario})

            if adjunto:
                correo.attach(adjunto.name, adjunto.read(), adjunto.content_type )
            correo.send(fail_silently=False)
            messages.success(request,'Mensaje Enviado con Exito.')
        
        except Exception as e:
            messages.error(request, f'El mensaje No se pudo enviar:  {e}')
    
    return redirect('/correo')
