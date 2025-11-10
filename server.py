from flask import Flask, jsonify
from contentful_client import get_content
import os

app = Flask(__name__)

@app.route("/")
def home():
    content = get_content()
    return jsonify({
        "message": "🚀 Proyecto desplegado correctamente",
        "contentful_data": content
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # 👈 Asegura puerto 5000
    app.run(host="0.0.0.0", port=port)
