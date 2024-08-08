from celery import shared_task
from PIL import Image as PILImage
import io
import base64
from django.core.files.base import ContentFile


@shared_task
def compress_image(image_id):
    from .models import Image
    try:
        image = Image.objects.get(id=image_id)
        with open(image.image_path, 'rb') as f:
            img_data = f.read()
        
        # Process the image with Pillow
        img = PILImage.open(io.BytesIO(img_data))
        img = img.convert('L')  # Convertir en niveaux de gris
        img.save(image.image_path)

        # Re-encode the image to base64 and publish it to Redis or RabbitMQ
        with open(image.image_path, 'rb') as f:
            img_data = f.read()
        encoded_image = base64.b64encode(img_data).decode('utf-8')
        # Publish the encoded image
    except Exception as e:
        print(f"Erreur lors de la compression de l'image: {e}")
