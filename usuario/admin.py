from django.contrib import admin
from .models import Usuario, ExperienciaProfissional, Habilidade, Idioma, FormacaoAcademica, Telefone, Endereco

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'data_nascimento', 'cpf', 'rg', 'sexo', 'nacionalidade', 'estado_civil', 'profissao', 'escolaridade', 'data_cadastro', 'data_atualizacao')
    search_fields = ('user__username', 'cpf', 'rg')
    list_filter = ('estado_civil', 'profissao', 'escolaridade', 'nacionalidade', 'data_cadastro', 'data_atualizacao')

@admin.register(ExperienciaProfissional)
class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'empresa', 'cargo', 'data_inicio', 'data_fim')
    search_fields = ('usuario__user__username', 'empresa', 'cargo')
    list_filter = ('data_inicio', 'data_fim')

@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome', 'nivel')
    search_fields = ('usuario__user__username', 'nome')
    list_filter = ('nivel',)

@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome', 'nivel')
    search_fields = ('usuario__user__username', 'nome')
    list_filter = ('nivel',)

@admin.register(FormacaoAcademica)
class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'instituicao', 'curso', 'data_inicio', 'data_fim')
    search_fields = ('usuario__user__username', 'instituicao', 'curso')
    list_filter = ('data_inicio', 'data_fim')

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'numero', 'tipo')
    search_fields = ('usuario__user__username', 'numero')
    list_filter = ('tipo',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'logradouro', 'cidade', 'estado', 'cep')
    search_fields = ('usuario__user__username', 'logradouro', 'cidade', 'estado', 'cep')
    list_filter = ('cidade', 'estado')
