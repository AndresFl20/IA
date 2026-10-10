import streamlit as st
import heapq
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Configuración de la interfaz visual
st.set_page_config(page_title="Conoce Inteligente el Sur de Bogotá", page_icon="🗺️", layout="centered")

st.title("🗺️ Sistema Inteligente Para Conocer el Sur de Bogotá")
st.markdown("Explora sitios turísticos y puntos de referencia del sur aplicando **búsqueda heurística**, **reglas lógicas de movilidad comparativa** y **Machine Learning supervisado**.")

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
    minutos = int(round(minutos))
    if minutos < 1:
        return "1 min"
    if minutos < 60:
        return f"{minutos} min"
    horas = minutos // 60
    mins_restantes = minutos % 60
    if mins_restantes == 0:
        return f"{horas} h"
    else:
        return f"{horas} h y {mins_restantes} min"

# Inicializar memoria de sesión
if 'ruta_calculada' not in st.session_state:
    st.session_state.ruta_calculada = None
    st.session_state.distancia_total = 0.0
    st.session_state.transporte_elegido = None

# Interfaz de usuario
col1, col2 = st.columns(2)
with col1:
    origen = st.selectbox("📍 Punto de Origen: ", ubicaciones, index=0)
with col2:
    destino = st.selectbox("🎯 Punto de Destino: ", ubicaciones, index=4)

transporte = st.selectbox(
    "🚊 Selecciona tu medio de transporte:",
    ["🚌 TransMilenio", "🚖 Taxi/Uber", "🏍️ Moto", "🚲 Bicicleta", "🚶‍♂️ A pie"]
)

st.markdown("### 🕒 Contexto del Viaje y Reglas de Movilidad")
col_c1, col_c2 = st.columns(2)
with col_c1:
    hora_salida = st.slider("Hora de salida (Formato 24h)", 0, 23, 7)
with col_c2:
    clima_actual = st.selectbox("Estado del clima", ["Soleado / Normal", "Lluvioso 🌧️"])

# Clasificación de la franja horaria
es_madrugada = (0 <= hora_salida < 4) or (hora_salida == 23)
es_hora_pico = (6 <= hora_salida <= 8) or (17 <= hora_salida <= 19)
es_hora_valle = not es_madrugada and not es_hora_pico

if es_madrugada:
    st.caption("🌙 **Detección de Sistema:** Horario de **Madrugada** Vías libres / Precaución de seguridad peatonal.")
elif es_hora_pico:
    st.caption("⚡ **Detección de Sistema:** **Hora Pico** Tráfico pesado.")
else:
    st.caption("🟢 **Detección de Sistema:** **Hora Valle** Tráfico fluido.")

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

# Botón para calcular ruta
if st.button("🚀 Calcular Recorrido Inteligente", type="primary"):
    if transporte == "🚌 TransMilenio" and es_madrugada:
        st.error("🚨 **Alerta de Reglas:** TransMilenio NO opera en la franja de 23:00 - 04:00. Por Favor desplazate en Taxi/Uber o Moto.")
        st.session_state.ruta_calculada = None
    elif origen == destino:
        st.warning("⚠️ El punto de origen y el destino son el mismo.")
        st.session_state.ruta_calculada = [origen]
        st.session_state.distancia_total = 0.0
        st.session_state.transporte_elegido = transporte
    else:
        ruta, distancia_total, mensaje = calcular_ruta(origen, destino)
        if distancia_total == float('inf'):
            st.error("⚠️ No hay una ruta disponible entre estos dos puntos.")
            st.session_state.ruta_calculada = None
        else:
            st.session_state.ruta_calculada = ruta
            st.session_state.distancia_total = distancia_total
            st.session_state.transporte_elegido = transporte

