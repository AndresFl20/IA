import pandas as pd
import numpy as np

# Semilla para que los datos sean siempre los mismos y organizados
np.random.seed(42)
n_muestras = 500

# Creamos datos simulados basados en el sur de Bogotá 
# Distancias entre 1 y 12 km en base a la actividad anterior 
distancias = np.random.uniform(1.0, 12.0, n_muestras) 
transportes = np.random.choice(['TransMilenio', 'Taxi/Uber', 'Moto', 'Bicicleta', 'A pie'], n_muestras)
hora_pico = np.random.choice([0, 1], n_muestras, p=[0.6, 0.4])
clima_lluvioso = np.random.choice([0, 1], n_muestras, p=[0.7, 0.3])

# Lógica inteligente para definir si el viaje tuvo retraso 
retraso = []
for d, t, hp, cl in zip(distancias, transportes, hora_pico, clima_lluvioso):
    puntaje = d * 1.5 + (hp * 3) + (cl * 4)
    if t == 'Bicicleta' and cl == 1:
        puntaje += 5
    if t == 'TransMilenio' and hp == 1:
        puntaje += 3
        
    # Si no es hora pico (madrugada o valle) y las vías están libres, 
    # evitamos que una lluvia ligera dispare un retraso absurdo en vehículo motorizado
    if hp == 0 and t in ['Taxi/Uber', 'Moto'] and cl == 1:
        puntaje -= 3
        
    # Si el puntaje pasa de 12 
    # se marca como Retraso Alto (1)
    retraso.append(1 if puntaje > 12 else 0)

# Construimos la tabla
df_dataset = pd.DataFrame({
    'distancia_km': np.round(distancias, 2),
    'transporte': transportes,
    'hora_pico': hora_pico,
    'clima_lluvioso': clima_lluvioso,
    'retraso_alto': retraso
})

# Creación archivo CSV
df_dataset.to_csv('dataset_transporte_bogota.csv', index=False)
print("¡Listo! Archivo 'dataset_transporte_bogota.csv' generado con éxito.")