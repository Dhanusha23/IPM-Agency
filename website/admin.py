from django.contrib import admin
from django.utils.html import format_html
from .models import Testimonial, ContactMessage #, WorkSection, InstagramPost, Reel, WebsiteProject


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



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')

    def has_add_permission(self, request):
        return False  # admin cannot add messages manually


'''
#works

class InstagramInline(admin.TabularInline):
    model = InstagramPost
    extra = 1


class ReelInline(admin.TabularInline):
    model = Reel
    extra = 1


class WebsiteInline(admin.TabularInline):
    model = WebsiteProject
    extra = 1



@admin.register(WorkSection)
class WorkSectionAdmin(admin.ModelAdmin):
    list_display = ("name", "section_type", "order", "is_active")

    def get_inlines(self, request, obj=None):
        if obj is None:
            return []

        if obj.section_type == "instagram":
            return [InstagramInline]
        elif obj.section_type == "reels":
            return [ReelInline]
        elif obj.section_type == "website":
            return [WebsiteInline]

        return []
    
    '''