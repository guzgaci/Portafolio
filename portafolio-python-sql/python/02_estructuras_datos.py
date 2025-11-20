"""
02_estructuras_datos.py

Ejemplos de estructuras de datos en Python dentro de un contexto de
empleados, departamentos y cursos de capacitación.
"""

# Lista de empleados (cada uno será un diccionario)
empleados = [
    {"id": 1, "nombre": "Ana", "departamento": "Finanzas", "salario": 25000},
    {"id": 2, "nombre": "Luis", "departamento": "TI", "salario": 30000},
    {"id": 3, "nombre": "María", "departamento": "Recursos Humanos", "salario": 22000},
]

# Tuplas para representar cursos (id, nombre, tema)
cursos = (
    (1, "Introducción a SQL", "TIC"),
    (2, "Python para análisis de datos", "TIC"),
    (3, "Habilidades blandas", "Soft skills"),
)

# Diccionario para contar empleados por departamento
empleados_por_depto = {}

for empleado in empleados:
    depto = empleado["departamento"]
    if depto not in empleados_por_depto:
        empleados_por_depto[depto] = 0
    empleados_por_depto[depto] += 1

print("Empleados por departamento:", empleados_por_depto)

# Lista por comprensión: salarios mayores de 25000
salarios_altos = [e["salario"] for e in empleados if e["salario"] > 25000]
print("Salarios altos:", salarios_altos)
