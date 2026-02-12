import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'Nombre': 
        ['Juan', 'María', 'Pedro', 'Ana', 'Julia', 'Abigail', 'Gertrudis', 'Sofia', 'Carlos', 'Lucía'],
    'Edad': 
        [28, 34, 22, 19, 25, 30, 27, 26, 31, 24],
    'Nota': 
        [85, 92, 78, 88, 90, 95, 80, 82, 91, 87],
    'Ciudad': 
        ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid', 'Barcelona']
}

df = pd.DataFrame(datos);
print("==================================================================")
avg = df["Edad"].mean();
print("La edad promedio es:", avg);
MaxEdad = df["Edad"].max();
print("La edad máxima es:", MaxEdad);
MinEdad = df["Edad"].min();
print("La edad mínima es:", MinEdad);
max = df.loc[df["Edad"].idxmax()];
print("Los datos de la persona con la mayor edad es:", max["Nombre"], max["Edad"], max["Ciudad"]);
print(" ");

print("==================================================================")
AvgNota = df["Nota"].mean();
print("La nota promedio es:", AvgNota);
MinNota = df["Nota"].min();
print("La nota mínima es:", MinNota);
MaxNota = df["Nota"].max();
print("La nota máxima es:", MaxNota);
max = df.loc[df["Nota"].idxmax()];
print("Los datos de la persona con la mayor nota es:", max["Nombre"], max["Nota"], max["Ciudad"]);
print(" ");

print("==================================================================")
df_agrupado = df.groupby("Ciudad")["Edad"].mean();
print("Edad promedio por ciudad:");
print(" ");
print(df_agrupado);
print(" ");

print("==================================================================")
df_agrupado_Ciudad_Nota = df.groupby("Ciudad")["Nota"].mean();
print("Nota promedio por ciudad:");
print(" ");
print(df_agrupado_Ciudad_Nota);

df_agrupado_Ciudad_Nota.plot(kind="bar");
plt.title("Nota promedio por ciudad");
plt.xlabel("Ciudad");
plt.ylabel("Nota");
plt.show();

df_agrupado.plot(kind="bar");
plt.title("Edad promedio por ciudad");
plt.xlabel("Ciudad");
plt.ylabel("Edad");
plt.show();

df.plot(x="Nombre", y="Edad", kind="bar");
plt.title("Edad de las personas por nombre");
plt.xlabel("Nombre");
plt.ylabel("Edad");
plt.show();


