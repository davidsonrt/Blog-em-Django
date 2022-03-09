from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comentari
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import PostSerializer, ComentariSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ComentariViewSet(viewsets.ModelViewSet):
    queryset = Comentari.objects.all()
    serializer_class = ComentariSerializer


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/logout/')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

# Create your views here.

@login_required(login_url='/login/')
def register_post(request):
    post_id = request.GET.get('id')
    if post_id:
        post = Post.objects.get(id=post_id)
        if post.user == request.user:
            return render(request, 'register-post.html', {'post':post})
    return render(request, 'register-post.html')



@login_required(login_url='/login/')
def set_comment(request, id):
    post = Post.objects.get(active=True, id=id)
    comentari = Comentari.objects.filter(post=id).exists()
    if comentari:
        comentari = Comentari.objects.filter(active=True, post=post)
        context = {'post':post, 'comentari':comentari}
    else:
        context = {'post':post}
    return render(request, 'comentar.html', context)
    
@login_required(login_url='/login/')
def comentar(request, id):
    text = request.POST.get('text')
    user = request.user
    post = Post.objects.get(active=True, id=id)
    comentari = Comentari.objects.create(text=text, user=user, post=post)
    
    url = '/post/detail/{}/'.format(id)
    return redirect(url)


@login_required(login_url='/login/')
def set_post(request):
    title = request.POST.get('title')
    subtitle = request.POST.get('subtitle')
    text = request.POST.get('text')
    photo = request.FILES.get('file')
    post_id = request.POST.get('post-id')
    user = request.user
    if post_id:
        post = Post.objects.get(id=post_id)
        if user == post.user:
            post.title = title
            post.subtitle = subtitle
            post.text = text
            if photo:
                post.photo = photo
            post.save()
    else:
        post = Post.objects.create(title=title, subtitle=subtitle, text=text, photo=photo, user=user)

    url = '/post/detail/{}/'.format(post.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
    return redirect('/')

@login_required(login_url='/login/')
def list_all_post(request):
    post = Post.objects.filter(active=True)
    return render(request, 'list.html', {'post':post})

@login_required(login_url='/login/')
def list_user_post(request):
    post = Post.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'post':post})
    
@login_required(login_url='/login/')
def post_detail(request, id):
    post = Post.objects.get(active=True, id=id)
    comentari = Comentari.objects.filter(post=id).exists()
    if comentari:
        comentari = Comentari.objects.filter(active=True, post=post)
        context = {'post':post, 'comentari':comentari}
    else:
        context = {'post':post}
    return render(request, 'post.html', context)


def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e senha inválidos. Por favor tentar novamente.')
        return redirect('/login/')
