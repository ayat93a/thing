from django.contrib import admin


from .models import Thing
# Register your models here.
admin.site.register(Thing)

# @admin.register
# class AdminThing(admin.ModelAdmin):
#     list_display = ['name' , 'rating' , 'raiting' , 'reviewer']
