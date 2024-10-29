from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'photo', 'slug')
    fields = ('title', 'photo')

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'photo', 'slug', 'category')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Фото'

class ReviewsAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'review', 'created_at')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Reviews, ReviewsAdmin)
