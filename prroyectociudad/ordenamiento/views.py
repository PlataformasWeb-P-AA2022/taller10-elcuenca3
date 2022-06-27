from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

from ordenamiento.models import *
from ordenamiento.forms import BarrioForm, ParroquiaForm
#Generar una vista que liste las parroquias y sus barrios
def index(request):
    parroquias = Parroquia.objects.all()
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)
#Generar una vista que liste los barrios
def barrios(request):
    barrios = Barrio.objects.all()
    informacion_template = {'barrios': barrios}
    return render(request, 'barrios.html', informacion_template)
#Generar un formulario que cree una parroquia
def crear_parroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


#Generar un formulario que edite un barrio
def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(barrios)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

# Generar un formulario que edite una parroquia
def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)
#Generar un formulario que cree un barrio de una parroquia1
def crear_barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(barrios)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)
