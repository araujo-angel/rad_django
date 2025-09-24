from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Bem vindo ao meu blog!")

def eco(request, textoUrl):
    return HttpResponse(f"Você digitou: {textoUrl}")

def info(request):
    informacoes = {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
    }
    return JsonResponse(informacoes)
