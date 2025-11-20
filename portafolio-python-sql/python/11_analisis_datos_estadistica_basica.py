"""
Cálculo de estadísticas descriptivas básicas para un dataset de salarios.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def estadisticas_salarios(df, col="salario"):
    descripcion = df[col].describe()
    return descripcion

if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR / "empleados_clean.csv")
    desc = estadisticas_salarios(df)
    print(desc)
