-- 1. Mostrar todos los empleados
SELECT * FROM empleados;

-- 2. Empleados de TI con salario > 25000
SELECT nombre, salario
FROM empleados
WHERE departamento = 'TI'
  AND salario > 25000
ORDER BY salario DESC;

-- 3. Empleados nacidos después de 1995-01-01
SELECT nombre, fecha_nacimiento
FROM empleados
WHERE fecha_nacimiento > '1995-01-01';
