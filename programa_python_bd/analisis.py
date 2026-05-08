import pandas as pd
import matplotlib.pyplot as plt
ruta="basededatosexcel.csv"
Datos_formulario=pd.read_csv(ruta)

print("imprimiendo los encabezados del archivo")
print (Datos_formulario.head())

print("imprimiendo informacion de el formulario:")
print (Datos_formulario.info())

print ("imprimiendo estadisticas de los productos:")

Datos_formulario["PRECIO"]= Datos_formulario["PRECIO"].replace('[/$,]','',regex=True).astype(float)
suma_productos=Datos_formulario["PRECIO"].sum()
max_productos=Datos_formulario["PRECIO"].max()
min_productos=Datos_formulario["PRECIO"].min()
prom_productos=Datos_formulario["PRECIO"].mean()
ordenado_productos=Datos_formulario["PRECIO"].sort_values()


print (f"suma de productos:{suma_productos}")
print("-----------------------------")
print (f"maximo de productos:{max_productos}")
print("-----------------------------")
print (f"minimo de productos:{min_productos}")
print("-----------------------------")
print (f"promedio de productos:{prom_productos}")
print("-----------------------------")
print(f"productos ordenados{ordenado_productos}")
print("-----------------------------")


plt.figure(figsize=(10,6))
plt.hist(Datos_formulario["PRECIO"], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("PRECIO")
plt.ylabel("FRECUENCIA")
plt.title("PRECIO DE PRODUCTOS")
plt.show()

plt.figure(figsize=(10,6))
plt.hist(Datos_formulario["MARCA"], bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.xlabel("MARCA")
plt.ylabel("FRECUENCIA")
plt.title("MARCA DE PRODUCTOS")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(Datos_formulario["STOCK"], Datos_formulario["PRECIO"], color='red', edgecolors='black', alpha=0.8)
plt.xlabel("STOCK")
plt.ylabel("PRECIO")
plt.title("Relación entre STOCK y PRECIO")
plt.grid(True)
plt.show()
