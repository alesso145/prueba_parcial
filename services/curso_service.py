from repositories import curso_repository
from database.models import Curso

def crear_curso(data):
    try:
        nuevo_curso = Curso(
            nombre=data['nombre'],
            instructor=data['instructor'],
            duracion=data['duracion'],
            cupos=data['cupos'],
            precio=data['precio'],
            categoria_id=data['categoria_id']
        )

        curso_repository.guardar_curso(nuevo_curso)

        return {'exito': True, 'curso': nuevo_curso}

    except Exception as e:
        return {'exito': False, 'error': str(e)}

def obtener_cursos():
    cursos = curso_repository.obtener_cursos()
    return [curso.to_dict() for curso in cursos]

def obtener_curso_por_id(id):
    curso = curso_repository.obtener_por_id(id)

    if not curso:
        return {'exito': False, 'error': 'Curso no encontrado'}

    return {'exito': True, 'curso': curso}

def actualizar_curso(id, data):
    try:
        curso = curso_repository.obtener_por_id(id)

        if not curso:
            return {'exito': False, 'error': 'Curso no encontrado'}

        curso.nombre = data['nombre']
        curso.instructor = data['instructor']
        curso.duracion = data['duracion']
        curso.cupos = data['cupos']
        curso.precio = data['precio']
        curso.categoria_id = data['categoria_id']

        curso_repository.actualizar_curso()

        return {'exito': True, 'curso': curso}

    except Exception as e:
        return {'exito': False, 'error': str(e)}

def eliminar_curso(id):
    try:
        curso = curso_repository.obtener_por_id(id)

        if not curso:
            return {'exito': False, 'error': 'Curso no encontrado'}

        curso_repository.eliminar_curso(curso)

        return {'exito': True}

    except Exception as e:
        return {'exito': False, 'error': str(e)}
