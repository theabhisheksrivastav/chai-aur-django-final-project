from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect('all_posts')
    return render(request, 'create_post.html', {'form': form})

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author = request.user)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect('posts')
    return render(request, 'create_post.html', {'form': form})



@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author = request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('all_posts')
    return render(request, 'delete_post.html', {'post': post})



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_posts')
    return render(request, 'registration/register.html', {'form': form})