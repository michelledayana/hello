import os
from contentful import Client
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

# Crear el cliente de Contentful
client = Client(SPACE_ID, ACCESS_TOKEN)

def get_entries():
    """Obtiene todas las entradas publicadas desde Contentful."""
    entries = client.entries()
    return [entry.fields() for entry in entries]
