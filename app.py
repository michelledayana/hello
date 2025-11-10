from dotenv import load_dotenv
import os

load_dotenv()  # Esto carga las variables de .env

SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

print("SPACE_ID:", SPACE_ID)        # Para probar si se está leyendo
print("ACCESS_TOKEN:", ACCESS_TOKEN)
