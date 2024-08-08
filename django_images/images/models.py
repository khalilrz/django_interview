# images/models.py
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Image(models.Model):
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_path
    
@receiver(post_save, sender=Image)
def handle_image_save(sender, instance, **kwargs):
    """Handle the save signal to compress the image."""
    from .tasks import compress_image  
    compress_image.delay(instance.id)
