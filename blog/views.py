from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=',1').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def mid_post_list(request, pk):
	corrent = get_object_or_404(Post, pk=pk)
	destinations = corrent.destination
	posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=destinations).order_by('published_date')
	return render(request, 'blog/mid_post_list.html', {'posts': posts}, {'corrent': corrent})
	
def last_post_list(request, pk):
	corrent = get_object_or_404(Post, pk=pk)
	destinations = corrent.destination
	posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=destinations).order_by('published_date')
	return render(request, 'blog/last_post_list.html', {'posts': posts}, {'corrent': corrent})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})
	
	
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})