from django.http import HttpResponse
from django.shortcuts import render
from empresa.models import Vaga

def index(request):
    if request.method == 'GET':
        template_name = 'empresa/index.html'
        vagas = Vaga.objects.all()
        return render(request, template_name, context={'vagas': vagas})
    return HttpResponse('Page not Found')
