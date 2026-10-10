from datetime import datetime

# GESTOR DE HOJA DE TIEMPOS EMPLEANDO CLOCKIFY
#libreria scikit-learn

# Fecha actual de corte simulada
hoy = datetime.strptime("2026-09-12", "%Y-%m-%d")

# Lista de Casos
casos = [
    {
        "id": "CASO-0055424",
        "horas_asignadas": 18.0,
        "horas_gastadas": 14.0,
        "fecha_limite": datetime.strptime("2026-09-03", "%Y-%m-%d"),
        "fecha_entrega": datetime.strptime("2026-09-03", "%Y-%m-%d"),
        "estado": "Cerrado"
    },
    {
        "id": "CASO-0055496",
        "horas_asignadas": 12.0,
        "horas_gastadas": 18.0,
        "fecha_limite": datetime.strptime("2026-09-07", "%Y-%m-%d"),
        "fecha_entrega": datetime.strptime("2026-09-08", "%Y-%m-%d"),
        "estado": "Cerrado"
    },
    {
        "id": "CASO-0055539",
        "horas_asignadas": 10.0,
        "horas_gastadas": 10.0,
        "fecha_limite": datetime.strptime("2026-09-09", "%Y-%m-%d"),
        "fecha_entrega": datetime.strptime("2026-09-10", "%Y-%m-%d"),
        "estado": "Cerrado"
    },
    {
        "id": "CASO-0055560",
        "horas_asignadas": 10.0,
        "horas_gastadas": 5.0,
        "fecha_limite": datetime.strptime("2026-09-11", "%Y-%m-%d"),
        "fecha_entrega": None,
        "estado": "En Proceso"
    },
    {
        "id": "CASO-0055582",
        "horas_asignadas": 6.0,
        "horas_gastadas": 2.0,
        "fecha_limite": datetime.strptime("2026-09-14", "%Y-%m-%d"),
        "fecha_entrega": None,
        "estado": "En Proceso"
    }
]

print("==================================================")
print("      REPORTE DE INDICADORES Y HOJA DE TIEMPOS     ")
print("==================================================\n")

total_asignadas = 0.0
total_gastadas = 0.0
casos_exitosos_total = 0
casos_con_retraso = 0
casos_activos_a_tiempo = 0
casos_activos_vencidos = 0

for caso in casos:
    print(f"# Caso: {caso['id']} [{caso['estado']}]")
    
    total_asignadas += caso["horas_asignadas"]
    total_gastadas += caso["horas_gastadas"]
    
    # Si el caso sigue abierto (En Proceso)
    if caso["estado"] == "En Proceso":
        dias_restantes = (caso["fecha_limite"] - hoy).days
        horas_restantes_presupuesto = caso["horas_asignadas"] - caso["horas_gastadas"]
        
        print(f"• Horas Asignadas: {caso['horas_asignadas']} hrs | Horas Consumidas hasta hoy: {caso['horas_gastadas']} hrs")
        print(f"👉 Margen de Horas restantes: {horas_restantes_presupuesto} hrs")
        print(f"• Fecha Límite: {caso['fecha_limite'].strftime('%Y-%m-%d')}")
        
        if dias_restantes > 0:
            casos_activos_a_tiempo += 1
            horas_disponibles_segun_dias = dias_restantes * 8.0
            print(f"ℹ️  Estado: Activo a tiempo (Faltan {dias_restantes} días). Capacidad estimada: {horas_disponibles_segun_dias} hrs.\n")
        else:
            casos_activos_vencidos += 1
            print(f"❌ Alerta Crítica: El caso está abierto, pero YA VENCIÓ hace {abs(dias_restantes)} días o vence hoy.\n")
            
    else:
        # Casos ya cerrados (Histórico)
        diferencia_horas = caso["horas_asignadas"] - caso["horas_gastadas"]
        diferencia_dias = (caso["fecha_limite"] - caso["fecha_entrega"]).days
        
        print(f"• Horas Asignadas: {caso['horas_asignadas']} hrs | Horas Gastadas: {caso['horas_gastadas']} hrs")
        print(f"• Fecha Límite: {caso['fecha_limite'].strftime('%Y-%m-%d')} | Fecha Entrega: {caso['fecha_entrega'].strftime('%Y-%m-%d')}")
        
        cumplio_horas = diferencia_horas >= 0
        cumplio_tiempo = diferencia_dias >= 0
        
        if cumplio_horas and cumplio_tiempo:
            casos_exitosos_total += 1
            print(f"✅ Resultado: Caso 100% Exitoso (+{diferencia_horas} hrs a favor, entregado {diferencia_dias} días antes).\n")
        elif not cumplio_horas and cumplio_tiempo:
            casos_con_retraso += 1
            print(f"⚠️ Resultado: Entregado a tiempo en fecha, pero SE PASÓ DE HORAS ({abs(diferencia_horas)} hrs de exceso).\n")
        elif cumplio_horas and not cumplio_tiempo:
            casos_con_retraso += 1
            print(f"⚠️ Resultado: No gastó más horas, pero SE ENTREGÓ TARDE ({abs(diferencia_dias)} días de retraso).\n")
        else:
            casos_con_retraso += 1
            print(f"❌ Resultado: Desfase Total (Se pasó en horas y se entregó tarde).\n")
            
    print("-" * 50)

# 3. Indicador Total / Dashboard General
efectividad_global = (total_asignadas / total_gastadas) * 100 if total_gastadas > 0 else 0
total_evaluados = len(casos)

print("\n==================================================")
print("            INDICADOR GLOBAL DE GESTIÓN           ")
print("==================================================\n")
print(f"Total de Registros en la Base: {total_evaluados}")
print(f"  - Casos Cerrados Exitosos (En tiempo y presupuesto): {casos_exitosos_total}")
print(f"  - Casos Cerrados con Algún Desfase (Horas/Tiempo): {casos_con_retraso}")
print(f"  - Casos Activos a Tiempo: {casos_activos_a_tiempo}")
print(f"  - Casos Activos Vencidos / Críticos: {casos_activos_vencidos}")
print(f"--------------------------------------------------\n")
print(f"Horas Totales Asignadas: {total_asignadas} hrs")
print(f"Horas Totales Registradas: {total_gastadas} hrs")
print(f"Efectividad Total de Horas: {efectividad_global:.2f}%\n")