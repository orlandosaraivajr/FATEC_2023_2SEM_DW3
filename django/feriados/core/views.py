from django.shortcuts import render
from .models import FeriadoModel
from datetime import date


def feriado(request):
    hoje = date.today()
    feriados = FeriadoModel.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(feriados) > 0:
        contexto = {'feriado':True, 'nome':feriados[0].nome}
    else:
        contexto = {'feriado':False}
    return render(request, 'feriado.html',contexto)
