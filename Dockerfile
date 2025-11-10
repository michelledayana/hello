# Imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de requerimientos
COPY requirements.txt ./requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al contenedor
COPY . .

# Exponer el puerto (ajústalo si tu app usa otro)
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]

