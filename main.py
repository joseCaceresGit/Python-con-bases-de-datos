import tkinter as tk
from tkinter import messagebox
from funciones import *

def agregar_estudiante():
    id_estudiante = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    codigo_sis = entry_codigo.get()
    edad = entry_edad.get()

    if nombre and apellido and codigo_sis and edad:
        try:
            insertar_estudiante(id_estudiante, nombre, apellido, codigo_sis, edad)
            messagebox.showinfo("Exito")
        except Exception as e:
            messagebox.showerror("Errro")
    
    else:
        messagebox.showwarning("No tienes los campos completados")

def mostrar_estudiante():
    try:
        estudiantes = consulta_edad()

        for estudiante in estudiantes:
            text_estudiante.insert(tk.END, f"ID: {estudiante[0]}, Nombre: {estudiante[1],}, Apellido:{estudiante[2]}, Codigo SIS: {estudiante[3]}, Edad: {estudiante[4]}\n")
    
    except Exception as e:
        messagebox.showerror("Error")

ventana= tk.Tk()
ventana.title("Gestion de estudiantes")

tk.Label(ventana, text="ID").grid(row=0, column=0)
tk.Label(ventana, text="NOMBRE").grid(row=1, column=0)
tk.Label(ventana, text="APELLIDO").grid(row=2, column=0)
tk.Label(ventana, text="CODIGO SIS").grid(row=3, column=0)
tk.Label(ventana, text="EDAD").grid(row=4, column=0)

entry_id = tk.Entry(ventana)
entry_nombre=tk.Entry(ventana)
entry_apellido=tk.Entry(ventana)
entry_codigo=tk.Entry(ventana)
entry_edad=tk.Entry(ventana)

entry_id.grid(row=0, column=1)
entry_nombre.grid(row=1, column=1)
entry_apellido.grid(row=2, column=1)
entry_codigo.grid(row=3, column=1)
entry_edad.grid(row=4, column=1)


tk.Button(ventana, text="Agregar estudiantes", command=agregar_estudiante).grid(row=5, column=0)
tk.Button(ventana, text="Consultar Estudiante", command=mostrar_estudiante).grid(row=5, column=1)


text_estudiante = tk.Text(ventana, height=10, width=80)
text_estudiante.grid(row=6, columnspan=2, padx=10, pady=10)

ventana.mainloop()
