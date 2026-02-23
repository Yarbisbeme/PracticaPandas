import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'Nombre': ['Ana', 'Luis', 'Maria', 'Carlos', 'Jose', 'Elena', 'Pedro', 'Sofia', 'Miguel', 'Laura'],
    'Ventas': [45,50,55,60,48,52,47,63,58,54]
}

df = pd.DataFrame(datos);
print("==================================================================")

def clasificar_ventas(venta):
    if venta >= 55: return "Alto rendimiento";
    elif 50 <= venta <= 54: return "Rendimiento medio";
    else: return "Bajo rendimiento";

df["Clasificación"] = df["Ventas"].apply(clasificar_ventas);
porcentajes = df["Clasificación"].value_counts(normalize=True) * 100

print("\n--- PORCENTAJE POR CLASIFICACIÓN ---")
print(porcentajes.map("{:.2f}%".format)) # Formatea para ver el símbolo %

print("\n--- TABLA DE VENTAS Y RENDIMIENTO ---")
print(df);
print("\n")

# Cálculo de estadísticas
media = df["Ventas"].mean();
mediana = df["Ventas"].median();
moda = df["Ventas"].mode()[0];
desviacion = df["Ventas"].std();
maximo = df["Ventas"].max();
minimo = df["Ventas"].min();

print("--- Parte 2 ---")
print("Media de ventas:", media);
print("Mediana de ventas:", mediana);
print("Moda de ventas:", moda);
print("Desviación estándar de ventas:", desviacion);
print("Valor máximo de ventas:", maximo);
print("Valor mínimo de ventas:", minimo);

# Visualización de datos
porcentajes.plot(kind='pie', autopct='%1.2f%%', color=['blue', 'orange', 'green']);
plt.title("Distribución de Clasificación de Ventas");
plt.ylabel(""); 
plt.show();

df.plot(x='Nombre', y='Ventas', kind='bar', color='skyblue');
plt.title("Ventas por Vendedor");
plt.xlabel("Nombre del Vendedor");
plt.ylabel("Ventas");
plt.xticks(rotation=45);
plt.tight_layout();
plt.show();
