# Base image
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY app/ ./app

# Installer les dépendances
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 8000

# Commande pour démarrer l'app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
