from flask import Flask, jsonify
from contentful_client import get_content
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
PORT = int(os.getenv("PORT", 5000))

@app.route('/')
def index():
    content = get_content()
    return jsonify(content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True)
