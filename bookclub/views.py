from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def book_list(request):
    posts = Post.objects.filter(submitted_date__lte=timezone.now()).order_by('submitted_date')
    return render(request, 'bookclub/book_list.html', {'posts':posts})

def book_detail(request,pk):
    book = get_object_or_404(Post, pk=pk)
    return render(request, 'bookclub/book_detail.html', {'book': book})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.submitted_date = timezone.now()
            post.poster = request.user.username
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'bookclub/post_edit.html', {'form': form})

@login_required
def book_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.submitted_date = timezone.now()
            post.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bookclub/post_edit.html', {'form': form})

@login_required
def book_remove(request, pk):
    book = get_object_or_404(Post, pk=pk)
    book.delete()
    return redirect('book_list')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.username
            comment.save()
            return redirect('book_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bookclub/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('book_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'bookclub/signup.html', {'form': form})
