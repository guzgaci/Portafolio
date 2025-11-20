-- Empleados con el nombre de su departamento
SELECT e.nombre,
       d.nombre_departamento,
       e.salario
FROM empleados e
JOIN departamentos d
  ON e.id_departamento = d.id_departamento;

-- Empleados y cursos que han tomado
SELECT e.nombre AS empleado,
       c.nombre_curso,
       c.tema
FROM empleados e
JOIN empleado_curso ec
  ON e.id_empleado = ec.id_empleado
JOIN cursos c
  ON ec.id_curso = c.id_curso;
