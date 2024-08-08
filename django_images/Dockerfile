# Utilisez l'image Python officielle comme image de base
FROM python:3.10-slim

# Définir les variables d'environnement pour éviter l'écriture de fichiers .pyc et pour bufferiser stdout et stderr
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update \
    && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . /app/

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port sur lequel l'application sera accessible
EXPOSE 8000

# Définir la commande pour exécuter l'application
CMD ["gunicorn", "django_images.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
