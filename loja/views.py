from django.shortcuts import render ,  redirect
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import Produto,Categoria
from .forms import ProductForm,ImagemForm
import math
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
# Create your views here.
def index(request):
    return redirect('/loja')
    #return render(request,'loja/produto.html')


def loja(request):
    pg = int(request.GET.get('page','0'))
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    try:
        search = request.GET.get('search')
        produtos = Produto.objects.filter(Q(nome__icontains = search) | Q(descricao__icontains =search) | Q(categoria__descricao__icontains =search ))
    except:
        search = ''
    try: 
        cate = request.GET.get('cate')
        produtos = produtos.filter(categoria__pk__in = cate)
    except:
        cate = ''  

    npages = math.ceil(produtos.count() / 10 )
    pages = []
    for i in range(npages):
        pages = pages.append(i)
    data = {'produtos': produtos[pg*10:(pg*10)+10],  'pages':pages, 'categorias':categorias} 
    return render(request,'loja/loja.html' ,data)

class ProdutoDetail(DetailView):
    model = Produto
    template_name = 'loja/produto.html'


class ProdutoNovo(LoginRequiredMixin,CreateView , SuccessMessageMixin):
    form_class = ProductForm
    template_name = 'loja/form.html' 
    success_message = 'Produto criado !'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()  
        return super().form_valid(form)

class ProdutoEdit(LoginRequiredMixin,UpdateView , SuccessMessageMixin):
    model = Produto
    form_class = ProductForm
    template_name = 'loja/form.html' 
    success_message = 'Produto criado !'


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()  
        return super().form_valid(form)   


def addImage(request,pk):
    
    if request.method == "POST":
        produto = Produto.objects.get(pk=pk)
        form = ImagemForm(request.POST)
        post = form.save()
        produto.imagem.add(post)
        return redirect(produto)
    
    if request.method == "GET":    
        form = ImagemForm()
        context = { 'form': form}
        return render(request, 'loja/form.html', context)
        

        