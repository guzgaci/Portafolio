-- 05_vista_salarios_departamento.sql
CREATE VIEW vista_salarios_departamento AS
SELECT 
    d.nombre_departamento,
    AVG(e.salario) AS salario_promedio,
    MIN(e.salario) AS salario_min,
    MAX(e.salario) AS salario_max,
    COUNT(*) AS total_empleados
FROM empleados e
JOIN departamentos d
  ON e.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento;
