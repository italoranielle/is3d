

# Create your models here.
from django.db import models
from django.urls import reverse

class Imagens(models.Model):
    descricao = models.CharField(max_length=250,null=True,blank=True)
    img = models.ImageField(upload_to = "produtos/",null=True,blank=True)
    imagem = models.URLField(null = True, blank = True)
    
    def __str__(self):
        return str(self.descricao)


class Material(models.Model):
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return str(self.descricao)


class Categoria(models.Model):
    descricao = models.CharField(max_length=250)

    
    def __str__(self):
        return str(self.descricao)  

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    file3d = models.URLField(null = True, blank = True)
    imagem = models.ManyToManyField(Imagens,null = True, blank = True)
    categoria = models.ManyToManyField(Categoria)
    descricao = models.TextField()
    desconto = models.FloatField(default = 0.0) 
    quantidade_material = models.FloatField() 
    tempo = models.DurationField(null = True, blank = True)
    valor = models.FloatField(null=True ,blank=True) 
    
    def preco(self):
        if self.valor:
            return self.valor
        else:
            return((((self.quantidade_material * 0.17) + ((self.tempo.total_seconds()/60) * 0.018)) *2)* (1-self.desconto) )
    
    def get_absolute_url(self):
        return reverse('produto',args=[self.pk])
    
    def __str__(self):
        return str(self.nome)   
    
    
class Estoque(models.Model):
    material = models.ForeignKey(Material,  models.PROTECT)
    cor = models.CharField(max_length=100)
    quantidade = models.FloatField()
    valor_compra = models.FloatField()

    def __str__(self):
        return str(self.material) 
    