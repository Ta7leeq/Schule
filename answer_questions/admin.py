from django.contrib import admin

# Register your models here.



from . models import Exercise,Question

class excerciseAdmin (admin.ModelAdmin):
    
    list_display=("name",)
    
admin.site.register(Exercise, excerciseAdmin)


class questionAdmin (admin.ModelAdmin):
    
    list_display=("exercise","text","correct_answer","pk",)

admin.site.register(Question, questionAdmin)