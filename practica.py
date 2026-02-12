import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [28, 34, 22, 19],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(datos)

avg = df["Edad"].mean()
print("La edad promedio es:", avg)

MaxEdad = df["Edad"].max()
print("La edad máxima es:", MaxEdad)

max = df.loc[df["Edad"].idxmax()]
print("La persona con la edad máxima es:", max["Nombre"], max["Edad"], max["Ciudad"])

df.plot(x="Nombre", y="Edad", kind="bar");
plt.title("Edad de las personas")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

