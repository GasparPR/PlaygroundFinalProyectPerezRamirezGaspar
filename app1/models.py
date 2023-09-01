from django.db import models

# Create your models here.

class Tecnologia(models.Model):
    tecnologiaSeleccion = (
    ('teclado','Teclado'),
    ('monitor', 'Monitor'),
    ('mouse','Mouse'),
    ('cpu','Cpu'),
    ('auriculares','Auriculares'),
    ('parlante','Parlantes'),
    ('otro', 'Otro'),
    )
    titulo = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    tecnologia = models.CharField(max_length=15, default='cpu')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
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