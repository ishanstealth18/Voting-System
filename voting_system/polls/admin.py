from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Area"
admin.site.index_title = "Welcome to the Polls Admin Area"


class ChoiceInLine(admin.TabularInline):
    model = Choice



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': ['question_text']
            }
        ),
        (
            'Published Date',
            {
                'classes': ['collapse'],
                'fields': ['pub_date']
            }
        )
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)

