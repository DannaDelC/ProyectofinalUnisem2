import tkinter as tk 
import subprocess import subproces

def run_AL():
    subprocess.run(['python', 'AL.py'])

def run_MD():
    subprocess.run(['python', 'MD.py'])

def show_algebra():
    algebra_window = tk.Toplevel(root)
    algebra_window.title("Álgebra Lineal")
    tk.Label(algebra_window, text="Álgebra Lineal", font=("Arial", 30, "bold"), bg= "#F0FFFF").pack(pady=20) 
    tk.Label(algebra_window, text="Definición de matrices", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(algebra_window, text="Una matriz es un arreglo bidimensional de números.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algebra_window, text="Matriz inversa", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(algebra_window, text="La matriz inversa de una matriz A es otra matriz que, cuando se multiplica por A, da la matriz identidad.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algebra_window, text="Matriz por Gauss-Jordan", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(algebra_window, text="El método de Gauss-Jordan es un algoritmo para encontrar la matriz inversa.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algebra_window, text="Matriz por regla de Cramer", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(algebra_window, text="La regla de Cramer es un método para resolver sistemas de ecuaciones lineales usando determinantes.", font=("Arial", 12)).pack(pady=5)
    tk.Button(algebra_window, text="Calculadora de matrices", font=("Arial", 12, "bold"), command=run_AL).pack(pady=20)

       

def show_discrete_math():
    discrete_window = tk.Toplevel(root)
    discrete_window.title("Matemáticas Discreta")
    tk.Label(discrete_window, text="Permutaciones y Combinaciones", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(discrete_window, text="Las permutaciones son arreglos ordenados de elementos, mientras que las combinaciones son selecciones de elementos sin importar el orden.", font=("Arial", 12)).pack(pady=5)
    tk.Button(discrete_window, text="Calculadora de permutaciones y combinaciones", font=("Arial", 12, "bold"), command=run_MD).pack(pady=20)


def show_algorithms():
    algorithms_window = tk.Toplevel(root)
    algorithms_window.title("Algoritmo")
    tk.Label(algorithms_window, text="Librerías en Python", font=("Arial", 14, "bold"), bg="#808080").pack(pady=10)
    tk.Label(algorithms_window, text="Tkinter: Biblioteca para crear interfaces gráficas.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algorithms_window, text="Numpy: Biblioteca para cálculos numéricos.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algorithms_window, text="Sympy: Biblioteca para matemáticas simbólicas.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algorithms_window, text="Matplotlib: Biblioteca para crear gráficos.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algorithms_window, text="Scipy: Biblioteca para cálculos científicos.", font=("Arial", 12)).pack(pady=5)
    tk.Label(algorithms_window, text="Pillow: Biblioteca para manipulación de imágenes.", font=("Arial", 12)).pack(pady=5)
    

def show_credits():
    credits_window = tk.Toplevel(root)
    credits_window.title("Créditos")
    tk.Label(credits_window, text="Integrantes del Proyecto", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(credits_window, text="Mercedes Vásquez", font=("Arial", 12)).pack(pady=5)
    tk.Label(credits_window, text="Nombre 2", font=("Arial", 12)).pack(pady=5)
    tk.Label(credits_window, text="Nombre 3", font=("Arial", 12)).pack(pady=5)
    tk.Label(credits_window, text="Nombre 3", font=("Arial", 12)).pack(pady=5)
    tk.Label(credits_window, text="Nombre 3", font=("Arial", 12)).pack(pady=5)


root = tk.Tk()
root.title("Menú Principal")

frame = tk.Frame(root, bg="#F0FFFF")
frame.pack(pady=20, padx=20)



tk.Label(frame, text="Bienvenidos a nuestro Proyecto", font=("Arial", 20, "bold"), bg="#F0FFFF").pack(pady=10)

tk.Button(frame, text="Álgebra Lineal", font=("Arial", 14, "bold"), bg="#3CB371", command=show_algebra).pack(pady=5)
tk.Button(frame, text="Mate Discreta", font=("Arial", 14, "bold"), bg="#66CDAA", command=show_discrete_math).pack(pady=5)
tk.Button(frame, text="Algoritmos", font=("Arial", 14, "bold"), bg="#98FB98", command=show_algorithms).pack(pady=5)
tk.Button(frame, text="Créditos", font=("Arial", 14, "bold"), bg="#F5FFFA", command=show_credits).pack(pady=5)

root.mainloop()


