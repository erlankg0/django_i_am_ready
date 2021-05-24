from django.contrib import admin
from .models import Entry, Blog, Author, Dog, Store, Publisher, Book, Person
from .models import OpinionPoll, Response

admin.site.register(OpinionPoll)
admin.site.register(Response)
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Dog)
admin.site.register(Store)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Person)
