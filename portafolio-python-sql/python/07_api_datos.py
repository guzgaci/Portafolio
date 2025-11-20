"""
07_api_datos.py
Ejemplo de consumo de una API pública y limpieza posterior.
"""

import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
resp = requests.get(url)
data = resp.json()

df = pd.DataFrame(data)[["id", "name", "email", "company"]]
df["company"] = df["company"].apply(lambda x: x["name"])

print(df.head())
