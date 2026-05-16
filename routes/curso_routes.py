from flask import Blueprint, jsonify, request
from services import curso_service

cursos_bp = Blueprint('cursos', __name__)

@cursos_bp.route('/cursos', methods=['POST'])
def crear_curso():
    data = request.get_json()
    resultado = curso_service.crear_curso(data)

    if resultado['exito']:
        return jsonify({
            "mensaje": "Curso creado correctamente",
            "curso": resultado['curso'].to_dict()
        }), 201
    else:
        return jsonify({
            "mensaje": "Error al crear el curso",
            "error": resultado['error']
        }), 500

@cursos_bp.route('/cursos', methods=['GET'])
def obtener_cursos():
    resultado = curso_service.obtener_cursos()
    return jsonify({"cursos": resultado}), 200

@cursos_bp.route('/cursos/<int:id>', methods=['GET'])
def obtener_curso(id):
    resultado = curso_service.obtener_curso_por_id(id)

    if resultado['exito']:
        return jsonify({"curso": resultado['curso'].to_dict()}), 200
    else:
        return jsonify({
            "mensaje": "Curso no encontrado",
            "error": resultado['error']
        }), 404

@cursos_bp.route('/cursos/<int:id>', methods=['PUT'])
def actualizar_curso(id):
    data = request.get_json()
    resultado = curso_service.actualizar_curso(id, data)

    if resultado['exito']:
        return jsonify({
            "mensaje": "Curso actualizado correctamente",
            "curso": resultado['curso'].to_dict()
        }), 200
    else:
        return jsonify({
            "mensaje": "Error al actualizar el curso",
            "error": resultado['error']
        }), 404

@cursos_bp.route('/cursos/<int:id>', methods=['DELETE'])
def eliminar_curso(id):
    resultado = curso_service.eliminar_curso(id)

    if resultado['exito']:
        return jsonify({"mensaje": "Curso eliminado correctamente"}), 200
    else:
        return jsonify({
            "mensaje": "Error al eliminar el curso",
            "error": resultado['error']
        }), 404
