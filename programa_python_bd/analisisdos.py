import pandas as pd
import matplotlib.pyplot as plt

ruta = "ventas.csv"
ventas = pd.read_csv(ruta, encoding='latin1')

#convetir fecha a datetime
ventas['Fecha'] = pd.to_datetime(ventas['Fecha'], dayfirst=True)

#columna mes tomando en cuenta Fecha
ventas['Mes']= ventas['Fecha'].dt.to_period('M')


#crear columna ingreso multiplicando cantidad con precio unitario
ventas['Ingreso'] = ventas['Cantidad']* ventas['Precio Unitario']

#Agrupar por mes y sumar los ingresos 
#imprimir tabla
ventasmes= ventas.groupby('Mes')['Ingreso'].sum().reset_index()
print(ventasmes)

#agrupar ventas por ciudad
ciudad = ventas.groupby('Ciudad')['Ingreso'].sum().sort_values(ascending=True)
print(ciudad)

#agrupar ventas por producto

producto= ventas.groupby('Producto')['Cantidad'].sum().sort_values()
print(producto)


#estadisticas clave 

masvendido = producto.idxmax()
cantidadmax = producto.max()

ingresototal = ventas['Ingreso'].sum()

print(f'prodctos mas vendidos: {masvendido} con {cantidadmax}')


#GRAFICAS 
plt.style.use('dark_background')

color_azul = '#1f77b4'
color_morado = '#9467bd'
color_gris = '#7f7f7f'


#graficas de ventas mensuales 
plt.figure(figsize=(20, 10))
plt.plot(ventasmes['Mes'].astype(str), ventasmes['Ingreso'], color=color_azul, marker='o', linewidth=3)
plt.xlabel('Mes', fontsize=14, color='white')
plt.ylabel('Ingreso total', fontsize=14, color='white')
plt.title('INGRESOS MENSUALES', fontsize=18, color=color_azul)
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()



#GRAFICA DE VENTAS POR CIUDAD
plt.figure(figsize=(20, 10))
ciudad.plot(kind='barh', color=color_morado)
plt.title('VENTAS POR CIUDAD', fontsize=18, color=color_morado)
plt.xlabel('Ingreso total', fontsize=14, color='white')
plt.ylabel('Ciudad', fontsize=14, color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()


#ventas por producto
plt.figure(figsize=(10, 5))
producto.plot(kind='bar', color=color_gris)
plt.title('Ventas de producto', fontsize=16, color=color_gris)
plt.xlabel('Producto', fontsize=12, color='white')
plt.ylabel('Cantidad vendida', fontsize=12, color='white')
plt.xticks(rotation=90, color='white')
plt.yticks(color='white')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()











