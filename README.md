# 📚 Proyecto de Software | CORPORACIÓN UNIVERSITARIA IBEROAMERICANA

**Docente:** Sandra Bautista
**Curso:** 24082026_C1_202634
**Actividad:** Sistema Integral de IA (Búsqueda, Reglas, Supervisado y No Supervisado)

**Proyecto:**   
RutaSur IA — Sistema Inteligente Para Conocer y Analizar la Movilidad del Sur de Bogotá

---

## ✍🏽 1. Necesidad y Problema del Proyecto

### 📌 Descripción del problema
En las localidades del sur de Bogotá, la planificación de trayectos turísticos, académicos y cotidianos suele carecer de herramientas optimizadas que integren simultáneamente múltiples variables de movilidad (como tarifas de transporte público o privado, esfuerzo físico en bicicleta, tiempos estimados según topografía, reglas lógicas de validación y modelos predictivos de Machine Learning para detectar retrasos críticos). Los usuarios frecuentemente enfrentan desinformación sobre los tiempos reales de desplazamiento y los costos asociados.

### 🌍 Contexto del problema
El problema se presenta en el sector de movilidad urbana y turismo local, específicamente en las zonas del sur de la ciudad (como el Portal del Sur, Portal 20 de Julio, Parque El Tunal, Mirador de Usme, entre otros), donde una correcta gestión del tiempo, la analítica predictiva y el agrupamiento de datos mejoran la eficiencia del transporte.

### 👥 Población afectada
- Turistas y Visitantes: Requieren conocer rutas óptimas, tiempos estimados y costos aproximados de transporte hacia los principales puntos de interés del sur de Bogotá.
- Estudiantes y Ciudadanos: Necesitan una herramienta rápida y automatizada para planificar sus desplazamientos diarios evaluando diferentes alternativas (TransMilenio, taxi, moto, bicicleta o a pie) y anticipando niveles de congestión.

### 💡 Justificación de la solución tecnológica
La solución tecnológica RutaSur IA permite optimizar la toma de decisiones de movilidad mediante la implementación de un sistema basado en reglas lógicas, búsqueda heurística (Algoritmo A*), aprendizaje supervisado (Árboles de Decisión) y aprendizaje no supervisado (Clustering K-Means). Una aplicación interactiva centralizada ayuda al acceso rápido de la información, mejorando la planeación de trayectos y reduciendo la incertidumbre. Además, fomenta el uso de tecnologías accesibles basadas en Python y Streamlit para la simulación y análisis avanzado de redes de transporte urbano.

---

## 🎯 2. Objetivos del Proyecto

### 🎯 Objetivo General
Desarrollar una aplicación web interactiva y un sistema analítico basado en búsqueda heurística, sistemas de reglas lógicas y modelos de Machine Learning (supervisado y no supervisado) para calcular rutas, predecir retrasos y segmentar patrones de transporte en el sur de Bogotá.

### ✅ Objetivos Específicos
- Modelar la red de transporte y puntos de interés del sur de Bogotá mediante una estructura de datos tipo grafo ponderado y tablas heurísticas.
- Implementar el algoritmo de búsqueda heurística (A*) para encontrar el trayecto más eficiente entre un origen y un destino.
- Incorporar reglas lógicas para validar escenarios especiales de movilidad, climas y franjas horarias.
- Integrar un modelo de Machine Learning supervisado (Árbol de Decisión) para predecir la probabilidad de retrasos altos según las condiciones del viaje.
- Incorporar un modelo de aprendizaje no supervisado (K-Means Clustering) para descubrir y agrupar perfiles de tráfico en el dataset de transporte.
- Garantizar una experiencia de usuario (UX) intuitiva y visualmente atractiva mediante componentes interactivos en Streamlit.

---

## 📂 3. Alcance del Proyecto

### ✔️ Alcance funcional
El sistema permitirá:
- Selección interactiva de un punto de origen y un destino turístico o de transporte en el sur de Bogotá.
- Selección del medio de transporte preferido (TransMilenio, Taxi, Moto, Bicicleta, A pie).
- Cálculo automático de la distancia total en kilómetros y del tiempo estimado de viaje con formato inteligente.
- Estimación de costos monetarios (pasajes, tarifas de taxi o consumo de gasolina).
- Visualización detallada del itinerario paso a paso y evaluación del nivel de esfuerzo físico en bicicleta.
- Ejecución de predicciones en tiempo real sobre la probabilidad de retraso alto mediante Árboles de Decisión.
- Segmentación de trayectos mediante el algoritmo no supervisado K-Means.

### 🚫 Fuera de alcance
- Conexión en tiempo real con APIs de tráfico vehicular de Google Maps o Waze.
- Procesamiento de pagos integrados dentro de la plataforma.
- Aplicación móvil nativa para dispositivos iOS o Android.
- Historial persistente de rutas guardadas en bases de datos externas.

### 🎁 Beneficios esperados
- Optimización en la planeación de viajes y recorridos por el sur de Bogotá.
- Transparencia en la estimación de costos, tiempos y riesgos de congestión.
- Promoción de herramientas tecnológicas basadas en Inteligencia Artificial clásica y Machine Learning para la resolución de problemas urbanos.

---

