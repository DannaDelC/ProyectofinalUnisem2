import numpy as np
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
import matplotlib.pyplot as plt

# Funciones matemáticas
def inversa_matriz(matriz):
    try:
        inversa = np.linalg.inv(matriz)
        inversa_frac = np.vectorize(lambda x: Fraction(x).limit_denominator())(inversa)
        return inversa_frac
    except np.linalg.LinAlgError:
        return None

def multiplicar_matrices(matriz1, matriz2):
    resultado = np.dot(matriz1, matriz2)
    resultado_frac = np.vectorize(lambda x: Fraction(x).limit_denominator())(resultado)
    return resultado_frac

def resolver_ecuaciones(matriz_a, matriz_b, metodo='gauss'):
    if metodo == 'gauss':
        return gauss_jordan(matriz_a, matriz_b)
    elif metodo == 'cramer':
        return regla_de_cramer(matriz_a, matriz_b)
    else:
        raise ValueError("Método no reconocido. Usa 'gauss' o 'cramer'.")

def gauss_jordan(matriz_a, matriz_b):
    augmented = np.hstack((matriz_a, matriz_b))
    filas, columnas = augmented.shape
    pasos = f"Matriz aumentada:\n{mostrar_matriz(augmented)}\n\n"

    for i in range(filas):
        pivot = augmented[i, i]
        if pivot == 0:
            for k in range(i + 1, filas):
                if augmented[k, i] != 0:
                    augmented[[i, k]] = augmented[[k, i]]
                    pasos += f"Permutación de filas {i+1} y {k+1}:\n{mostrar_matriz(augmented)}\n"
                    pivot = augmented[i, i]
                    break
            else:
                messagebox.showerror("Error", "La matriz no tiene solución única.")
                return

        augmented[i] = augmented[i] / pivot
        pasos += f"Dividir fila {i+1} entre {pivot}:\n{mostrar_matriz(augmented)}\n"

        for j in range(filas):
            if j != i:
                factor = augmented[j, i]
                augmented[j] -= factor * augmented[i]
                pasos += f"Restar fila {i+1} multiplicada por {factor} de la fila {j+1}:\n{mostrar_matriz(augmented)}\n"

    soluciones = augmented[:, -1]
    pasos += f"Solución:\n{mostrar_matriz(soluciones)}"
    return pasos, soluciones

def regla_de_cramer(matriz_a, matriz_b):
    det_a = np.linalg.det(matriz_a)
    det_a_frac = Fraction(det_a).limit_denominator()
    pasos = f"Determinante de la matriz A: {det_a_frac}\n\n"
    
    if det_a == 0:
        return "Sin solución o soluciones infinitas", []

    n = matriz_a.shape[0]
    soluciones = []
    
    for i in range(n):
        matriz_temp = matriz_a.copy()
        matriz_temp[:, i] = matriz_b.flatten()
        det_temp = np.linalg.det(matriz_temp)
        det_temp_frac = Fraction(det_temp).limit_denominator()
        pasos += f"Matriz modificada para X{i+1}:\n{mostrar_matriz(matriz_temp)}\n"
        pasos += f"Determinante de la matriz modificada para X{i+1}: {det_temp_frac}\n"
        soluciones.append(det_temp_frac / det_a_frac)
    
    soluciones_frac = [Fraction(sol).limit_denominator() for sol in soluciones]
    pasos += f"Solución: {soluciones_frac}"
    return pasos, soluciones_frac

def mostrar_matriz(matriz):
    if matriz.ndim == 1:
        return "  ".join([str(Fraction(val).limit_denominator()) for val in matriz])
    filas = []
    for fila in matriz:
        filas.append("  ".join([str(Fraction(val).limit_denominator()) for val in fila]))
    return "\n".join(filas)

def graficar_ecuaciones(matriz_a, matriz_b):
    n = matriz_a.shape[0]
    x = np.linspace(-10, 10, 400)

    plt.figure(figsize=(8, 6))
    
    for i in range(n):
        if matriz_a[i][1] != 0:
            m = -matriz_a[i][0] / matriz_a[i][1]
            b = matriz_b[i][0] / matriz_a[i][1]
            y = m * x + b
            plt.plot(x, y, label=f'Ecuación {i+1}')

    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.title("Gráfica de las Ecuaciones")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()

