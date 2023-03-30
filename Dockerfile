# Utilisez une image de python
FROM python:3.9

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier Pipfile et Pipfile.lock dans l'espace de travail
COPY Pipfile Pipfile.lock /app/

# Installe les dépendances à partir du fichier Pipfile
RUN apt-get update
RUN pip install pipenv && pipenv install --system

# Copie le code source dans le conteneur
COPY . /app

# Expose le port sur lequel le serveur web écoutera
EXPOSE 8000

CMD ["python3", "manage.py", "runserver","0.0.0.0:8000"]





