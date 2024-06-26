from django.shortcuts import render, redirect

from servicios.forms import ServicioEditarForm, ServicioForm
from servicios.models import Servicio

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from PIL import Image
# Create your views here.
def servicio_list_view(request,id=None):
    titulo= "Servicios"
    
    
    if request.method == 'POST' and id:
        servicio= Servicio.objects.get(id=id)
        form = ServicioEditarForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            servicio= form.save()
            messages.success(request, f'¡El Servicio se editó de forma exitosa!')
            return redirect("servicios-listar")
        else:
            form= ServicioEditarForm(request.POST,request.FILES,instance=servicio)
            messages.error(request, f'¡Error al editar servicio!')
           
    elif request.method == 'POST':
        form= ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡El Servicio se agregó de forma exitosa!')
            return redirect('servicios-listar')
        else:
            form= ServicioForm(request.POST,request.FILES)
            messages.error(request, f'¡Error al agregar servicio!')
    else:
        if(id):
            servicio= Servicio.objects.get(id=id)
            form= ServicioEditarForm(instance=servicio)
        else:
            form= ServicioForm()
    context={
        "titulo":titulo,
        "form":form,  
    }
    return render(request, 'admin/servicios/servicios.html', context)


def servicio_delete_view(request,id):
    servicio= Servicio.objects.filter(id=id)
    servicio.update(estado=False)
    return redirect('servicios-listar')