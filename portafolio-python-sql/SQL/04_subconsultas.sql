-- Empleados que ganan más que el salario promedio global
SELECT nombre, salario
FROM empleados
WHERE salario > (
    SELECT AVG(salario)
    FROM empleados
);

-- Departamentos cuyo salario promedio es mayor que el salario promedio global
SELECT d.nombre_departamento
FROM departamentos d
JOIN empleados e
  ON d.id_departamento = e.id_departamento
GROUP BY d.nombre_departamento
HAVING AVG(e.salario) > (
    SELECT AVG(salario)
    FROM empleados
);
