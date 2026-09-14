from django.db import models
from django.contrib.auth.models import User
from .constants import estado_civil_choices, escolaridade_choices, nacionalidade_choices, nivel_choices, sexo_choices, telefone_tipo_choices

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    cpf = models.CharField(max_length=14, blank=True, null=True, verbose_name="CPF")
    rg = models.CharField(max_length=12, blank=True, null=True, verbose_name="RG")
    sexo = models.CharField(max_length=10, choices=sexo_choices, blank=True, null=True, verbose_name="Sexo")
    nacionalidade = models.CharField(max_length=50, choices=nacionalidade_choices, blank=True, null=True, verbose_name="Nacionalidade")
    estado_civil = models.CharField(max_length=20, choices=estado_civil_choices, blank=True, null=True, verbose_name="Estado Civil")
    escolaridade = models.CharField(max_length=50, choices=escolaridade_choices, blank=True, null=True, verbose_name="Escolaridade")
    linkedin = models.URLField(max_length=255, blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(max_length=255, blank=True, null=True, verbose_name="GitHub")
    portfolio = models.URLField(max_length=255, blank=True, null=True, verbose_name="Portfólio")
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True, verbose_name="Foto de Perfil")
    curriculum = models.FileField(upload_to='curriculos/', blank=True, null=True, verbose_name="Currículo")
    bio = models.TextField(blank=True, null=True, verbose_name="Biografia")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.user.username

class Habilidade(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nivel = models.CharField(max_length=50, choices=nivel_choices, blank=True, null=True, verbose_name="Nível")

    class Meta:
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.nome

class Idioma(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nivel = models.CharField(max_length=50, choices=nivel_choices, blank=True, null=True, verbose_name="Nível")

    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"

    def __str__(self):
        return self.nome

class ExperienciaProfissional(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_inicio = models.DateField(blank=True, null=True, verbose_name="Data de Início")
    data_fim = models.DateField(blank=True, null=True, verbose_name="Data de Fim")

    class Meta:
        verbose_name = "Experiência Profissional"
        verbose_name_plural = "Experiências Profissionais"

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

class FormacaoAcademica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    instituicao = models.CharField(max_length=100, verbose_name="Instituição")
    curso = models.CharField(max_length=100, verbose_name="Curso")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    data_inicio = models.DateField(blank=True, null=True, verbose_name="Data de Início")
    data_fim = models.DateField(blank=True, null=True, verbose_name="Data de Fim")

    class Meta:
        verbose_name = "Formação Acadêmica"
        verbose_name_plural = "Formações Acadêmicas"

    def __str__(self):
        return f"{self.curso} - {self.instituicao}"

class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    rua = models.CharField(max_length=100, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=100, verbose_name="Estado")
    cep = models.CharField(max_length=20, verbose_name="CEP")

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"

class Telefone(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário")
    tipo = models.CharField(max_length=20, choices=telefone_tipo_choices, blank=True, null=True, verbose_name="Tipo")
    numero = models.CharField(max_length=20, verbose_name="Número")

    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"

    def __str__(self):
        return self.numero