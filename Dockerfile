# Użyj obrazu bazowego Pythona (wersja 3.10 w tym przypadku)
FROM python:3.13-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiowanie jarki z hosta do kontenera
COPY Welcome.py /app/Welcome.py

# Wystawienie portu 8080
EXPOSE 8080

# Uruchom aplikację
CMD ["python", "Welcome.py"]