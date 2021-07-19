from django import forms
from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category_type', 'post_title', 'post_content')