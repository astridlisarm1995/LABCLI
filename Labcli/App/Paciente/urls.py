from django.urls import path, include
from django.contrib.auth.decorators import login_required

from App.Paciente.views import index, Paciente_view, Paciente_list, PacienteList, PacienteCreate,\
    PacienteDelete, PacienteUpdate, index2


from App.Paciente.models import Paciente
app_name = 'App'

urlpatterns = [
    path('', index, name= 'index'),
    path('nuevo',login_required(PacienteCreate.as_view()), name='crear_paciente'),
    path('List',login_required(PacienteList.as_view()), name='ver_lista'),
    path('List2', login_required(index2), name='ver_lista2'),
    path('Editar/<pk>',login_required(PacienteUpdate.as_view()), name='editar_lista'),
    path('Eliminar/<pk>',login_required(PacienteDelete.as_view()), name='eliminar_lista'),
    path('ConsultaDatos', index2, name='index2'),

]
