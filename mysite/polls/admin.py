from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date']})]


# 修改模型的后台管理选项
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
