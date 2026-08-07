from django.forms import ModelForm ,HiddenInput, Select ,DateInput ,TimeInput
from .models import Produto,Imagens
from datetime import datetime


class ProductForm(ModelForm):
    class Meta:           
        model = Produto
        exclude = ['imagem']

class ImagemForm(ModelForm):
    class Meta:           
        model = Imagens
        fields = ['imagem']