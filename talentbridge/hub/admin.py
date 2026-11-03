from django.contrib import admin
from .models import Job, Post, Lead


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "active", "created")
    list_filter = ("active",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("kind", "name", "email", "company", "service", "budget", "created")
    list_filter = ("kind",)
