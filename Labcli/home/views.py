from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render
from django.views.generic import TemplateView

from usuario.forms import FormularioContacto
from django.core.mail import EmailMessage

def home(request):
    return render(request, 'home.html')

def examenes(request):
    return render(request, 'examenes.html')

def servicios(request):
    return render(request, 'services.html')

def contacto(request):
    return render(request, 'contacto_email.html')

def services(request):
    return render(request, 'services2.html')     

def services3(request):
    return render(request, 'services3.html')   

# Create your views here.

from django.core.mail import send_mail

def ContactEmail(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			asunto = formulario.cleaned_data['asunto']
			mensaje = formulario.cleaned_data['mensaje']
			usuario = formulario.cleaned_data['usuario']
			msg_mail = str(mensaje) + '\n'+ "Enviado por: " + str(usuario)
			mail = EmailMessage(asunto, msg_mail, to = ['laboratorioclinicolainmaculada@gmail.com'], reply_to=[usuario])			
			mail.send()
		return render(request, 'home.html')
	
	else:
		formulario = FormularioContacto()


	return render(request, 'contacto_email.html', {'formulario':formulario}) 

