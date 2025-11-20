"""
05_limpieza_datos.py
Ejemplo profesional de limpieza y depuración de datos.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "nombre": ["Ana", "Luis", "Maria", None, "Carlos"],
    "salario": [25000, None, 22000, 18000, -5000],
    "departamento": ["TI", "Finanzas", None, "TI", "Marketing"]
})

print("=== Datos crudos ===")
print(df)

# Eliminar salarios negativos
df.loc[df["salario"] < 0, "salario"] = np.nan

# Rellenar valores faltantes
df["nombre"] = df["nombre"].fillna("Desconocido")
df["departamento"] = df["departamento"].fillna("Pendiente")

# Rellenar salarios con promedio
df["salario"] = df["salario"].fillna(df["salario"].mean())

print("\n=== Datos limpios ===")
print(df)
