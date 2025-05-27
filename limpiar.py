import pandas as pd
from unidecode import unidecode
df = pd.read_csv("notas_estudiantes_sucio.csv")

#ver las primeras filas
print(df.head())
df_nuevo = df.copy()
#eliminar acentos
df_nuevo["Carrera"]=df_nuevo["Carrera"].apply(lambda X:unidecode(X.strip().title())if isinstance(X, str)else X)
#eliminar filas con nombres o carreras vacios

df_nuevo = df_nuevo.dropna(subset=["Nombre","Carrera"])

#eliminar duplicados
df_nuevo=df_nuevo.drop_duplicates()

#rellenar valores faltantes en edad con la media
df_nuevo["Edad"] = df_nuevo["Edad"].fillna(df_nuevo["Edad"].mean())

#cambiar el tipo de dato
df_nuevo["Edad"] = df_nuevo ["Edad"].astype(int)

#estandarizar nombres
df_nuevo["Nombre"]=df_nuevo["Nombre"].str.capitalize()
df_nuevo["Carrera"]=df_nuevo["Carrera"].str.capitalize()

#eliminar filas con datos faltantes
df_nuevo = df_nuevo.dropna(subset=["Nota1","Nota2","Nota3"])
df_nuevo["Promedio"] = df_nuevo[["Nota1","Nota2","Nota3"]].mean(axis=1)

#crea columna con promedio de notas
df_nuevo ["Promedio"]
df_nuevo[["Nota1","Nota2","Nota3"]].mean(axis=1)
#clasificacion de desempeño
def clasificar(prom):
    if prom>=4.5:
        return "Excelente"
    elif prom>=3.5:
        return "Bueno"
    elif prom>=3.0:
        return "Regular"
    else:
        return "bajo"
df_nuevo["Desempeño"] = df_nuevo["Promedio"].apply(clasificar)

#descargar nuevo archivo
df_nuevo.to_csv("notaslimpias.csv",index=False)
print (df_nuevo)