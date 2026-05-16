from . import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    cursos = db.relationship('Curso', backref='categoria', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }

class Curso(db.Model):
    __tablename__ = 'cursos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.String(50), nullable=False)
    cupos = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    estudiantes = db.relationship('Estudiante', backref='curso', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'instructor': self.instructor,
            'duracion': self.duracion,
            'cupos': self.cupos,
            'precio': self.precio,
            'categoria_id': self.categoria_id
        }

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'curso_id': self.curso_id
        }
