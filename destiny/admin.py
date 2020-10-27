from django.contrib import admin
from .models import Category, Roulette,Content

class ContentInline(admin.StackedInline):
    model = Content
    extra = 2
    max_num = 10


class RouletteAdmin(admin.ModelAdmin):
    inlines = [ContentInline]


admin.site.register(Roulette, RouletteAdmin)
admin.site.register(Category)
admin.site.register(Content)

# Register your models here.
