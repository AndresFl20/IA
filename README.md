#📚 Proyecto de Software | CORPORACIÓN UNIVERSITARIA IBEROAMERICANA

**Docente:** Sandra Bautista
**Curso:** 24082026_C1_202634
**Actividad 2:** Búsqueda y sistemas basados en reglas

**Proyecto:**   
RutaSur IA — Sistema Inteligente Para Conocer el Sur de Bogotá

---

## ✍🏽 1. Necesidad y Problema del Proyecto

### 📌 Descripción del problema
En las localidades del sur de Bogotá, la planificación de trayectos turísticos, académicos y cotidianos suele carecer de herramientas optimizadas que integren simultáneamente múltiples variables de movilidad (como tarifas de transporte público o privado, esfuerzo físico en bicicleta, tiempos estimados según topografía y reglas lógicas de validación). Los usuarios frecuentemente enfrentan desinformación sobre los tiempos reales de desplazamiento y los costos asociados.

### 🌍 Contexto del problema
El problema se presenta en el sector de movilidad urbana y turismo local, específicamente en las zonas del sur de la ciudad (como el Portal del Sur, Portal 20 de Julio, Parque El Tunal, Mirador de Usme, entre otros), donde una correcta gestión del tiempo y la ruta mejora la eficiencia del transporte.

### 👥 Población afectada
- Turistas y Visitantes: Requieren conocer rutas óptimas, tiempos estimados y costos aproximados de transporte hacia los principales puntos de interés del sur de Bogotá.
- Estudiantes y Ciudadanos: Necesitan una herramienta rápida y automatizada para planificar sus desplazamientos diarios evaluando diferentes alternativas (TransMilenio, taxi, moto, bicicleta o a pie).

### 💡 Justificación de la solución tecnológica
La solución tecnológica RutaSur IA permite optimizar la toma de decisiones de movilidad mediante la implementación de un sistema basado en reglas lógicas y búsqueda heurística (Algoritmo A*). Una aplicación interactiva centralizada ayuda al acceso rápido de la información, mejorando la planeación de trayectos y reduciendo la incertidumbre en los tiempos de viaje. Además, fomenta el uso de tecnologías accesibles basadas en Python y Streamlit para la simulación y análisis de redes de transporte urbano.

---

##🎯 2. Objetivos del Proyecto

### 🎯 Objetivo General
Desarrollar una aplicación web interactiva basada en búsqueda heurística y sistemas de reglas lógicas para calcular y optimizar rutas, tiempos, distancias y costos de transporte entre diferentes puntos clave del sur de Bogotá.

### ✅ Objetivos Específicos
- Modelar la red de transporte y puntos de interés del sur de Bogotá mediante una estructura de datos tipo grafo ponderado.
- Implementar el algoritmo de búsqueda heurística (A*) para encontrar el trayecto más eficiente entre un origen y un destino seleccionados por el usuario.
- Incorporar reglas lógicas para validar escenarios especiales, como la detección de un origen y destino idénticos con métricas en cero.
- Adaptar el cálculo de resultados a diferentes medios de transporte (TransMilenio, taxi, moto, bicicleta y a pie), integrando variables como tarifas, consumo de combustible o esfuerzo físico.
- Garantizar una experiencia de usuario (UX) intuitiva, rápida y visualmente atractiva mediante componentes interactivos en Streamlit.

---

## 📂 3. Alcance del Proyecto

### ✔️ Alcance funcional
El sistema permitirá:
- Selección interactiva de un punto de origen y un destino turístico o de transporte en el sur de Bogotá.
- Selección del medio de transporte preferido (TransMilenio, Taxi, Moto, Bicicleta, A pie).
- Cálculo automático de la distancia total en kilómetros y del tiempo estimado de viaje (con formato inteligente de horas y minutos para trayectos largos).
- Estimación de costos monetarios (pasajes de TransMilenio, tarifas de taxi o consumo de gasolina en moto).
- Visualización detallada del itinerario paso a paso (estaciones intermedias, puntos clave o zonas de tránsito).
- Evaluación del nivel de esfuerzo físico para trayectos en bicicleta según la topografía del sur.

### 🚫 Fuera de alcance
- Conexión en tiempo real con APIs de tráfico vehicular de Google Maps o Waze.
- Procesamiento de pagos integrados dentro de la plataforma.
- Aplicación móvil nativa para dispositivos iOS o Android.
- Historial persistente de rutas guardadas en bases de datos externas.

