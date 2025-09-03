import tkinter as tk

ventana=tk.Tk()
ventana.title("Calculadora :)")
ventana.geometry("650x350")

etiqueta=tk.Label(ventana, text="Ingrese dos numeros: ")
etiqueta.pack(pady=6)

entrada1=tk.Entry(ventana)
entrada1.pack(pady=6)

entrada2=tk.Entry(ventana)
entrada2.pack(pady=6)

resultado=tk.Label(ventana,text="El resultado es:")
resultado.pack(pady=6)

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

boton_Limpiar=tk.Button(ventana, text="Limpiar", command=Limpiar)
boton_Limpiar.pack(pady=6)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=6)

ventana.mainloop()
