from django.urls import path
from .views import lista_vagas, cadastrar_vaga

app_name = 'vagas'

urlpatterns = [
    path('', lista_vagas, name='lista'),
    path('/cadastrar/', cadastrar_vaga, name='cadastrar_vaga'),
]