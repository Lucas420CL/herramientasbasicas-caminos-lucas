# Trabajo Práctico Final - Herramientas básicas para el Análisis de Datos

* **Autor:** Lucas Caminos
* **Curso / Cohorte:** Herramientas básicas para el Análisis de Datos - UTN BA
* **Dataset utilizado:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 1. Objetivo del Proyecto
Integrar un flujo completo de análisis de datos end-to-end, abarcando desde la ingesta, auditoría y limpieza en Python (Pandas), pasando por la exploración visual (Matplotlib y Seaborn), hasta la construcción de un dashboard interactivo en Power BI para la toma de decisiones comerciales.

## 2. Pregunta Principal y KPIs
* **Pregunta principal:** ¿Cómo evolucionaron las ventas mensuales por categoría entre 2016 y 2018 y qué factores explican el volumen de transacciones en la plataforma de e-commerce?
* **KPIs definidos:**
  1. Facturación Neta Total.
  2. Ticket Promedio por Transacción.
  3. Volumen de unidades vendidas por categoría.

## 3. Pasos Realizados
1. **Ingesta y Limpieza (Python):** Carga de tablas relacionales de Olist, tratamiento de valores nulos en categorías, conversión de tipos de datos y estandarización de marcas temporales (`datetime`).
2. **EDA y Visualizaciones:** Generación de gráficos analíticos de evolución temporal, distribución de precios y ranking de categorías con Matplotlib y Seaborn.
3. **Dashboard (Power BI):** Desarrollo de un reporte interactivo con tarjetas de KPIs, gráficos de tendencia y filtros cruzados por período.

## 4. Estructura del Repositorio
* `/data/raw/`: Contiene los archivos fuente en formato CSV.
* `/notebooks/`: Archivo con el código de preparación y EDA en Python.
* `/dashboard/`: Archivo del reporte interactivo y capturas de visualización.

## 5. Interpretación de Resultados y Hallazgos
* **Evolución de las ventas:** El análisis temporal muestra un crecimiento sostenido de la plataforma entre 2016 y 2018, con picos estacionales marcados en periodos de alta actividad comercial.
* **Distribución de estados de órdenes:** Se observa que la gran mayoría de las órdenes se completan con éxito en el estado de entregadas (*delivered*), evidenciando una buena eficiencia logística general.
* **Categorías más vendidas:** Las categorías principales concentran el mayor volumen de transacciones, traccionando el ticket promedio de la tienda.

## 6. Conclusión Final
El desarrollo del proyecto permitió aplicar un flujo completo de análisis de datos (*end-to-end*): desde la ingesta y limpieza con Pandas y la exploración visual en Python, hasta la consolidación del tablero interactivo en Power BI. Con esto se logró responder a las preguntas de negocio planteadas, demostrando cómo el rendimiento logístico y la concentración de categorías impactan directamente en el volumen de ventas del e-commerce.
