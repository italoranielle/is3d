from django.contrib import admin

# Register your models here.
from . models import Imagens,Material, Produto, Estoque, Categoria
     
admin.site.register(Imagens)

admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(Categoria)