import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética de gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. INGESTA DE DATOS (Ajusta la ruta según tus archivos locales)
ruta = "" # Dejar vacío si están en la misma ruta o poner la carpeta correspondiente
df_orders = pd.read_csv(ruta + 'olist_orders_dataset.csv')
df_items = pd.read_csv(ruta + 'olist_order_items_dataset.csv')
df_products = pd.read_csv(ruta + 'olist_products_dataset.csv')

# 2. AUDITORÍA Y LIMPIEZA (Punto 2 de la rúbrica)
print("--- NULOS EN ÓRDENES ---")
print(df_orders.isnull().sum())

print("\n--- NULOS EN PRODUCTOS ---")
print(df_products.isnull().sum())

# Estandarización de fechas a tipo datetime
df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp'])
df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'])

# Limpieza de nulos rellenando categorías faltantes
df_products['product_category_name'] = df_products['product_category_name'].fillna('desconocido')

# 3. UNIÓN DE TABLAS PARA EL EDA
df_merged = df_items.merge(df_orders, on='order_id', how='inner')
df_merged = df_merged.merge(df_products, on='product_id', how='inner')

# Creación de columna temporal para análisis mensual
df_merged['anio_mes'] = df_merged['order_purchase_timestamp'].dt.to_period('M')

# 4. EXPLORACIÓN Y VISUALIZACIÓN (Punto 3 de la rúbrica)

# Gráfico 1: Evolución temporal de las ventas mensuales
plt.figure()
ventas_mensuales = df_merged.groupby('anio_mes')['price'].sum().reset_index()
ventas_mensuales['anio_mes'] = ventas_mensuales['anio_mes'].astype(str)
sns.lineplot(data=ventas_mensuales, x='anio_mes', y='price', marker='o', color='b')
plt.xticks(rotation=45)
plt.title('Evolución de la Facturación Mensual (2016-2018)')
plt.xlabel('Año-Mes')
plt.ylabel('Facturación Total ($)')
plt.tight_layout()
plt.show()

# Gráfico 2: Top 10 Categorías con mayor volumen de ventas
plt.figure()
top_categorias = df_merged['product_category_name'].value_counts().head(10).reset_index()
top_categorias.columns = ['categoria', 'cantidad']
sns.barplot(data=top_categorias, x='cantidad', y='categoria', palette='viridis')
plt.title('Top 10 Categorías de Productos más Vendidos')
plt.xlabel('Cantidad de Unidades')
plt.ylabel('Categoría')
plt.tight_layout()
plt.show()

# Gráfico 3: Distribución del precio de los ítems (Outliers)
plt.figure()
sns.boxplot(x=df_merged['price'], color='orange')
plt.title('Distribución de Precios Unitarios')
plt.xlabel('Precio ($)')
plt.tight_layout()
plt.show()
