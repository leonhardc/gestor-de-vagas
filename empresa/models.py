from django.db import models
from usuario.models import Usuario
from empresa.constants import modelo_de_trabalho_choices, tipo_de_emprego_choices, encontrado_em_choices, status_choices

class Empresa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=255, verbose_name="Nome")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    email = models.EmailField(max_length=255, verbose_name="Email")
    linkedin_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="LinkedIn")
    website_url = models.URLField(max_length=255, blank=True, null=True, verbose_name="Website")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.nome

class Vaga(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    url_vaga = models.URLField(max_length=255, blank=True, null=True, verbose_name="URL da Vaga")
    modelo_de_trabalho = models.CharField(max_length=50, choices=modelo_de_trabalho_choices, blank=True, null=True, verbose_name="Modelo de Trabalho")
    tipo_de_emprego = models.CharField(max_length=50, choices=tipo_de_emprego_choices, blank=True, null=True, verbose_name="Tipo de Emprego")
    encontrado_em = models.CharField(max_length=255, choices=encontrado_em_choices, blank=True, null=True, verbose_name="Encontrado Em")
    requisitos = models.TextField(blank=True, null=True, verbose_name="Requisitos")
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Salário")
    localizacao = models.CharField(max_length=255, blank=True, null=True, verbose_name="Localização")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.titulo

class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, verbose_name="Vaga")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    status = models.CharField(max_length=50, choices=status_choices, blank=True, null=True, verbose_name="Status")
    aplicado_em = models.DateTimeField(auto_now_add=True, verbose_name="Aplicado Em")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.usuario} - {self.vaga}"