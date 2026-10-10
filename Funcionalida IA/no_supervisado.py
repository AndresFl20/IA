import pandas as pd
from sklearn.cluster import KMeans

# Cargar el dataset
df = pd.read_csv('dataset_transporte_bogota.csv')

# Seleccionar las variables numéricas para el análisis de agrupamiento
X = df[['distancia_km', 'hora_pico', 'clima_lluvioso']]

# Aplicar el algoritmo no supervisado
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X)

# Mostrar los primeros resultados en consola
print("¡Modelo no supervisado ejecutado con éxito!")
print(df.head(10))

# Guardar archivo CSV
df.to_csv('dataset_transporte_bogota_clusters.csv', index=False)