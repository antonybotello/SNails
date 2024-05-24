from django.shortcuts import render, get_object_or_404
from .models import Usuario

def usuario_list_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'comunidad/usuario.html', {'usuarios': usuarios})

def usuario_detail_view(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'comunidad/usuario-detalle.html', {'usuario': usuario})