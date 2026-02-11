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


class Work(models.Model):
    CATEGORY_CHOICES = [
        ('instagram', 'Instagram'),
        ('reels', 'Reels'),
        ('website', 'Website'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    image = models.ImageField(upload_to='works/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