## 🔄 4. Metodología de Desarrollo (Scrum)
### 📌 Descripción
Se emplea una metodología ágil basada en Sprints para el desarrollo iterativo e incremental del software de análisis geoespacial, de rutas y de Machine Learning.

### 👨‍💻 Roles
- Product Owner: Define y prioriza los requisitos del sistema de enrutamiento y analítica de datos, asegurando la coherencia con los modelos de IA.
- Scrum Master: Facilita el desarrollo del sprint, organiza las revisiones y elimina impedimentos técnicos en Python, Streamlit y Scikit-Learn.
- Equipo de Desarrollo: Implementa la estructura del grafo, el algoritmo A*, los árboles de decisión y los scripts de clustering no supervisado.
- Tester: Valida el funcionamiento correcto de las rutas, la precisión de los modelos supervisados y no supervisados, y la usabilidad de la interfaz web.

### 🔁 Organización
Sprints enfocados en la estructuración de la base de conocimiento, la lógica de búsqueda, los modelos predictivos y la interfaz visual.

### 🛠️ Herramientas
- Git y GitHub
- Python (Librerías de grafos, heapq, Pandas y Scikit-Learn)
- Streamlit (Framework de desarrollo web interactivo)

---

## 🔀 5. Flujo del Sistema
- El usuario ingresa a la aplicación web.
- Selecciona el Punto de Origen y el Sitio Destino en el sur de Bogotá.
- Elige su medio de transporte preferido, la hora de salida y el estado del clima.
- Hace clic en el botón de cálculo y ejecución de modelos.
- El sistema valida las reglas lógicas, ejecuta el algoritmo A* para calcular la ruta y procesa el Árbol de Decisión para evaluar el retraso.
- Se despliegan en pantalla las métricas de distancia, tiempo formateado, costos, itinerario paso a paso y la predicción de Machine Learning.
- Adicionalmente, el sistema permite correr scripts independientes de K-Means para el análisis no supervisado de los datos de transporte.


## 💻 6. Solución Tecnológica y Estructura del Repositorio

### 📌 Descripción
- Solución integral de Inteligencia Artificial compuesta por una aplicación web interactiva de enrutamiento basada en grafos, búsqueda heurística, sistemas de reglas lógicas y módulos de Machine Learning supervisado y no supervisado.

### 🏗️ Arquitectura
- Capa de Presentación (Frontend): Interfaz web desarrollada con Streamlit, diseñada con columnas métricas, avisos visuales e itinerarios estructurados.
- Capa de Lógica y Algoritmos (Backend en Python): Implementación del grafo ponderado del sur de Bogotá, tablas heurísticas, algoritmo A* y modelos de Scikit-Learn (DecisionTreeClassifier y KMeans).

### 🧰 Archivos y Componentes del Repositorio
- `actividad_2.py`: Módulo inicial con la lógica del grafo y la búsqueda heurística.
- `Actividad_3.py`: Aplicación principal en Streamlit con la interfaz visual y el modelo supervisado (Árbol de Decisión).
- `no_supervisado.py`: Script en Python encargado del modelo de aprendizaje no supervisado (K-Means Clustering).
- `generar_data.py`: Script para la creación y estructuración del dataset de movilidad.
- `python_ia.py`: Archivo auxiliar con funciones y utilidades de soporte lógico para la inteligencia artificial.
- `dataset_transporte_bogota.csv`: Archivo de datos fuente con los registros de movilidad en el sur de la ciudad.
- `dataset_transporte_bogota_clusters.csv`: Archivo de datos enriquecido con las etiquetas de clústeres generadas por el modelo no supervisado.


## 📊 7. Modelamiento del Sistema

### 🗄️ Entidades principales del Modelo
- Grafo de Ubicaciones: Estructura de diccionario que relaciona nodos (estaciones y puntos turísticos) con sus costos en kilómetros.
- Tabla Heurística: Valores estimados de distancia en línea recta desde cada nodo hacia la Plaza de Bolívar.
- Reglas de Transporte y Clima: Factores matemáticos de velocidad, banderazos, tarifas, desgaste físico y condiciones de hora pico o lluvia.
- Modelos de Aprendizaje: Dataset histórico de movilidad parametrizado para la clasificación supervisada de retrasos y segmentación no supervisada por clústeres.

## 🚀 Guía de Instalación y Ejecución Local
Para ejecutar la aplicación en un entorno de desarrollo local, siga estos pasos:

### 1. Requisitos Previos
- Asegúrese de tener instalado en su sistema:
- Python (Versión 3.8 o superior)
- Git

### 2. Clonar el Repositorio
- Abra su terminal y descargue el código fuente del proyecto.

### 3. Instalar Dependencias
- Instale las librerías requeridas ejecutando en su terminal:
- pip install streamlit pandas scikit-learn matplotlib

### 4. Ejecutar la Aplicación Principal
- Para iniciar el servidor local de Streamlit, ejecute en su terminal:
- streamlit run Actividad_3.py

### 5. Ejecución del Módulo No Supervisado
- Para correr el script de agrupamiento K-Means de manera independiente, ejecute:
- python no_supervisado.py

---
  
## 🫱🏽‍🫲🏽 Autores  

- Andrés Felipe Luengas  
- Alejandro Rodriguez Guarnizo
