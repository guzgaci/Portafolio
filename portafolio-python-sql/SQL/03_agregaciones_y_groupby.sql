-- Salario promedio por departamento
SELECT d.nombre_departamento,
       AVG(e.salario) AS salario_promedio,
       COUNT(*) AS n_empleados
FROM empleados e
JOIN departamentos d
  ON e.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento;

-- Cantidad de cursos por tema
SELECT c.tema,
       COUNT(*) AS n_cursos_impartidos
FROM cursos c
JOIN empleado_curso ec
  ON c.id_curso = ec.id_curso
GROUP BY c.tema;
