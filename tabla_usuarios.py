import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generar_tabla(usuarios, ventana_tabla):
    columnas = ("id","nombre", "apellido", "edad", "genero", "pais", "ciudad", "correo", "telefono")
    
    yscrollbar = ttk.Scrollbar(ventana_tabla, orient="vertical")

    tabla = ttk.Treeview(ventana_tabla, yscrollcommand=yscrollbar.set, columns=columnas, show="headings")
    tabla.grid(row=0, column=0, rowspan=6)

    yscrollbar.configure(command=tabla.yview) #Yview es un metodo para conectar el scrollbar vertical con el Scrollable widget
    yscrollbar.grid(row=0, column=1, rowspan=6, sticky="nsew")

    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("edad", text="Edad")
    tabla.heading("genero", text="Genero")
    tabla.heading("pais", text="Pais")
    tabla.heading("ciudad", text="Ciudad")
    tabla.heading("correo", text="Correo")
    tabla.heading("telefono", text="Telefono")
    
    for usuario in usuarios:
        tabla.insert("", tk.END, values=([usuario["id"]], usuario["nombre"], usuario["apellido"], usuario["edad"], usuario["genero"], usuario["pais"], usuario["ciudad"], usuario["correo"], usuario["telefono"]))
    
    def seleccion_valor(evento):
        for valor_seleccionado in tabla.selection():
            item = tabla.item(valor_seleccionado)
            print(item)
            usuario_seleccionado = item["values"]
            print(usuario_seleccionado)
            usuario_seleccionado[0] = str(usuario_seleccionado[0]) 
            usuario_seleccionado[3] = str(usuario_seleccionado[3]) 
            tk.messagebox.showinfo(title="Info", message=','.join(usuario_seleccionado))

    tabla.bind("<<TreeviewSelect>>", seleccion_valor)
    