INSERT INTO categorias (nombre, descripcion) VALUES
('Informática', 'Cursos relacionados con tecnología y programación'),
('Arte', 'Cursos de dibujo y creatividad'),
('Idiomas', 'Cursos de aprendizaje de idiomas');

INSERT INTO cursos (nombre, instructor, duracion, cupos, precio, categoria_id) VALUES
('Curso de Python', 'Carlos Pérez', '3 meses', 25, 120.50, 1),
('Curso de Dibujo Digital', 'María López', '2 meses', 20, 90.00, 2),
('Curso de Inglés Básico', 'John Smith', '4 meses', 30, 150.00, 3);

INSERT INTO estudiantes (nombre, email, telefono, curso_id) VALUES
('Alejandro Ruiz', 'alejandro@gmail.com', '0991111111', 1),
('Camila Torres', 'camila@gmail.com', '0982222222', 2),
('Mateo Sánchez', 'mateo@gmail.com', '0973333333', 3);
