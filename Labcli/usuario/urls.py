from django.urls import path
from usuario.views import RegistroUsuario, UserAPI
from usuario.views import ContactEmail
app_name = 'App'

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('api', UserAPI.as_view(), name="api"),
    path('ContactEmail', ContactEmail, name="ContactEmail"),

]
