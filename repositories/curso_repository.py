from database import db
from database.models import Curso

def guardar_curso(curso):
    db.session.add(curso)
    db.session.commit()
    return curso

def obtener_cursos():
    return Curso.query.all()

def obtener_por_id(id):
    return Curso.query.get(id)

def actualizar_curso():
    db.session.commit()

def eliminar_curso(curso):
    db.session.delete(curso)
    db.session.commit()
