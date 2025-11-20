CREATE TABLE departamentos (
    id_departamento INT PRIMARY KEY,
    nombre_departamento VARCHAR(100) NOT NULL
);

CREATE TABLE empleados (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sexo CHAR(1),
    salario DECIMAL(12,2),
    anios_experiencia INT,
    fecha_nacimiento DATE,
    id_departamento INT,
    id_jefe INT,
    FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento)
);