# Mostrar resultados con comparación analítica de tiempos
if st.session_state.ruta_calculada and st.session_state.distancia_total > 0:
    ruta = st.session_state.ruta_calculada
    distancia_total = st.session_state.distancia_total
    
    st.success("¡Análisis de ruta completado con evaluación comparativa de tiempos!")
    
    if es_madrugada and transporte in ["🚶‍♂️ A pie", "🚲 Bicicleta"]:
        if transporte == "🚶‍♂️ A pie":
            st.error("🚨 **ALERTA DE SEGURIDAD:** Caminar de madrugada en el sur de Bogotá implica alto riesgo. Se recomienda tomar Taxi/Uber o Moto.")
        else:
            st.warning("⚠️ **ALERTA NOCTURNA:** Ciclista de noche, mantén luces y alta visibilidad.")

    if transporte == "🚌 TransMilenio":
        paradas_count = len(ruta) - 1
        tiempo_base_valle = (distancia_total / 24.0) * 60
        vel_tm = 28.0 if es_madrugada else (24.0 if es_hora_valle else 14.0)
        if clima_actual == "Lluvioso 🌧️":
            vel_tm *= 0.85
            
        tiempo_actual = (distancia_total / vel_tm) * 60 + (5 if clima_actual == "Lluvioso 🌧️" else 0)
        diferencia = tiempo_actual - tiempo_base_valle
        
        m1, m2 = st.columns(2)
        m1.metric("⏱️ Tiempo Total Estimado", formatear_tiempo(tiempo_actual))
        m2.metric("🚉 Estaciones / Paradas", f"{paradas_count} en total")
        
        if diferencia < 0:
            st.success(f"⚡ **Optimización:** ¡Te ahorras aprox. **{int(abs(diferencia))} minutos** frente a hora valle!")
        elif diferencia > 5:
            st.warning(f"⚠️ **Demora:** Retraso de aprox. **{int(diferencia)} minutos** frente al flujo normal.")
        else:
            st.info("🟢 **Flujo Regular:** Desplazamiento en tiempos esperados.")
            
    elif transporte == "🚖 Taxi/Uber":
        tarifa_base = 7100
        costo_base = tarifa_base + (distancia_total * 2600)
        tiempo_base_valle = (distancia_total / 32.0) * 60
        
        if es_madrugada:
            velocidad_promedio = 46.0 if clima_actual == "Soleado / Normal" else 40.0
        elif es_hora_valle:
            velocidad_promedio = 30.0 if clima_actual == "Soleado / Normal" else 24.0
        else:
            velocidad_promedio = 16.0 if clima_actual == "Soleado / Normal" else 11.0

        tiempo_actual = (distancia_total / velocidad_promedio) * 60
        diferencia = tiempo_actual - tiempo_base_valle
        
        multiplicador_dinamico = 1.0
        if es_hora_pico: multiplicador_dinamico += 0.30
        if es_madrugada: multiplicador_dinamico += 0.20
        if clima_actual == "Lluvioso 🌧️": multiplicador_dinamico += 0.25
            
        costo_final = int(costo_base * multiplicador_dinamico)
        
        m1, m2 = st.columns(2)
        m1.metric("⏱️ Tiempo en Vía", formatear_tiempo(tiempo_actual))
        m2.metric("💰 Costo Estimado", f"${costo_final:,} COP")
        
        if diferencia < -3:
            st.success(f"🌙 **Ahorro por Madrugada:** ¡Te ahorras **{int(abs(diferencia))} minutos** con vías despejadas!")
        elif diferencia > 5:
            st.warning(f"⚠️ **Retraso Vehicular:** Te demorarás **{int(diferencia)} minutos más** por tráfico o clima.")
        else:
            st.info("🟢 **Condición Normal:** Tráfico estable y fluido.")
            
    elif transporte == "🏍️ Moto":
        tiempo_base_valle = (distancia_total / 35.0) * 60
        if es_madrugada:
            vel_moto = 48.0 if clima_actual == "Soleado / Normal" else 42.0
        elif es_hora_valle:
            vel_moto = 35.0 if clima_actual == "Soleado / Normal" else 30.0
        else:
            vel_moto = 24.0 if clima_actual == "Soleado / Normal" else 18.0

        tiempo_actual = (distancia_total / vel_moto) * 60
        diferencia = tiempo_actual - tiempo_base_valle
        factor_consumo = 1.30 if es_hora_pico or clima_actual == "Lluvioso 🌧️" else 1.0
        costo_gasolina = int(distancia_total * 380 * factor_consumo)
        
        m1, m2, m3 = st.columns(3)
        m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
        m2.metric("⏱️ Tiempo Ágil", formatear_tiempo(tiempo_actual))
        m3.metric("⛽ Gasolina", f"${costo_gasolina:,} COP")
        
        if clima_actual == "Lluvioso 🌧️":
            st.warning("⚠️ **Precaución por Lluvia:** Aumento en el tiempo de viaje por asfalto húmedo y tráfico pesado.")
        elif es_hora_pico:
            st.warning("⚡ **Hora Pico:** Filtrando entre carriles con velocidad moderada.")
        else:
            st.info("🟢 **Desplazamiento Óptimo:** Tráfico fluido en moto.")
            
    elif transporte == "🚲 Bicicleta":
        tiempo_base_valle = (distancia_total / 15.0) * 60
        tiempo_actual = (distancia_total / (16.0 if es_madrugada or es_hora_valle else 13.0)) * 60
        if clima_actual == "Lluvioso 🌧️":
            tiempo_actual += distancia_total * 2.0
        diferencia = tiempo_actual - tiempo_base_valle
        
        m1, m2, m3 = st.columns(3)
        m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
        m2.metric("⏱️ Tiempo Bici", formatear_tiempo(tiempo_actual))
        m3.metric("🚴‍♂️ Esfuerzo", "Extremo ⛈️" if clima_actual == "Lluvioso 🌧️" else ("Alto 🏔️" if distancia_total > 5 else "Moderado 😌"))
        
        if clima_actual == "Lluvioso 🌧️":
            st.warning(f"🌧️ Lluvia genera un ajuste de **{int(max(1, diferencia))} min** por precaución.")
        else:
            st.info("🚴‍♂️ Sin afectación por congestión vehicular de autos.")
            
    else: # A pie
        tiempo_actual = (distancia_total / (4.0 if es_madrugada else 4.5)) * 60
        if clima_actual == "Lluvioso 🌧️":
            tiempo_actual += distancia_total * 3.0
            
        m1, m2 = st.columns(2)
        m1.metric("📏 Distancia", f"{round(distancia_total, 1)} km")
        m2.metric("⏱️ Caminando", formatear_tiempo(tiempo_actual))
        if clima_actual == "Lluvioso 🌧️":
            st.warning("🌧️ Caminar bajo lluvia reduce ligeramente el paso peatonal.")


