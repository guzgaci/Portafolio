"""
08_visualizaciones.py
Gráficos profesionales con Matplotlib.
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "departamento": ["TI", "Finanzas", "Marketing", "RH"],
    "salario_promedio": [30000, 28000, 25000, 23000]
})

plt.bar(df["departamento"], df["salario_promedio"])
plt.title("Salario promedio por departamento")
plt.xlabel("Departamento")
plt.ylabel("Salario")
plt.tight_layout()
plt.show()
