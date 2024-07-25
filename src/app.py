import os
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup
url = "https://es.wikipedia.org/wiki/Leucocito"
html_data = requests.get(url, time.sleep(10)).text  # Método GET usado

# If no information is extracted, then connect as anonymous
if "403 Forbidden" in html_data:
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    request = requests.get(url, headers = headers)
    time.sleep(10)
    html_data = request.text

    # Mostrar el contenido HTML obtenido
# print(html_data)

soup = BeautifulSoup(html_data,"html.parser")

# Find all tables
tabla = soup.find_all("table", class_="wikitable")

tabla = tabla[0]

# Inicializar listas para almacenar los datos
columnas = []
filas = []

# Extraer los encabezados de la tabla
for th in tabla.find_all("th"):
    columnas.append(th.text.strip())

# Extraer las filas de la tabla
for tr in tabla.find_all("tr"):
    celdas = tr.find_all("td")
    if len(celdas) > 0:
        fila = [td.text.strip() for td in celdas]
        filas.append(fila)

# Crear el DataFrame de Pandas
df = pd.DataFrame(filas, columns=columnas)

# Mostrar el DataFrame
print(df)

# Nombres de las columnas
#print("Nombres de las columnas:", df.columns)

# Seleccionar las columnas relevantes
tipos = df['Tipo']
porcentajes = df['Porcentaje aproximado en adultos'].str.replace('%', '').astype(float)  # Eliminar el signo '%' y convertir a float
# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(tipos, porcentajes, color='skyblue')
plt.xlabel('Tipo de leucocito')
plt.ylabel('Porcentaje aproximado en adultos')
plt.title('Comparación de tipos de leucocitos y su porcentaje aproximado en adultos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("Done")




