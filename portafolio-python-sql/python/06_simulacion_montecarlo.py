"""
06_simulacion_montecarlo.py
Simula un portafolio con rendimientos aleatorios.
"""

import numpy as np

# Parámetros
n_simulaciones = 10000
rend_medio = 0.07
volatilidad = 0.15
inversion_inicial = 100000

rendimientos = np.random.normal(
    loc=rend_medio, 
    scale=volatilidad, 
    size=n_simulaciones
)

valores_finales = inversion_inicial * (1 + rendimientos)

print("Valor esperado:", valores_finales.mean())
print("Percentil 5% (escenario pesimista):", np.percentile(valores_finales, 5))
print("Percentil 95% (escenario optimista):", np.percentile(valores_finales, 95))
