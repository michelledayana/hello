from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from contentful_client import get_entries

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    try:
        data = get_entries()
        return jsonify({
            "message": "🚀 Proyecto desplegado correctamente",
            "SPACE_ID": os.getenv("CONTENTFUL_SPACE_ID"),
            "entries": data
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "message": "❌ Error al consumir la API de Contentful"
        }), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
