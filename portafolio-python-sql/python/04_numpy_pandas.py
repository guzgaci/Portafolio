"""
04_numpy_pandas.py

Análisis con pandas de empleados, salarios y cursos.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def cargar_datos_empleados():
    ruta = DATA_DIR / "empleados.csv"
    return pd.read_csv(ruta)

def indicadores_por_departamento(df):
    resumen = (
        df.groupby("departamento")
          .agg(
              salario_promedio=("salario", "mean"),
              salario_min=("salario", "min"),
              salario_max=("salario", "max"),
              n_empleados=("id_empleado", "count"),
          )
          .reset_index()
    )
    return resumen

if __name__ == "__main__":
    df = cargar_datos_empleados()
    resumen = indicadores_por_departamento(df)
    print(resumen)
