import os
import contentful
from dotenv import load_dotenv

load_dotenv()

SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

# Inicializamos el cliente
client = contentful.Client(SPACE_ID, ACCESS_TOKEN)

def get_content():
    entries = client.entries({'content_type': 'helloWorldContentful'})
    content_list = []
    for entry in entries:
        content_list.append({
            'title': getattr(entry, 'title', ''),
            'description': getattr(entry, 'description', '')
        })
    return content_list
