from tkinter import CASCADE
from turtle import title
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title



class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]} "