import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from database import init_db
from routes.curso_routes import cursos_bp

load_dotenv()

app = Flask(__name__)

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("===================================")
print("Conectando a PostgreSQL...")
print(f"Base de datos: {DB_NAME}")
print(f"Host: {DB_HOST}")
print("===================================")

init_db(app)

app.register_blueprint(cursos_bp)

@app.route('/')
def home():
    return jsonify({
        "mensaje": "Sistema de Cursos funcionando correctamente",
        "estado": "activo"
    })

@app.route('/health')
def health():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(debug=True)