# Interfaz gráfica
def ingresar_matriz():
    n = int(entry_n.get())
    matriz_window = tk.Toplevel(root)
    matriz_window.title(f"Ingresar matriz {n}x{n}")
    matriz_window.configure(bg="#f5f5f5")

    global entries_matriz1, entries_matriz2, entries_resultados
    entries_matriz1 = []
    entries_matriz2 = []
    entries_resultados = []

    frame_matriz_a = tk.Frame(matriz_window, bg="#f5f5f5", padx=10, pady=10)
    frame_matriz_b = tk.Frame(matriz_window, bg="#f5f5f5", padx=10, pady=10)
    frame_resultados = tk.Frame(matriz_window, bg="#f5f5f5", padx=10, pady=10)
    frame_botones = tk.Frame(matriz_window, bg="#f5f5f5", padx=10, pady=10)

    frame_matriz_a.grid(row=0, column=0, padx=10, pady=10)
    frame_matriz_b.grid(row=0, column=1, padx=10, pady=10)
    frame_resultados.grid(row=0, column=2, padx=10, pady=10)
    frame_botones.grid(row=1, column=0, columnspan=3, pady=20)

    tk.Label(frame_matriz_a, text="Matriz A", bg="#f5f5f5", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=n)
    for i in range(n):
        fila_entries = []
        for j in range(n):
            entry = tk.Entry(frame_matriz_a, width=5)
            entry.grid(row=i+1, column=j)
            fila_entries.append(entry)
        entries_matriz1.append(fila_entries)

    tk.Label(frame_matriz_b, text="Matriz B (para multiplicación)", bg="#f5f5f5", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=n)
    for i in range(n):
        fila_entries = []
        for j in range(n):
            entry = tk.Entry(frame_matriz_b, width=5)
            entry.grid(row=i+1, column=j)
            fila_entries.append(entry)
        entries_matriz2.append(fila_entries)

    tk.Label(frame_resultados, text="Resultados B (para Gauss/Cramer)", bg="#f5f5f5", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=n)
    for i in range(n):
        entry = tk.Entry(frame_resultados, width=5)
        entry.grid(row=i+1, column=0)
        entries_resultados.append(entry)

    boton_color = "#4CAF50"
    texto_boton = "#FFFFFF"

    tk.Button(frame_botones, text="Inversa de la matriz A", bg=boton_color, fg=texto_boton, command=lambda: calcular_inversa(n)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame_botones, text="Multiplicar matrices", bg=boton_color, fg=texto_boton, command=lambda: calcular_multiplicacion(n)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_botones, text="Resolver ecuaciones (Gauss)", bg=boton_color, fg=texto_boton, command=lambda: calcular_ecuaciones(n, metodo='gauss')).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(frame_botones, text="Resolver ecuaciones (Cramer)", bg=boton_color, fg=texto_boton, command=lambda: calcular_ecuaciones(n, metodo='cramer')).grid(row=1, column=0, columnspan=3)

    tk.Button(frame_botones, text="Regresar", bg="#f44336", fg="#FFFFFF", command=matriz_window.destroy).grid(row=2, column=0, columnspan=3, pady=10)

def calcular_inversa(n):
    matriz_a = np.array([[float(entries_matriz1[i][j].get()) for j in range(n)] for i in range(n)])
    inversa = inversa_matriz(matriz_a)
    if inversa is None:
        messagebox.showerror("Error", "La matriz no es invertible.")
    else:
        messagebox.showinfo("Inversa de la Matriz", f"Inversa:\n{mostrar_matriz(inversa)}")

def calcular_multiplicacion(n):
    matriz_a = np.array([[float(entries_matriz1[i][j].get()) for j in range(n)] for i in range(n)])
    matriz_b = np.array([[float(entries_matriz2[i][j].get()) for j in range(n)] for i in range(n)])
    resultado = multiplicar_matrices(matriz_a, matriz_b)
    messagebox.showinfo("Resultado de la Multiplicación", f"Matriz resultante:\n{mostrar_matriz(resultado)}")

def calcular_ecuaciones(n, metodo='gauss'):
    matriz_a = np.array([[float(entries_matriz1[i][j].get()) for j in range(n)] for i in range(n)])
    matriz_b = np.array([[float(entries_resultados[i].get())] for i in range(n)])
    pasos, soluciones = resolver_ecuaciones(matriz_a, matriz_b, metodo)
    
    messagebox.showinfo("Resultado de la Resolución", f"Pasos:\n{pasos}")
    
    respuesta = messagebox.askyesno("Mostrar Gráfica", "¿Desea ver la gráfica de las ecuaciones?")
    if respuesta:
        graficar_ecuaciones(matriz_a, matriz_b)

root = tk.Tk()
root.title("Calculadora de Matrices")
root.geometry("600x400")
root.configure(bg="#282C34")

tk.Label(root, text="Tamaño de la matriz (n):", bg="#282C34", fg="#FFFFFF", font=("Arial", 12, "bold")).pack(pady=10)
entry_n = tk.Entry(root)
entry_n.pack(pady=5)
tk.Button(root, text="Ingresar Matrices", bg="#4CAF50", fg="#FFFFFF", command=ingresar_matriz).pack(pady=20)

root.mainloop()
