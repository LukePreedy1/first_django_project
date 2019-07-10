from django.contrib import admin
from .models import Question

admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fileds = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
