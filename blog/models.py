from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    Nome = models.CharField(max_length=250)

    def __str__(self):
        return str(self.Nome)

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    imagem = models.URLField(null = True, blank = True)
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, models.PROTECT)
    postagem = RichTextField()
    autor = models.ForeignKey(User,on_delete= models.PROTECT)
    data = models.DateTimeField(default = timezone.now)
    tags = models.CharField(max_length=250, null =True, blank = True)
    
    
    
    def get_absolute_url(self):
        return reverse('postDetail',args=[self.slug])
    
    def __str__(self):
        return str(self.titulo)      
    
@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()