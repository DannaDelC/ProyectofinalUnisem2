import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Combinaciones")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Combinaciones", font=("Garamond", 20, "bold"), bg="#0B1550", fg='#17becf')
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Se refiere a la selección de elementos sin considerar el orden. Es una forma de contar o enumerar conjuntos sin orden, que son conjuntos donde el orden de los elementos no importa. En matemáticas, las combinaciones se utilizan en el estudio de la probabilidad, la estadística y la combinatoria. Tienen varias propiedades importantes:

1. Argumentos Enteros No Negativos
2. Propiedad de Simetría
3. Propiedad de Adición
4. Propiedad Multiplicativa
5. Teorema Binomial
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 12), wraplength=552, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.ck12.org/flexi/es/grado-6/combinaciones/explica-las-propiedades-de-las-combinaciones/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()