from django.contrib import admin

# Register your models here.
from . models import gaps

class gapsAdmin (admin.ModelAdmin):
    
    list_display=("pk","sentence","gapWord", "category")
    
admin.site.register(gaps, gapsAdmin)
