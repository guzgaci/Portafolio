"""
09_anomalias_salarios.py
Detectar valores atípicos usando IQR.
"""

import pandas as pd

df = pd.DataFrame({
    "salario": [10000, 12000, 13000, 12500, 500000, 14000, 15000]
})

Q1 = df["salario"].quantile(0.25)
Q3 = df["salario"].quantile(0.75)
IQR = Q3 - Q1

lim_inferior = Q1 - 1.5 * IQR
lim_superior = Q3 + 1.5 * IQR

df["anomalia"] = df["salario"].apply(
    lambda x: "SI" if x < lim_inferior or x > lim_superior else "NO"
)

print(df)
