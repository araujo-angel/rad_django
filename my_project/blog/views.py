from datetime import date
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

def home(request):
    return render(request, "blog/home.html") #blog/ indica que esta na pasta blog de template, como no slide

def about(request):
    return render(request, "blog/about.html")

def contato(request, telefone):
    return render(request, "blog/contato.html", {"telefone": telefone})

def nome(request):
    contexto = {
        "usuario": "Alex",
        "numero": 10,
        "data": date.today(),
    }
    return render(request, "blog/nome.html", contexto)

def condicionais(request):
    contexto = {
        "is_logged_in": True,
        "idade": 20,
        "role": "admin",
    }
    return render(request, "blog/condicionais.html", contexto) 

def loops(request):
    produtos = [
        {"nome": "Notebook", "preco": 3500},
        {"nome": "Mouse", "preco": 80},
        {"nome": "Teclado", "preco": 150},
        {"nome": "Monitor", "preco": 1200},
    ]
    return render(request, "blog/loops.html", {"produtos": produtos})