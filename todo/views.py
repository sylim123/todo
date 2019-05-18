from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    now2 = timezone.now()
    form = PostForm()
    posts = Post.objects.filter(checked=False).order_by('-created_data')
    checkedPosts = Post.objects.filter(checked=True).order_by('-checked_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.checked = False
            post.created_data = timezone.now()
            post.save()
    return render(request, 'todo/post_list.html', {'posts': posts, 'now2': now2, 'form': form, 'checkedPosts': checkedPosts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'todo/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_data = timezone.now()
            post.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('/')
    else:
        form = PostForm(instance=post)
    return render(request, 'todo/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')

def post_check(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.checked = True
    post.checked_date = timezone.now()
    post.save()
    return redirect('/')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.checked = False
            post.created_data = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'todo/post_edit.html', {'form': form})

def post_priority_up(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.priority > 1:
        post.priority = post.priority - 1
    post.save()
    return redirect('/')

def post_priority_down(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.priority < 6:
        post.priority = post.priority + 1
    post.save()
    return redirect('/')
