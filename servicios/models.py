from django.db import models

from comunidad.models import Usuario

# Create your models here.
class Servicio(models.Model):
    nombre= models.CharField(max_length=45,verbose_name="Nombre")
    descripcion= models.CharField(max_length=200,verbose_name="Descripción")
    estado=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    fecha=models.DateField()
    cliente= models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
    def __str__(self):
        return "Compra # "+str(self.id)
    

class DetalleCompra(models.Model):
    compra= models.ForeignKey(Compra,on_delete=models.CASCADE)
    servicio= models.ForeignKey(Servicio,on_delete=models.CASCADE)
    precio= models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return "Detalle de compra # "+str(self.compra.id) + " - "+self.servicio.nombre