from django.db import models
from django.db.models.functions import Coalesce


class JoeBookManager(models.Manager):
    def get_queryset(self):
        return super(JoeBookManager, self).get_queryset().filter(author='Joe')


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
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

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    objects = models.Manager()
    joe_books = JoeBookManager()

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    people = models.Manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PollManager(models.Manager):
    def with_counts(self):
        return self.annotate(
            num_response=Coalesce(models.Count("response"), 0)
        )


class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    objects = PollManager()

    def __str__(self):
        return self.question


class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
