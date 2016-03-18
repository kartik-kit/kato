from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=100)
    author_bio=models.TextField()
    author_email=models.EmailField(unique=True)
    def __str__(self):
        return self.author_name

class Categories(models.Model):
    cat_name=models.CharField('Category name',max_length=100)
    cat_description=models.CharField('Category Description',max_length=200)
    def __str__(self):
        return self.cat_name
    class Meta():
        verbose_name_plural='Categories'

class Tags(models.Model):
    tag_name=models.CharField(max_length=100)
    tag_description=models.CharField(max_length=200)
    def __str__(self):
        return self.tag_name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    categories=models.ManyToManyField(Categories)
    tags=models.ManyToManyField(Tags)
    author=models.ForeignKey(Author)
    date=models.DateTimeField(auto_now_add=True,auto_now=False)
    def __str__(self):
        return self.title