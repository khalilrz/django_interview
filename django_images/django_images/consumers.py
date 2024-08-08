import json
from channels.generic.websocket import WebsocketConsumer
import base64
import os
from django.conf import settings
from .models import Image
from django.utils import timezone

class ImageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        image_data = data['imageB64'].split(',')[1]
        image_binary = base64.b64decode(image_data)
        image_path = os.path.join(settings.MEDIA_ROOT, 'images', f"{timezone.now().strftime('%Y%m%d%H%M%S')}.jpg")

        # Sauvegarde de l'image
        with open(image_path, 'wb') as f:
            f.write(image_binary)

        # Création de l'entrée dans la base de données
        image = Image.objects.create(image_path=image_path)
        self.send(text_data=json.dumps({'message': 'Image received and saved.'}))
