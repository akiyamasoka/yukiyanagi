from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .models import Post, Servey
from .forms import PostForm, ServeyForm

def main(request):
	return render(request, 'blog/main.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=',1').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
def mid_post_list(request, pk):
	corrent = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=corrent.text).order_by('published_date')
	return render(request, 'blog/mid_post_list.html', {'posts': posts})
	
def last_post_list(request, pk):
	corrent = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=corrent.text).order_by('published_date')
	return render(request, 'blog/last_post_list.html', {'posts': posts})
	
def post_result(request, pk):
	corrent = get_object_or_404(Post, pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now(), tag__contains=corrent.text).order_by('published_date')
	return render(request, 'blog/post_result.html', {'posts': posts})
	
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
    
    
    
def servey_form(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ServeyForm(request.POST)
        if form.is_valid():
            servey = form.save(commit=False)
            servey.link = post.link
            servey.tag = post.title
            servey.published_date = timezone.now()
            servey.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ServeyForm()
    return render(request, 'blog/servey_form.html', {'form': form})
    
    
    
    