import pika
import base64
from PIL import Image
import io
import os


RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'image_queue'
PROCESSED_IMAGES_DIR = 'processed_images'

os.makedirs(PROCESSED_IMAGES_DIR, exist_ok=True)

def callback(ch, method, properties, body):
    print("Received message")
    data = body.decode('utf-8')  # Make sure the data is in UTF-8
    image_data = base64.b64decode(data)
    
    image = Image.open(io.BytesIO(image_data))
    grayscale_image = image.convert('L') # Convert to grayscale

    # Sauvegarder l'image traitée
    output_path = os.path.join(PROCESSED_IMAGES_DIR, 'processed_image.png')
    grayscale_image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue=RABBITMQ_QUEUE)

    # Message consumption
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