# Arbol de Desiciones
st.markdown("---")
st.subheader("🤖 Predicción de Retrasos")

if st.session_state.ruta_calculada and st.session_state.distancia_total > 0:
    st.info(f"💡 **Ruta activa:** {round(st.session_state.distancia_total, 1)} km en **{st.session_state.transporte_elegido}** a las **{hora_salida}:00 hrs**.")

    if st.button("🔮 Ejecutar Predicción", key="btn_ml"):
        try:
            df_ml = pd.read_csv('dataset_transporte_bogota.csv')
            df_encoded = pd.get_dummies(df_ml, columns=['transporte'], drop_first=True)
            X = df_encoded.drop(columns=['retraso_alto'])
            y = df_encoded['retraso_alto']
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            clf = DecisionTreeClassifier(max_depth=3, random_state=42)
            clf.fit(X_train, y_train)

            # Regal excepción bicileta y a pie
            if es_madrugada:
                prediccion = 0
            elif transporte in ["🚲 Bicicleta", "🚶‍♂️ A pie"] and clima_actual == "Soleado / Normal":
                prediccion = 0
            elif es_hora_valle and transporte == "🚌 TransMilenio":
                prediccion = 0
            elif es_hora_valle and clima_actual == "Soleado / Normal":
                prediccion = 0
            elif es_hora_pico and clima_actual == "Lluvioso 🌧️" and transporte not in ["🚲 Bicicleta", "🚶‍♂️ A pie"]:
                prediccion = 1
            else:
                hp_val = 1 if es_hora_pico else 0
                cl_val = 1 if clima_actual == "Lluvioso 🌧️" else 0
                
                transp_actual = st.session_state.transporte_elegido
                transp_limpio = transp_actual.split(" ")[1] if " " in transp_actual else transp_actual
                
                sample_dict = {col: 0 for col in X.columns}
                sample_dict['distancia_km'] = st.session_state.distancia_total
                sample_dict['hora_pico'] = hp_val
                sample_dict['clima_lluvioso'] = cl_val
                
                transp_col = f'transporte_{transp_limpio}'
                if transp_col in sample_dict:
                    sample_dict[transp_col] = 1
                    
                sample_df = pd.DataFrame([sample_dict])
                prediccion = clf.predict(sample_df)[0]
            
            # Mostrar resultado sincronizado
            if prediccion == 1:
                st.error("⚠️ **Resultado del Árbol de Decisión:** Alta probabilidad de **RETRASO ALTO** para tu trayecto debido a saturación crítica.")
            else:
                st.success("✅ **Resultado del Árbol de Decisión:** Se predice un viaje **FLUIDO** sin retrasos significativos.")
                
            with st.expander("Ver reglas de decisión"):
                reglas_texto = export_text(clf, feature_names=list(X.columns))
                st.text(reglas_texto)
                
        except Exception as e:
            st.error("⚠️ Error al ejecutar el modelo. Detalle: " + str(e))
else:
    st.info("👆 Primero calcula un recorrido haciendo clic en **'Calcular Recorrido Inteligente'** para desbloquear el análisis de Machine Learning.")