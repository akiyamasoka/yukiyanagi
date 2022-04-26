from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .models import Post, Servey, Servey_re
from .forms import PostForm, Servey_reForm

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
        form = Servey_reForm(request.POST)
        if form.is_valid():
            servey = form.save(commit=False)
            servey.institution = post.title
            servey.published_date = timezone.now()
            servey.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Servey_reForm()
    return render(request, 'blog/servey_form.html', {'form': form})
    
def post_place(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_place.html', {'post': post})
    
def post_place_re(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_place_re.html', {'post': post})
    
def servey_form_ex(request):
    if request.method == "POST":
        form = Servey_reForm(request.POST)
        if form.is_valid():
            servey = form.save(commit=False)
            servey.institution = "none"
            servey.published_date = timezone.now()
            servey.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = Servey_ReForm()
    return render(request, 'blog/servey_form_ex.html', {'form': form})
    
    
    