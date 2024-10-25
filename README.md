                                          Funcionamiento e Instrucciones Generales del Programa. 
Menú Principal: El programa es una interfaz gráfica de usuario (GUI) construida con Tkinter en Python, que sirve como un menú principal para acceder a 
diferentes módulos de matemáticas y algoritmos. Las funcionalidades principales del programa incluyen la ejecución de scripts para resolver problemas de 
álgebra lineal, matemáticas discretas, y el uso de diversas librerías de Python. Además, presenta una sección de créditos con los nombres de los integrantes del proyecto.

Funcionamiento del programa
1.	Menú Principal:
   o	Al iniciar el programa, se despliega una ventana con el título "Menú Principal".
   o	En esta ventana, se muestra un mensaje de bienvenida y varios botones que permiten al usuario acceder a las diferentes secciones del proyecto.
2.	Botones en el Menú Principal:
   o	Álgebra Lineal: Al presionar este botón, se abre una nueva ventana con cuatro opciones para trabajar con matrices (definición, matriz inversa,
  	método de Gauss-Jordan, y regla de Cramer). También incluye una calculadora para operaciones de matrices.
   o	Mate Discreta: Al seleccionar este botón, se abre una ventana donde se pueden ejecutar scripts relacionados con permutaciones y combinaciones.
  	 También hay una calculadora específica para estos conceptos.
   o  	Algoritmos: Este botón abre una ventana que lista varias librerías de Python (Tkinter, Numpy, Sympy, Matplotlib, Scipy, Pillow).
  	Cada botón ejecuta un script específico relacionado con la librería seleccionada.
   o	Créditos: Este botón muestra una ventana con los nombres de los integrantes del proyecto.
4.	Ejecución de Scripts:
o	Cada vez que se presiona uno de los botones dentro de las secciones "Álgebra Lineal", "Mate Discreta", o "Algoritmos", se ejecuta un script Python relacionado.
Esto se hace mediante la función subprocess.run(['python', 'nombre_del_script.py']), que corre el archivo Python correspondiente (por ejemplo, AL.py, MD.py, etc.).

Instrucciones para ejecutar el programa
1.	Pre-requisitos:
   o	Python 3.x instalado en el sistema.
   o	Tener instalados los módulos necesarios como Tkinter, Numpy, Sympy, Matplotlib, Scipy, y Pillow, dependiendo de los scripts que se vayan a ejecutar.
2.	Archivos necesarios:
   o	Los archivos Python mencionados (AL.py, MD.py, Al1.py, etc.) deben estar en el mismo directorio que el archivo principal que contiene el código de la interfaz
  	gráfica. Estos archivos deben contener las funciones o scripts específicos para realizar las operaciones matemáticas o algoritmos correspondientes.
4.	Ejecución:
   o	Guardar el código en un archivo Python, por ejemplo, menu_principal.py.
   o	Asegurarse de que los scripts Python a los que hace referencia el programa están en el mismo directorio.
   o	Ejecutar el archivo principal desde la terminal o un entorno de desarrollo integrado (IDE) utilizando el comando:
                                           python menu_principal.py
   o	Al iniciar, se abrirá la ventana del menú principal, desde donde se podrá navegar y ejecutar los distintos módulos.

