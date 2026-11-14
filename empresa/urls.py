from django.urls import path
from .views import lista_vagas

app_name = 'vagas'

urlpatterns = [
    path('', lista_vagas, name='lista'),
]