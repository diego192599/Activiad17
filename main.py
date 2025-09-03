import tkinter as tk

ventana=tk.Tk()
ventana.title("Calculadora :)")
ventana.geometry("400*300")

etiqueta=tk.Label(ventana, text="Ingrese dos numeros: ")
etiqueta.pack(pady=6)

entrada=tk.Entry(ventana)
entrada.pack(pady=6)

def sumar():
    num1=entrada.get()
    num2=entrada.get()

