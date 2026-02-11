from django.contrib import admin
from django.utils.html import format_html
from .models import Testimonial, Work, ContactMessage


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'stars', 'photo_preview')
    list_filter = ('stars',)
    search_fields = ('name', 'position')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="60" style="border-radius:50%;" />',
                obj.photo.url
            )
        return "No Photo"

    photo_preview.short_description = "Photo"


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_preview', 'uploaded_at')
    list_filter = ('category',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')

    def has_add_permission(self, request):
        return False  # admin cannot add messages manually
