import tkinter as tk

ventana=tk.Tk()
ventana.title("Calculadora :)")
ventana.geometry("400*300")

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

def multiplicar():
    try:
        num1=float(entrada1.get())
        num2=float(entrada2.get())


