-- 06_ranking_empleados.sql
SELECT 
    e.id_empleado,
    e.nombre,
    e.salario,
    RANK() OVER (ORDER BY e.salario DESC) AS ranking_salario
FROM empleados e;
