"""
03_funciones_y_archivos.py

Funciones para trabajar con archivos de datos (por ejemplo CSV) de empleados
y calcular indicadores básicos.
"""

import csv
from pathlib import Path

DATA_DIR = Path("data")  # si luego creas una carpeta data/

def leer_empleados_desde_csv(nombre_archivo):
    """
    Lee un archivo CSV de empleados y regresa una lista de diccionarios.
    """
    ruta = DATA_DIR / nombre_archivo
    empleados = []
    with ruta.open(mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            fila["salario"] = float(fila["salario"])
            empleados.append(fila)
    return empleados

def salario_promedio(empleados):
    """
    Calcula el salario promedio de una lista de empleados.
    """
    if not empleados:
        return 0
    total = sum(e["salario"] for e in empleados)
    return total / len(empleados)

def guardar_reporte_salarios(nombre_salida, promedio):
    ruta = DATA_DIR / nombre_salida
    with ruta.open(mode="w", encoding="utf-8") as f:
        f.write(f"Salario promedio: {promedio:.2f}\n")

if __name__ == "__main__":
    empleados = leer_empleados_desde_csv("empleados.csv")
    prom = salario_promedio(empleados)
    print(f"Salario promedio: {prom:.2f}")
    guardar_reporte_salarios("reporte_salarios.txt", prom)
