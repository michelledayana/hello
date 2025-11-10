import os
import contentful

# 🔐 Variables de entorno
SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

# 🚀 Cliente de Contentful
client = contentful.Client(SPACE_ID, ACCESS_TOKEN)

# 🔍 Función para obtener los datos desde Contentful
def get_content():
    try:
        entries = client.entries()  # 👈 Aquí se consume la API de Contentful
        data = []

        for entry in entries:
            data.append({
                "id": entry.sys.get("id"),
                "title": getattr(entry, "title", "No title"),
                "description": getattr(entry, "description", "No description")
            })

        return data

    except Exception as e:
        return {"error": str(e)}

