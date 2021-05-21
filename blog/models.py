from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=250)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    author = models.ManyToManyField(Author)
    num_of_comments = models.IntegerField()
    numbof_pingbacks = models.IntegerField()

    def __str__(self):
        return self.headline

"""
url https://djangodoc.ru/3.2/topics/db/queries/в
"""
# Create your models here.
