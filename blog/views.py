from django.shortcuts import render
import math
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from . models import Post , Categoria
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


def index(request):
    return render(request,'blog/index.html')


def postList(request,pg):
    post = Post.objects.all()
    Categorias = Categoria.objects.all()
    npages = math.ceil(post.count() / 10 )
    pages = []
    for i in range(npages):
        pages = pages.append(i)
    data = {'object_list': post[pg*10:(pg*10)+10], 'recente': post[:2], 'categorias': Categorias, 'pages':pages} 
    return render(request,'blog/post_list.html' ,data)
 
def postSearch(request):
    try:
        search = request.GET.get('q')
        posts = Post.objects.filter(postagem__icontains = search)
    except:
        search = ''
    try: 
        cate = request.GET.get('cate')
        posts = Post.objects.filter(categoria__Nome__icontains = cate)
    except:
        cate = ''  
        
    pg = 0
    post = Post.objects.all()[:2]
    Categorias = Categoria.objects.all()
    
    
    npages = math.ceil(posts.count() / 10 )
    pages = []
    for i in range(npages):
        pages = pages.append(i)
        
    data = {'object_list': posts[pg*10:(pg*10)+10], 'recente': post, 'categorias': Categorias, 'pages':pages} 
    return render(request,'blog/post_list.html' ,data)


   
    
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 
    
class PostCreate(CreateView,PermissionRequiredMixin):
    permission_required = 'add.change_Post'
    model = Post
    #form_class = CompForm
    template_name = 'blog/post_create.html'  
    fields = ['imagem','titulo','categoria','postagem','autor','data','tags']

class PostEdit(UpdateView,PermissionRequiredMixin):
    permission_required = 'blog.change_Post'
    model = Post
    #form_class = CompForm
    template_name = 'blog/post_edit.html'  
    fields = ['imagem','titulo','categoria','postagem','autor','data','tags']