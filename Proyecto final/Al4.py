import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Matriz por regla de Cramer")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Matriz por regla de Cramer", font=("Garamond", 20, "bold"),  bg= "#2B572C", fg="#9ACD32")
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
La regla de Cramer es un método que utiliza determinantes para obtener las distintas soluciones de un sistema de ecuaciones lineales. Según sea el sistema se pueden aplicar el mismo método de dos formas distntintas.

Puede utilizarse cuando el determinante de la matriz A es distinto de cero, ya que las soluciones se obtienen dividiendo un determinante (ya veremos cuál) entre el determinante de la matriz A.

Si el determinante de la matriz A es cero no se podría utilizar este método, ya que dividir entre cero es imposible por la propia definición de la división, vamos que entre cero no se puede dividir.

Es importante destacar que este método de resolución de sistemas de ecuaciones lineales se debe utilizar una vez que se ha discutido el sistema para ver el número de soluciones de este y así poder aplicar el método apropiado.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 11), wraplength=552, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.motyscience.com/bachillerato/2o-bachillerato/matematicas-ii-2o-bach/regla-de-cramer-resolucion-de-sistemas/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()



