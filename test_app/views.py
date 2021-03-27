from django.shortcuts import render, redirect
from .models import Category, Product_Name, Comment
from .forms import ProductForm, ProdCommentForm, CommentForm
from django.contrib import auth


def get_all_posts(request):
    categories = Category.objects.all()
    product = Product_Name.objects.all()
    data = {
        'categories': categories,
        'products': product,
    }
    return render(request, 'index.html', context=data)


def get_post(request, id):
    product = Product_Name.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(data=request.POST, initial={'product': product})
        if form.is_valid():
            form.save()
    comments = Comment.objects.filter(product_id=id)
    form = CommentForm()
    data = {
        'product': product,
        'comments': comments,
        'form': form,
        'username': auth.get_user(request).username
    }
    return render(request, 'post.html', context=data)


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    form = ProductForm()
    data = {
        'form': form,
        'username': auth.get_user(request).username
    }
    return render(request, 'add.html', context=data)


def add_product_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    form = ProdCommentForm()
    data = {
        'form': form,
        'username': auth.get_user(request).username
    }
    return render(request, 'product.html', context=data)