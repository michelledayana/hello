from flask import Flask
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

SPACE_ID = os.getenv("CONTENTFUL_SPACE_ID")
ACCESS_TOKEN = os.getenv("CONTENTFUL_ACCESS_TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <h2>🚀 Proyecto desplegado correctamente</h2>
    <p><b>SPACE_ID:</b> {SPACE_ID}</p>
    <p><b>ACCESS_TOKEN:</b> {ACCESS_TOKEN[:10]}... (oculto)</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
