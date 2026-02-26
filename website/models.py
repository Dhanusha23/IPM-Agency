from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise ValidationError("Image size should not exceed 2MB")


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    position = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

'''

#works page

# PARENT MODEL (just to group everything)

class WorkSection(models.Model):

    SECTION_TYPES = (
        ('instagram', 'Instagram'),
        ('reels', 'Reels'),
        ('website', 'Website'),
    )

    name = models.CharField(max_length=100)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.section_type})"
    

#INSTAGRAM POSTS (only image + caption)
class InstagramPost(models.Model):

    section = models.ForeignKey(
        WorkSection,
        on_delete=models.CASCADE,
        related_name="instagram_posts",
        limit_choices_to={'section_type': 'instagram'}
    )

    image = models.ImageField(upload_to="works/instagram/")
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Instagram - {self.caption or 'Post'}"

# REELS (video + caption)
class Reel(models.Model):

    section = models.ForeignKey(
        WorkSection,
        on_delete=models.CASCADE,
        related_name="reels",
        limit_choices_to={'section_type': 'reels'}
    )

    video = models.FileField(upload_to="works/reels/")
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Reel - {self.caption or 'Video'}"


# WEBSITES (image preview + link)
class WebsiteProject(models.Model):

    section = models.ForeignKey(
        WorkSection,
        on_delete=models.CASCADE,
        related_name="websites",
        limit_choices_to={'section_type': 'website'}
    )

    title = models.CharField(max_length=200)
    preview_image = models.ImageField(upload_to="works/websites/")
    website_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
'''