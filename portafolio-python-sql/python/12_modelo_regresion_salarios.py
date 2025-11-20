"""
Modelo de regresión lineal para predecir salarios a partir de años de experiencia.
"""

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

DATA_DIR = Path("data")

if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR / "empleados_ml.csv")
    X = df[["anios_experiencia"]]
    y = df["salario"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    print("Coeficiente:", modelo.coef_[0])
    print("Intercepto:", modelo.intercept_)
    print("RMSE:", rmse)
