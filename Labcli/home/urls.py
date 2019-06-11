from django.urls import path

from home.views import home, examenes, servicios, contacto, services, services3
from home.views import ContactEmail

app_name = 'App'

urlpatterns = [
    path('', home, name='home'),
    path('Examenes', examenes, name='examenes'),
    path('Servicios', servicios, name='servicios'),
    path('Contacto', ContactEmail, name='contacto'),
	path('Services', services, name='services'),
	path('Services3', services3, name='services3'),
    path('ContactEmail', ContactEmail, name="ContactEmail"),
]
# Create your models here.
