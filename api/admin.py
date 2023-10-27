from django.contrib import admin
from api.models import profile, post, todaymonologue

# Register your models here.

@admin.register(profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_username', 'bio')
    list_filter = ('user',)
    search_fields = ('user__username', 'id_username')

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'caption')

@admin.register(todaymonologue)
class TodayMonologueAdmin(admin.ModelAdmin):
    list_display = ('theme', 'title', 'dialogue')
    search_fields = ('theme', 'title')
