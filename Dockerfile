# Imagen base ligera de Python
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puerto 5000
EXPOSE 5000

# Comando de ejecución (Gunicorn recomendado)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]

