-- Empleados que ganan por encima del salario promedio global
SELECT nombre, salario
FROM empleados
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- Top 10 salarios
SELECT nombre, salario
FROM empleados
ORDER BY salario DESC
LIMIT 10;
