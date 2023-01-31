from django.contrib import admin

from .models import Parallax


class ParallaxAdmin(admin.ModelAdmin):
    list_display = ("id", "photo", "name")


admin.site.register(Parallax, ParallaxAdmin)
