import streamlit as st
import heapq

# Configuración de la interfaz visual
st.set_page_config(page_title="Conoce Inteligente el Sur de Bogotá", page_icon="🗺️", layout="centered")

st.title("🗺️ Sistema Inteligente Para Conocer el Sur de Bogotá")
st.markdown("Explora sitios turísticos y puntos de referencia del sur de la ciudad aplicando **sistemas basados en reglas** y **búsqueda heurística** adaptado al medio de transporte de tu preferencia.")

# Grafo con sitios turísticos y estaciones del sur de Bogotá
grafo_sur_bogota = {
    'Portal del Sur': {'Parque Timiza': 4.0, 'Parque El Tunal': 6.0},
    'Parque Timiza': {'Portal del Sur': 4.0, 'Centro Comercial Paseo Villa del Río': 2.5},
    'Centro Comercial Paseo Villa del Río': {'Parque Timiza': 2.5, 'Parque El Tunal': 3.5},
    'Parque El Tunal': {'Portal del Sur': 6.0, 'Centro Comercial Paseo Villa del Río': 3.5, '20 de Julio (Santuario)': 5.5},
    '20 de Julio (Santuario)': {'Parque El Tunal': 5.5, 'Portal 20 de Julio': 1.2, 'Plaza de Bolívar': 4.0},
    'Portal 20 de Julio': {'20 de Julio (Santuario)': 1.2, 'Mirador de Usme': 6.5},
    'Mirador de Usme': {'Portal 20 de Julio': 6.5},
    'Plaza de Bolívar': {'20 de Julio (Santuario)': 4.0}
}

# Heurística estimada (Distancia en línea recta aproximada en km hacia la Plaza de Bolívar)
heuristica_base = {
    'Portal del Sur': 9.0,
    'Parque Timiza': 6.5,
    'Centro Comercial Paseo Villa del Río': 5.0,
    'Parque El Tunal': 4.0,
    '20 de Julio (Santuario)': 2.0,
    'Portal 20 de Julio': 3.0,
    'Mirador de Usme': 7.0,
    'Plaza de Bolívar': 0.0
}

ubicaciones = sorted(list(grafo_sur_bogota.keys()))

# Función auxiliar para formatear el tiempo en horas y minutos si supera los 60 min
def formatear_tiempo(minutos):
    if minutos < 60:
        return f"{minutos} min"
    horas = minutos // 60
    mins_restantes = minutos % 60
    if mins_restantes == 0:
        return f"{horas} h"
    else:
        return f"{horas} h y {mins_restantes} min"

# Interfaz de usuario
col1, col2 = st.columns(2)
with col1:
    origen = st.selectbox("📍 Punto de Origen: ", ubicaciones, index=0)
with col2:
    destino = st.selectbox("🎯 Punto de Destino: ", ubicaciones, index=4)

transporte = st.selectbox(
    "🚊 Selecciona tu medio de transporte o desplazamiento de preferencia:",
    ["🚌 TransMilenio", "🚖 Taxi/Uber", "🏍️ Moto", "🚲 Bicicleta", "🚶‍♂️ A pie"]
)

# 2. Algoritmo de Búsqueda Heurística
def calcular_ruta(inicio, fin):
    pq = [(heuristica_base.get(inicio, 0), 0, inicio, [inicio])]
    visitados = set()
    
    while pq:
        f, g, actual, camino = heapq.heappop(pq)

        if actual == fin:
            return camino, g, "Ruta encontrada con éxito."

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, distancia_km in grafo_sur_bogota.get(actual, {}).items():
            if vecino not in visitados:
                nuevo_g = g + distancia_km
                h = heuristica_base.get(vecino, 0)
                nuevo_f = nuevo_g + h
                heapq.heappush(pq, (nuevo_f, nuevo_g, vecino, camino + [vecino]))
                
    return None, float('inf'), "No hay ruta conectada."

