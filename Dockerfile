# Pobierz obraz bazowy Pythona
FROM python:3.12-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki aplikacji
COPY app/ /app/

# Instaluj zależności
RUN pip install -r requirements.txt

# Wystawienie portu 8080
EXPOSE 8080

# Uruchom aplikację
CMD ["python", "app.py"]