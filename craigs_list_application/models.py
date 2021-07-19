from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"

class Post(models.Model):
    category_type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post')
    post_title = models.CharField(max_length=100)
    post_content = models.CharField(max_length=500)
    
    def __str__(self):
        return f"id={self.id}, Title: {self.category_type}, Body: {self.post_content}"
