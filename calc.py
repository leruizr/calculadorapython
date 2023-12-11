# Importa todas las funciones de la biblioteca tkinter, que es una biblioteca para crear interfaces gráficas.
from tkinter import *
import math

# Crea una nueva ventana de tkinter y la almacena en la variable "windows".
windows = Tk()

# Establece el título de la ventana "windows" como "Calculadora".
windows.title("Calculadora")
windows.configure(background="black", padx=10, pady=10)
i = 0

windows.geometry("330x470")  # Establece el tamaño de la ventana "windows" en 340x550 píxeles.

# Crea un campo de entrada de texto en la ventana "windows" con una fuente "Calibri" de tamaño 20.
texto = Entry(windows, font=("Calibri 20"))

# Coloca el campo de entrada de texto en la ventana "windows" en la fila 0 y la columna 0. 
# El campo de entrada de texto se extiende a través de 4 columnas. 
# Hay un relleno de 5 píxeles en el eje x y y alrededor del campo de entrada de texto.
texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Insertar
def clic(valor):
    global i
    if valor == "rad":
        texto.insert(i, "math.sqrt(")
        i += 10  # Incrementa el índice en 10 para evitar sobrescribir el cierre paréntesis y otros caracteres
    elif valor == "pot":
        texto.insert(i, "**")
        i += 2  # Incrementa el índice en 2 para evitar sobrescribir el segundo asterisco
    elif valor == "log":
        texto.insert(i, "math.log(")
        i += 10  # Incrementa el índice en 10 para evitar sobrescribir el cierre paréntesis y otros caracteres
    else:
        texto.insert(i, valor)
        i += 1

# Borrar desde indice 0 hasta el final
def borrar():
    texto.delete(0, END)
    i = 0

# Funcion operaciones
# Modificación en la función calcular
def calcular():
    datos = texto.get()
    try:
        resultado = eval(datos)
        texto.delete(0, END)
        texto.insert(0, resultado)
        i = 0
    except (ArithmeticError, ValueError, ZeroDivisionError):
        texto.delete(0, END)
        texto.insert(0, "Error: Operación no válida")
    except Exception as e:
        texto.delete(0, END)
        texto.insert(0, f"Error: {str(e)}")


# Crea botones y los almacena en las variables.
# Cada botón se coloca en la ventana "windows", tiene un ancho de 5 y una altura de 2.

button_width = 8
button_height = 3

box_uno = Button(windows, text="1", width=button_width, height=button_height, background="grey", command=lambda: clic(1))
box_dos = Button(windows, text="2", width=button_width, height=button_height, background="grey", command=lambda: clic(2))
box_tres = Button(windows, text="3", width=button_width, height=button_height, background="grey", command=lambda: clic(3))
box_cuatro = Button(windows, text="4", width=button_width, height=button_height, background="grey", command=lambda: clic(4))
box_cinco = Button(windows, text="5", width=button_width, height=button_height, background="grey", command=lambda: clic(5))
box_seis = Button(windows, text="6", width=button_width, height=button_height, background="grey", command=lambda: clic(6))
box_siete = Button(windows, text="7", width=button_width, height=button_height, background="grey", command=lambda: clic(7))
box_ocho = Button(windows, text="8", width=button_width, height=button_height, background="grey", command=lambda: clic(8))
box_nueve = Button(windows, text="9", width=button_width, height=button_height, background="grey", command=lambda: clic(9))
box_cero = Button(windows, text="0", width=button_width, height=button_height, background="grey", command=lambda: clic(0))
box_suma = Button(windows, text="+", width=button_width, height=button_height, background="grey", command=lambda: clic("+"))
box_resta = Button(windows, text="-", width=button_width, height=button_height, background="grey", command=lambda: clic("-"))
box_multiplicacion = Button(windows, text="*", width=button_width, height=button_height, background="grey", command=lambda: clic("*"))
box_division = Button(windows, text="/", width=button_width, height=button_height, background="grey", command=lambda: clic("/"))
box_porcentaje = Button(windows, text="%", width=button_width, height=button_height, background="grey", command=lambda: clic("%"))
box_radiacion = Button(windows, text="rad", width=button_width, height=button_height, background="grey", command=lambda: clic("rad"))
box_potencia = Button(windows, text="pot", width=button_width, height=button_height, background="grey", command=lambda: clic("pot"))
box_logaritmo = Button(windows, text="log", width=button_width, height=button_height, background="grey", command=lambda: clic("log"))
box_igual = Button(windows, text="=", width=button_width, height=button_height, background="aquamarine", command=lambda: calcular())
box_borrar = Button(windows, text="C", width=button_width, height=button_height, background="grey", command=lambda: borrar())
box_punto = Button(windows, text=".", width=button_width, height=button_height, background="grey", command=lambda: clic("."))
box_parentesis_izquierdo = Button(windows, text="(", width=button_width, height=button_height, background="grey", command=lambda: clic("("))
box_parentesis_derecho = Button(windows, text=")", width=button_width, height=button_height, background="grey", command=lambda: clic(")"))
box_coma = Button(windows, text=",", width=button_width, height=button_height, background="grey", command=lambda: clic(","))


# Coloca los botones en la ventana "windows" en las posiciones de la cuadrícula especificadas.
# Los valores de fila, columna, padx y pady no se han especificado en tu código, por lo que deberías completarlos.
# Números

# Fila 1
box_radiacion.grid(row=1, column=0, padx=5, pady=5)
box_potencia.grid(row=1, column=1, padx=5, pady=5)
box_logaritmo.grid(row=1, column=2, padx=5, pady=5)
box_porcentaje.grid(row=1, column=3, padx=5, pady=5)

# Fila 2
box_uno.grid(row=2, column=0, padx=5, pady=5)
box_dos.grid(row=2, column=1, padx=5, pady=5)
box_tres.grid(row=2, column=2, padx=5, pady=5)
box_suma.grid(row=2, column=3, padx=5, pady=5)

# Fila 3
box_cuatro.grid(row=3, column=0, padx=5, pady=5)
box_cinco.grid(row=3, column=1, padx=5, pady=5)
box_seis.grid(row=3, column=2, padx=5, pady=5)
box_resta.grid(row=3, column=3, padx=5, pady=5)

# Fila 4
box_siete.grid(row=4, column=0, padx=5, pady=5)
box_ocho.grid(row=4, column=1, padx=5, pady=5)
box_nueve.grid(row=4, column=2, padx=5, pady=5)
box_multiplicacion.grid(row=4, column=3, padx=5, pady=5)

# Fila 5
box_punto.grid(row=5, column=0, padx=5, pady=5)
box_cero.grid(row=5, column=1, padx=5, pady=5)
box_coma.grid(row=5, column=2, padx=5, pady=5)
box_division.grid(row=5, column=3, padx=5, pady=5)

# Fila 6
box_parentesis_izquierdo.grid(row=6, column=0, padx=5, pady=5)
box_parentesis_derecho.grid(row=6, column=1, padx=5, pady=5)
box_borrar.grid(row=6, column=2, padx=5, pady=5)
box_igual.grid(row=6, column=3, padx=5, pady=5)


# Inicia el bucle principal de la ventana "windows". Esto es necesario para que la ventana se muestre en la pantalla.
windows.mainloop()