Personalización de la interfaz
El programa incluye un esquema de colores con tonos pastel (#EADEE2, #6E7E71, #a9a5a2, etc.) para los botones y fondos de las ventanas.
Los textos utilizan distintas fuentes como Garamond, Arial, Georgia, y Rockwell, con diferentes estilos y tamaños para mejorar la presentación visual.


Calculadora de Matrices, Algebra Lineal. 
Este programa es una calculadora de matrices que permite realizar varias operaciones algebraicas con matrices cuadradas de tamaños hasta 4x4, entre ellas:
1.	Inversa de una Matriz.
2.	Multiplicación de dos Matrices.
3.	Resolución de sistemas de ecuaciones lineales mediante el método de Gauss-Jordan.
4.	Resolución de sistemas de ecuaciones lineales mediante la Regla de Cramer.

Funcionalidades del programa:
1.	Inversa de una matriz:
   o	El programa toma una matriz n×n ingresada por el usuario y calcula su inversa. Si la matriz no es invertible (su determinante es cero), se muestra un mensaje de error.
2.	Multiplicación de matrices:
   o	El programa permite ingresar dos matrices cuadradas n×n y realiza la multiplicación de estas matrices.
3.	Resolución de ecuaciones con Gauss-Jordan:
   o	Permite resolver sistemas de ecuaciones lineales usando el método de Gauss-Jordan. Se ingresa una matriz A de coeficientes y una matriz de resultados B (vector columna),
y el programa mostrará los pasos intermedios y el resultado de las ecuaciones.
5.	Resolución de ecuaciones con Regla de Cramer:
   o	Utiliza la regla de Cramer para resolver sistemas de ecuaciones. Similar al método de Gauss-Jordan, el usuario ingresa las matrices A y B, y el programa calculará las soluciones.
6.	Gráfica de las ecuaciones:
   o	Después de resolver un sistema de ecuaciones con Gauss-Jordan o Cramer, el programa permite graficar las rectas correspondientes a las ecuaciones del sistema.

Instrucciones para la ejecución del programa:
1.	Requisitos previos:
   o	Tener instalados los siguientes módulos de Python:
      	numpy: para operaciones matemáticas con matrices.
      	tkinter: para la interfaz gráfica de usuario (GUI).
      	matplotlib: para la visualización gráfica de las ecuaciones.
Puedes instalar las dependencias ejecutando:
                 pip install numpy matplotlib
2.	Ejecución:
   o	Ejecuta el archivo Python que contiene este código. Esto abrirá una ventana gráfica donde podrás interactuar con las diferentes opciones.
3.	Interfaz gráfica:
   o	En la ventana principal:
     	Introduce el tamaño de la matriz n×n (se recomienda un máximo de 4 para evitar errores).
      	Selecciona la operación que deseas realizar: Invertir, Multiplicar, Resolver por Gauss o Resolver por Cramer.
4.	Ingreso de datos:
   o	Según la operación seleccionada, aparecerán nuevas ventanas donde se solicitan las entradas de las matrices. Llena los valores en los campos de texto correspondientes y haz clic en los botones de acción (como "Invertir Matriz", "Multiplicar Matrices", etc.).
5.	Resultados:
   o	Los resultados se mostrarán en cuadros de diálogo que indicarán el proceso o el resultado final.
   o	Para los métodos de Gauss y Cramer, se te preguntará si deseas visualizar la gráfica de las ecuaciones resueltas.

Notas adicionales:
•	El programa utiliza números racionales para mostrar los resultados en fracciones, lo que permite una mayor precisión y legibilidad en comparación con
los números decimales.
•	El fondo y los colores de los botones siguen un esquema personalizado, con tonos suaves y botones de acción destacados para facilitar la interacción.


Calculadora de Permutaciones y Combinaciones, Matemática Discreta. 
Este programa en Python utiliza la biblioteca Tkinter para ofrecer una interfaz gráfica que permite calcular permutaciones y combinaciones con y sin repetición
para valores dados de n y r. Los cálculos incluyen las permutaciones y combinaciones de n elementos tomados de r en r, permitiendo al usuario seleccionar el tipo
de cálculo y si este incluye repetición.

Funcionamiento del Programa
1.	Ingreso de Valores:
   o	El usuario ingresa los valores de n (total de elementos) y r (elementos a elegir) en los campos de entrada correspondientes.
2.	Opciones de Cálculo:
   o	Selecciona el tipo de cálculo:
      	Permutaciones: el orden importa.
      	Combinaciones: el orden no importa.
   o	Selecciona si se desea cálculo Con Repetición o Sin Repetición:
      	Con repetición: los elementos pueden repetirse en las combinaciones o permutaciones.
      	Sin repetición: cada elemento se puede usar solo una vez.
3.	Cálculo y Resultados:
   o	Al hacer clic en el botón Calcular, el programa determina si es una permutación o combinación y si incluye repetición.
   o	Si el cálculo es válido, se muestra el número total de resultados y una lista de todas las combinaciones o permutaciones en un cuadro de diálogo.
   o	En caso de error (por ejemplo, r>n en combinaciones o permutaciones sin repetición), se muestra un mensaje de error.
Instrucciones para Ejecutar el Programa
1.	Abrir el Programa: Ejecutar el script en un entorno de Python que soporte Tkinter (como IDLE o cualquier IDE de Python).
2.	Ingresar los Valores de n y r: Escribir los valores deseados en los campos correspondientes.
3.	Seleccionar Opciones: Escoger entre Permutaciones o Combinaciones y Con o Sin Repetición.
4.	Calcular: Hacer clic en el botón Calcular.
5.	Visualizar el Resultado: El programa mostrará el número total de resultados y cada combinación o permutación en una ventana emergente.

Este programa facilita el aprendizaje de combinaciones y permutaciones, mostrando tanto los resultados numéricos como las listas detalladas de opciones
para entender mejor estos conceptos matemáticos.

Grupo Conformado por: 
Mercedes María José Vásquez Méndez
Luis Enrique Portillo Orellana 
Marlyn Yaneth Ixcoy García 
Danna Lucrecia Del Cid López