# Botón de ejecución
if st.button("🚀 Calcular Recorrido Inteligente", type="primary"):
   
    # Si el origen y destino son iguales, se corta el proceso de inmediato
    if origen == destino:
        st.warning("⚠️ **Advertencia del Sistema:** El punto de origen y el destino es el mismo.")
        
        # Métricas en ceros absolutos
        m1, m2, m3 = st.columns(3)
        m1.metric("📏 Distancia", "0.0 km")
        m2.metric("⏱️ Tiempo", "0 min")
        m3.metric("💰 Costo / Pasaje", "$0 COP")
        
        st.info(f"📍 Ya te encuentras ubicado en **{origen}**. El sistema determina que no existe desplazamiento físico, por lo que los costos, tiempos y trayectos son nulos.")
    else:
        ruta, distancia_total, mensaje = calcular_ruta(origen, destino)
        
        if distancia_total == float('inf'):
            st.error("⚠️ No hay una ruta disponible entre estos dos puntos en la base de conocimiento.")
        else:
            st.success("¡Análisis de ruta completado mediante reglas lógicas!")
            
            # Presentación de resultados personalizada según el transporte
            if transporte == "🚌 TransMilenio":
                paradas_count = len(ruta) - 1
                tiempo_aprox = int((distancia_total / 24.0) * 60) + 5
                tiempo_texto = formatear_tiempo(tiempo_aprox)
                
                m1, m2 = st.columns(2)
                m1.metric("⏱️ Tiempo Estimado", tiempo_texto)
                m2.metric("🚉 Estaciones / Paradas", f"{paradas_count} en total")
                
                st.markdown("### 🚏 Estaciones de TransMilenio:")
                for i, est in enumerate(ruta):
                    if i == 0:
                        st.markdown(f"🟢 **Inicio en estación:** {est}")
                    elif i == len(ruta) - 1:
                        st.markdown(f"🏁 **Llegada al destino:** {est}")
                    else:
                        st.markdown(f"➡️ Estación intermedia: {est}")
                st.info("🧠 **Regla aplicada:** Se calculó el uso de carril exclusivo con paradas intermedias en el sistema masivo del sur.")

            elif transporte == "🚖 Taxi/Uber":
                tarifa_base = 7100
                costo_estimado = int(tarifa_base + (distancia_total * 2600))
                tiempo_aprox = int((distancia_total / 25.0) * 60) + 8
                tiempo_texto = formatear_tiempo(tiempo_aprox)
                
                m1, m2 = st.columns(2)
                m1.metric("⏱️ Tiempo en Vía", tiempo_texto)
                m2.metric("💰 Costo Estimado", f"${costo_estimado:,} COP")
                
                st.markdown("### 🛣️ Puntos y Trayecto del Taxi/Uber:")
                for i, punto in enumerate(ruta):
                    if i == 0:
                        st.markdown(f"🟢 **Punto de recogida:** {punto}")
                    elif i == len(ruta) - 1:
                        st.markdown(f"🏁 **Punto de destino:** {punto}")
                    else:
                        st.markdown(f"📍 Pasa por / Cerca de: {punto}")
                st.info("🧠 **Regla aplicada:** Tarifa calculada sumando el banderazo inicial y el factor de distancia con taxímetro urbano.")

            elif transporte == "🏍️ Moto":
                tiempo_aprox = int((distancia_total / 32.0) * 60) + 3
                tiempo_texto = formatear_tiempo(tiempo_aprox)
                costo_gasolina = int(distancia_total * 380)
                
                m1, m2, m3 = st.columns(3)
                m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
                m2.metric("⏱️ Tiempo Ágil", tiempo_texto)
                m3.metric("⛽ Costo Gasolina", f"${costo_gasolina:,} COP")
                
                st.markdown("### 🏍️ Trayecto y Puntos de Paso:")
                for i, punto in enumerate(ruta):
                    if i == 0:
                        st.markdown(f"🟢 **Salida:** {punto}")
                    elif i == len(ruta) - 1:
                        st.markdown(f"🏁 **Llegada:** {punto}")
                    else:
                        st.markdown(f"📍 Zona de tránsito intermedio: {punto}")
                st.info("🧠 **Regla aplicada:** Se aplicó un factor de velocidad superior debido a la capacidad de filtrado vehicular de la motocicleta y consumo eficiente de combustible.")

            elif transporte == "🚲 Bicicleta":
                tiempo_aprox = int((distancia_total / 13.0) * 60)
                tiempo_texto = formatear_tiempo(tiempo_aprox)
                nivel_esfuerzo = "Alto 🏔️" if distancia_total > 5 else "Moderado 😌"
                detalle_esfuerzo = "Alto (Zonas de subida hacia el sur/cerros)" if distancia_total > 5 else "Moderado"
                
                m1, m2, m3 = st.columns(3)
                m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
                m2.metric("⏱️ Tiempo", tiempo_texto)
                m3.metric("🚴‍♂️ Esfuerzo Físico", nivel_esfuerzo)
                
                st.caption(f"📌 **Detalle de esfuerzo:** {detalle_esfuerzo}")
                
                st.markdown("### 🗺️ Trayecto en Bicicleta (Ciclorrutas y vías secundarias):")
                for i, punto in enumerate(ruta):
                    st.markdown(f"🔹 **Punto clave:** {punto}")
                st.info("🧠 **Regla aplicada:** Se evaluó el trayecto por vías secundarias y ciclorrutas, considerando la topografía del sur de la ciudad.")

            else: # A pie
                tiempo_aprox = int((distancia_total / 4.5) * 60)
                tiempo_texto = formatear_tiempo(tiempo_aprox)
                
                m1, m2 = st.columns(2)
                m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
                m2.metric("⏱️ Tiempo Caminando", tiempo_texto)
                
                st.markdown("### 🚶‍♂️ Trayecto a Pie:")
                for i, punto in enumerate(ruta):
                    st.markdown(f"👣 **Paso por:** {punto}")
                st.info("🧠 **Regla aplicada:** Cálculo basado en una velocidad promedio de caminata humana de 4.5 km/h sin costo monetario.")