from django.contrib import admin

# Register your models here.

from . models import Exercise,Question, Thema, Fach,Exercise_Type

class exerciseTypeAdmin (admin.ModelAdmin):
    
    list_display=("Name",)
admin.site.register(Exercise_Type, exerciseTypeAdmin)


class fachAdmin (admin.ModelAdmin):
    
    list_display=("Name","pk")
    
admin.site.register(Fach, fachAdmin)

class themaAdmin (admin.ModelAdmin):
    
    list_display=("Name",)
    
admin.site.register(Thema, themaAdmin)

class excerciseAdmin (admin.ModelAdmin):
    
    list_display=("name","pk")
    
admin.site.register(Exercise, excerciseAdmin)


class questionAdmin (admin.ModelAdmin):
    
    list_display=("exercise","text","correct_answer","question_number",)

admin.site.register(Question, questionAdmin)