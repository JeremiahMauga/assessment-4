from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Post
from .forms import CategoryForm, PostForm

# Helper Methods!

def get_category(category_id):
    return Category.objects.get(id=category_id)

def get_post(post_id):
    return Post.objects.get(id=post_id)

# Category Views!

def category_list(request):
    category = Category.objects.all()
    return render(request, 'category/category_list.html', {'category': category})

def category_detail(request, category_id):
    category = get_category(category_id)
    return render(request, 'category/category_detail.html', {'category': category})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form, 'type_of_request': 'New'})


def edit_category(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form, 'type_of_request': 'Edit'})


def delete_category(request, category_id):
    if request.method == "POST":
        category = get_category(category_id)
        category.delete()
    return redirect('category_list')

# Post Views!

def post_list(request, category_id):
    category = get_category(category_id)
    post = category.post.all()
    context = {'category': category, 'post': post}
    return render(request, 'category/post_list.html', context)

def post_detail(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    return render(request, 'category/post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = get_category(category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('post_detail', category_id=post.category.id, post_id=post.id)
    else:
        form = PostForm()
    return render(request, 'category/post_form.html', {'form': form, 'type_of_request': 'New'})

def edit_post(request, category_id, post_id):
    category_id = get_category(category_id)
    post = get_post(post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id, category_id=category_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'category/post_form.html', {'form': form, 'type_of_request': 'Edit'})


def delete_post(request, category_id, post_id):
    if request.method == "POST":
        post = get_post(post_id)
        post.delete()
    return redirect('post_list', category_id=category_id)