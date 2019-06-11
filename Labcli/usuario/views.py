# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.shortcuts import render 
from django.http import HttpResponseRedirect

#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from django.core.mail import EmailMessage
User = get_user_model()

from django.views.generic import CreateView
from django.urls import reverse_lazy
import json
from rest_framework.views import APIView

from usuario.forms import RegistroForm
from usuario.forms import FormularioContacto

from usuario.serializer import UserSerializer


class RegistroUsuario(CreateView):
    model = User
    template_name = "templates/usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('Paciente:crear_paciente')





class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')


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
		return HttpResponse('Enviado')
	
	else:
		formulario = FormularioContacto()


	return render(request, 'contacto_email.html', {'formulario':formulario}) 



