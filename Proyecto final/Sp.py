import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Sympy")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Sympy", font=("Garamond", 20, "bold"), bg="#242424", fg='Orange' )
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Sympy permite hacer operaciones analíticas o con símbolos en lugar de con valores numéricos Al igual que en Python existen varios tipos de datos numéricos como enteros (int), decimales (float) o booleanos (bool:True, False, etc.), Sympy posee tres tipos de datos propios: Real, Rational e Integer, es decir, números reales, racionales y enteros. Estoquiere decir que Rational(1,2) representa 1/2, Rational(5,2) a 5/2, etc. en lugar de 0.5 o 2.5.

También existen algunas constantes especiales, como el número e o π, si embargo éstos se tratan con símbolos y no tienen un valor númerico determinado. Eso quiere decir que no se puede obtener un valor numérico de una operación usando el pi de Sympy, como (1+pi), como lo haríamos con el de Numpy, que es numérico:

Como se ve, sin embargo, se puede usar el método evalf() para evaluar una expresión para tener un valor en punto flotante (float).
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=560, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://research.iac.es/sieinvens/python-course/sympy.html")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()