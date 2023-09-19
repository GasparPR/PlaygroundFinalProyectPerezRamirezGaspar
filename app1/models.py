from django.db import models

# Create your models here.

class Tecnologia(models.Model):

    titulo = models.CharField(max_length=200, default='default')
    usuario = models.CharField(max_length=200, default='default')
    tecnologia = models.CharField(max_length=15, default='default')
    marca = models.CharField(max_length=40, default='default')
    modelo = models.CharField(max_length=40, default='default')
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.IntegerField() 
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField( default='example@example.com')
    imagenTecnologia = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    comentario = models.ForeignKey(Tecnologia, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)