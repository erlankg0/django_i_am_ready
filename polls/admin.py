from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    fieldsets = [
        ('Добавления выбора.', {'fields': ['choice_text']}),
        ('Голос.', {'fields': ['votes']})
    ]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Текс для вопроса.", {'fields': ['question_text']}),
        ('Дата информация.', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# Register your models here.
