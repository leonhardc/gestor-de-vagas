from django.contrib import admin
from .models import Empresa, Vaga, Candidatura, EventoCandidatura

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nome', 'cnpj', 'telefone', 'email', 'data_cadastro', 'data_atualizacao']
    search_fields = ['usuario', 'nome', 'cnpj', 'telefone', 'email', 'data_cadastro', 'data_atualizacao']
    list_filter = [ 'usuario', 'nome', 'cnpj', 'telefone', 'email', 'data_cadastro', 'data_atualizacao']

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ['empresa', 'titulo', 'modelo_de_trabalho', 'tipo_de_emprego', 'salario', 'localizacao', 'data_cadastro', 'data_atualizacao']
    search_fields = ['empresa', 'titulo', 'modelo_de_trabalho', 'tipo_de_emprego', 'salario', 'localizacao', 'data_cadastro', 'data_atualizacao']
    list_filter = ['empresa', 'titulo', 'modelo_de_trabalho', 'tipo_de_emprego', 'salario', 'localizacao', 'data_cadastro', 'data_atualizacao']

@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = [ 'vaga', 'usuario', 'status', 'aplicado_em', 'data_cadastro', 'data_atualizacao']
    search_fields = [ 'vaga', 'usuario', 'status', 'aplicado_em', 'data_cadastro', 'data_atualizacao']
    list_filter = [ 'vaga', 'usuario', 'status', 'aplicado_em', 'data_cadastro', 'data_atualizacao']

@admin.register(EventoCandidatura)
class EventoCandidaturaAdmin(admin.ModelAdmin):
    list_display = ['candidatura', 'tipo_evento', 'data_evento', 'criado_em']
    search_fields = ['candidatura', 'tipo_evento', 'data_evento', 'criado_em']
    list_filter = ['candidatura', 'tipo_evento', 'data_evento', 'criado_em']

