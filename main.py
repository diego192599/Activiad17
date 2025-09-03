import tkinter as tk

ventana=tk.Tk()
ventana.title("Calculadora :)")
ventana.geometry("400x400")
ventana.config(bg="lightblue")

etiqueta=tk.Label(
    ventana,
    text="Calculadora Basica",
    bg="lightblue",
    fg="navy",
    font=("Arial", 14,"bold")
)
etiqueta.pack(pady=10)

entrada1=tk.Entry(ventana, font=("Arial",12),justify="center")
entrada1.pack(pady=5)

entrada2=tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada2.pack(pady=5)

resultado = tk.Label(
    ventana,
    text="El resultado es:",
    bg="lightblue",
    fg="black",
    font=("Arial", 14, "bold")
)
resultado.pack(pady=15)

def sumar():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        res=num1+num2
        resultado.config(text=f"El resultado {res}")
    except ValueError:
        resultado.config(text="Error: ingrese números válidos")
def restar():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        resul=num1-num2
        resultado.config(text=f"El resultado de la resta es {resul}")
    except ValueError:
        resultado.config(text="Error: ingrese números válidos")

def multiplicar():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())
        resu=num1*num2
        resultado.config(text=f"El resultado de la multiplicacion {resu}")
    except ValueError:
        resultado.config(text="Error: ingrese números válidos")
def division():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            resultado.config(text="Error: Divison entre 0 no es posible")
        else:
            resultados = num1 / num2
            resultado.config(text=f"El resultado de la divison es {resultados}")

    except ValueError:
        resultado.config(text="Error: ingrese números válidos")


def Limpiar():
    entrada1.delete(0,tk.END)
    entrada2.delete(0, tk.END)
    resultado.config(text="El resultado es: ")


boton_Suma=tk.Button(ventana, text="Suma", command=sumar)
boton_Suma.pack(pady=6)

boton_resta=tk.Button(ventana, text="Resta", command=restar)
boton_resta.pack(pady=6)

boton_Multi=tk.Button(ventana, text="Multiplicacion", command=multiplicar)
boton_Multi.pack(pady=6)

boton_Div=tk.Button(ventana,text="Division", command=division)
boton_Div.pack(pady=6)

boton_Limpiar=tk.Button(ventana, text="Limpiar", command=Limpiar)
boton_Limpiar.pack(pady=6)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=6)

ventana.mainloop()
