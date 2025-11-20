-- Salario promedio por departamento
SELECT d.nombre_departamento,
       AVG(e.salario) AS salario_promedio,
       COUNT(*) AS n_empleados
FROM empleados e
JOIN departamentos d
  ON e.id_departamento = d.id_departamento
GROUP BY d.nombre_departamento
ORDER BY salario_promedio DESC;

-- Distribución por sexo
SELECT sexo,
       COUNT(*) AS n_empleados,
       AVG(salario) AS salario_promedio
FROM empleados
GROUP BY sexo;