### 🎁 Beneficios esperados
- Optimización en la planeación de viajes y recorridos por el sur de Bogotá.
- Transparencia en la estimación de costos y tiempos según el medio de transporte elegido.
- Promoción de herramientas tecnológicas basadas en Inteligencia Artificial y teoría de grafos para la resolución de problemas urbanos.

---

## 🔄 4. Metodología de Desarrollo (Scrum)
### 📌 Descripción
Se emplea una metodología ágil basada en Sprints para el desarrollo iterativo e incremental del software de análisis geoespacial y de rutas.

### 👨‍💻 Roles
- Product Owner: Define y prioriza los requisitos del sistema de enrutamiento, asegurando que las reglas lógicas y el cálculo del algoritmo A* respondan a las necesidades de movilidad del sur de Bogotá.
- Scrum Master: Facilita el desarrollo del sprint, organiza las revisiones y elimina impedimentos técnicos en el entorno de Python y Streamlit.
- Equipo de Desarrollo: Implementa la estructura del grafo, la lógica matemática del algoritmo de búsqueda heurística y la maquetación de la interfaz de usuario.
- Tester: Valida el funcionamiento correcto de las rutas, la precisión de los tiempos calculados, el manejo de excepciones (como origen igual a destino) y la usabilidad de la interfaz web.

### 🔁 Organización
Sprints de 1 a 2 semanas enfocados en la estructuración de la base de conocimiento, la lógica de búsqueda, la parametrización de transportes y la interfaz visual.

### 🛠️ Herramientas
- Git y GitHub
- Python (Lotecas de grafos y manejo de colas de prioridad con heapq)
- Streamlit (Framework de desarrollo web interactivo)

---

## 🔀 5. Flujo del Sistema
- El usuario ingresa a la aplicación web.
- Selecciona el Punto de Origen y el Sitio Destino en el sur de Bogotá.
- Elige su medio de transporte preferido.
- Hace clic en el botón "🚀 Calcular Recorrido Inteligente".
- El sistema valida si el origen y el destino son iguales (si lo son, muestra ceros y un aviso; si son distintos, ejecuta el algoritmo A*).
- Se despliegan en pantalla las métricas de distancia, tiempo formateado, costos y el itinerario detallado paso a paso con su respectiva regla lógica aplicada.


## 💻 6. Solución Tecnológica

### 📌 Descripción
- Aplicación web interactiva de enrutamiento basada en grafos, inteligencia artificial clásica (búsqueda heurística) y sistemas basados en reglas lógicas.

### 🏗️ Arquitectura
- Capa de Presentación (Frontend): Interfaz web desarrollada con Streamlit, diseñada con columnas métricas, avisos visuales e itinerarios estructurados.
- Capa de Lógica y Algoritmos (Backend en Python): Implementación del grafo ponderado del sur de Bogotá, tablas heurísticas y el algoritmo de búsqueda A* con cola de prioridad (heapq).

### 🧰 Tecnologías
- Python: Lenguaje principal para la lógica de grafos y procesamiento de datos.
- Streamlit: Framework para la creación rápida de la interfaz de usuario web interactiva.
- Algoritmo A:* Búsqueda heurística informada para la optimización de caminos mínimos.
- Git y GitHub: Control de versiones y documentación colaborativa del proyecto.


## 📊 7. Modelamiento del Sistema

###🗄️ Entidades principales del Modelo
- Grafo de Ubicaciones: Estructura de diccionario que relaciona nodos (estaciones y puntos turísticos) con sus costos en kilómetros.
- Tabla Heurística: Valores estimados de distancia en línea recta desde cada nodo hacia la Plaza de Bolívar.
- Reglas de Transporte: Factores matemáticos de velocidad, costos de banderazo, tarifas y desgaste físico asociados a cada medio de desplazamiento.

## 🚀 Guía de Instalación y Ejecución Local
Para ejecutar la aplicación en un entorno de desarrollo local, siga estos pasos:

### 1. Requisitos Previos
- Asegúrese de tener instalado en su sistema:
- Python (Versión 3.8 o superior)
- Git

###  2. Clonar el Repositorio
- Abra su terminal y descargue el código fuente del proyecto.

### 3. Instalar Dependencias
- Instale el framework de interfaz gráfica requerido ejecutando:
- pip install streamlit


### 4. Ejecutar la Aplicación
- Para iniciar el servidor local de Streamlit, ejecute en su terminal:
- streamlit run actividad_2.py

---
  
## 🫱🏽‍🫲🏽 Autores  

- Andrés Felipe Luengas  
- Alejandro Rodriguez Guarnizo  
