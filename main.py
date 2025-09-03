import tkinter as tk

ventana=tk.Tk()
ventana.title("Calculadora :)")
ventana.geometry("400x400")
ventana.config(bg="lightblue")

etiqueta=tk.Label(
    ventana,
    text="Ingrese dos números:",
    bg="lightblue",
    fg="navy",
    font=("Arial", 14, "bold"),
    relief="ridge",
    bd=2,
    padx=10, pady=5
)
etiqueta.pack(pady=10)

entrada1=tk.Entry(
    ventana,
    font=("Arial", 12),
    justify="center",
    relief="sunken",
    bd=3,
    highlightbackground="gray",
    highlightcolor="blue",
    highlightthickness=1
)
entrada1.pack(pady=5)

entrada2=tk.Entry(
    ventana,
    font=("Arial", 12),
    justify="center",
    relief="sunken",
    bd=3,
    highlightbackground="gray",
    highlightcolor="blue",
    highlightthickness=1
)
entrada2.pack(pady=5)

resultado = tk.Label(
    ventana,
    text="El resultado es:",
    bg="lightblue",
    fg="black",
    font=("Arial", 14, "bold"),
    relief="groove",
    bd=3,
    padx=10, pady=5
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

frame_botones=tk.Frame(ventana,bg="lightblue")
frame_botones.pack(pady=10)

boton_Suma = tk.Button(
    frame_botones,
    text="Suma",
    command=sumar,
    bg="lightgreen",
    fg="black",
    activebackground="green",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised", bd=3,
    cursor="hand2"
)
boton_Suma.grid(row=0, column=0, padx=5, pady=5)

boton_resta = tk.Button(
    frame_botones,
    text="Resta",
    command=restar,
    bg="lightcoral",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised", bd=3,
    cursor="hand2"
)
boton_resta.grid(row=0, column=1, padx=5, pady=5)

boton_Multi = tk.Button(
    frame_botones,
    text="Multiplicación",
    command=multiplicar,
    bg="khaki",
    fg="black",
    activebackground="gold",
    activeforeground="black",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised", bd=3,
    cursor="hand2"
)
boton_Multi.grid(row=1, column=0, padx=5, pady=5)

boton_Div = tk.Button(
    frame_botones,
    text="División",
    command=division,
    bg="plum",
    fg="black",
    activebackground="purple",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised", bd=3,
    cursor="hand2"
)
boton_Div.grid(row=1, column=1, padx=5, pady=5)

boton_Limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=Limpiar,
    bg="lightgray",
    fg="black",
    activebackground="gray",
    font=("Arial", 12),
    width=12,
    relief="ridge", bd=2,
    cursor="hand2"
)
boton_Limpiar.pack(pady=5)

boton_salir = tk.Button(
    ventana,
    text="Salir",
    command=ventana.quit,
    bg="red",
    fg="white",
    activebackground="darkred",
    activeforeground="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="ridge", bd=2,
    cursor="hand2"
)
boton_salir.pack(pady=5)

ventana.mainloop()