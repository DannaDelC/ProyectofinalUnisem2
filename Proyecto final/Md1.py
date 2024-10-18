import tkinter as tk          
from tkinter import ttk           

root = tk.Tk()
root.title("Permutaciones")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(row=0, column=0,sticky=(tk.W, tk.E, tk.N, tk.S))

titulo = tk.Label(frame, text="Permutaciones", font=("Garamond", 20, "bold"), bg="#0B1550", fg='#17becf')
titulo.grid(row=0, column=0, sticky=tk.N, pady=(0, 10))

parrafo= """
Las permutaciones son diferentes formas de ordenar objetos en un orden determinado. También se pueden expresar como la reorganización de elementos en un orden lineal de un conjunto ya ordenado. El símbolo nortePAGa se utiliza para indicar el número de permutaciones de n objetos distintos, tomados de r en r. Bloquea horarios de autobuses, trenes o vuelos, asignación de códigos postales y números de teléfono. Estas son algunas situaciones en las que se utilizan permutaciones. Permutar significa posicionar. Aprendamos más sobre las permutaciones junto con algunos ejemplos resueltos.

Una permutación es una disposición ordenada de resultados y una combinación ordenada. Por ejemplo, hay 5 sillas y se van a sentar 3 personas. Tenemos 5 formas de sentar a la primera persona; 4 formas de sentar a la siguiente persona y 3 formas de sentar a la tercera persona. Por lo tanto, para encontrar la cantidad de formas de organizar 3 personas en 5 sillas, multiplicamos las opciones disponibles. Lo hacemos de 5 × 4 × 3 formas. Es decir, se puede hacer de 60 formas. Observe que 5 × 4 × 3 se puede escribir como (5!) / (2!) (o) (5!) / (5 - 3)!. Generalizando esto, obtenemos n opciones para llenar la primera silla, n-1 opciones para llenar la segunda y n-2 opciones para llenar la tercera silla. Por lo tanto, el número total de permutaciones (disposiciones) de r personas en n sillas se puede expresar como: n P r = n! / (n - r)!.
"""

parrafo = tk.Label(frame, text=parrafo, font=("Helvetica", 9), wraplength=552, justify="left" )
parrafo.grid(column=0, row=1, sticky=tk.W,)

enlace = tk.Label(frame, text="Más información aquí", fg="blue", cursor="hand2")
enlace.grid(column=0, row=2, sticky=tk.W, pady=(0, 10))

def abrir_url(event):
    import webbrowser
    webbrowser.open_new("https://www.cuemath.com/data/permutations/")
enlace.bind("<Button-1>", abrir_url)

root.mainloop()