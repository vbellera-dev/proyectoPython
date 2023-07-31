import tkinter
import time
import os
import re

#TKinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from idlelib.tooltip import Hovertip

#Temas de Tkinter
from ttkthemes import ThemedTk

#Otros modulos
from ast import literal_eval
import pywhatkit as pwk
import keyboard
from PIL import Image, ImageTk

#Mis modulos
from tabla_usuarios import generar_tabla

paises = ["Afganistán","Albania","Alemania","Andorra","Angola","Antigua y Barbuda","Arabia Saudita","Argelia","Argentina","Armenia","Australia","Austria","Azerbaiyán","Bahamas","Bangladés","Barbados","Baréin","Bélgica","Belice","Benín","Bielorrusia","Birmania","Bolivia","Bosnia y Herzegovina","Botsuana","Brasil","Brunéi","Bulgaria","Burkina Faso","Burundi","Bután","Cabo Verde","Camboya","Camerún","Canadá","Catar","Chad","Chile","China","Chipre","Ciudad del Vaticano","Colombia","Comoras","Corea del Norte","Corea del Sur","Costa de Marfil","Costa Rica","Croacia","Cuba","Dinamarca","Dominica","Ecuador","Egipto","El Salvador","Emiratos Árabes Unidos","Eritrea","Eslovaquia","Eslovenia","España","Estados Unidos","Estonia","Etiopía","Filipinas","Finlandia","Fiyi","Francia","Gabón","Gambia","Georgia","Ghana","Granada","Grecia","Guatemala","Guyana","Guinea","Guinea ecuatorial","Guinea-Bisáu","Haití","Honduras","Hungría","India","Indonesia","Irak","Irán","Irlanda","Islandia","Islas Marshall","Islas Salomón","Israel","Italia","Jamaica","Japón","Jordania","Kazajistán","Kenia","Kirguistán","Kiribati","Kuwait","Laos","Lesoto","Letonia","Líbano","Liberia","Libia","Liechtenstein","Lituania","Luxemburgo","Madagascar","Malasia","Malaui","Maldivas","Malí","Malta","Marruecos","Mauricio","Mauritania","México","Micronesia","Moldavia","Mónaco","Mongolia","Montenegro","Mozambique","Namibia","Nauru","Nepal","Nicaragua","Níger","Nigeria","Noruega","Nueva Zelanda","Omán","Países Bajos","Pakistán","Palaos","Palestina","Panamá","Papúa Nueva Guinea","Paraguay","Perú","Polonia","Portugal","Reino Unido","República Centroafricana","República Checa","República de Macedonia","República del Congo","República Democrática del Congo","República Dominicana","República Sudafricana","Ruanda","Rumanía","Rusia","Samoa","San Cristóbal y Nieves","San Marino","San Vicente y las Granadinas","Santa Lucía","Santo Tomé y Príncipe","Senegal","Serbia","Seychelles","Sierra Leona","Singapur","Siria","Somalia","Sri Lanka","Suazilandia","Sudán","Sudán del Sur","Suecia","Suiza","Surinam","Tailandia","Tanzania","Tayikistán","Timor Oriental","Togo","Tonga","Trinidad y Tobago","Túnez","Turkmenistán","Turquía","Tuvalu","Ucrania","Uganda","Uruguay","Uzbekistán","Vanuatu","Venezuela","Vietnam","Yemen","Yibuti","Zambia","Zimbabue"];

#Deberia meter diccionarios en una lista. Asi no trabajo con JSON y puedo usar un archivo txt

def actualizar_usuarios():
    global usuarios
    usuarios = []
    global numero_usuarios
    numero_usuarios = 0

    with open('registro_usuarios.txt', 'r') as archivo_usuarios:
        for line in archivo_usuarios:
            print(line)
            diccionario = literal_eval(line) #Toma la linea y literalmente Python la evalua. Entonces estoy asignando un diccionario a diccionario y lo guardo en usuarios
            usuarios.append(diccionario)
        numero_usuarios = len(usuarios)
        print(f"Numero de usuarios: {numero_usuarios}")
        print(list(usuarios))

actualizar_usuarios()

def validar_nombre(nombre):  
    patron = r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*$"
    coincidencia = re.match(patron, nombre)
    return coincidencia

def validar_telefono(telefono):
    patron = r"^\+\d{1,3}\-\d{3}\-\d{3}\-\d{3,4}$"
    coincidencia = re.match(patron, telefono)
    return coincidencia

def validar_correo(correo):
    patron = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
    coincidencia = re.match(patron, correo)
    return coincidencia

def correo_repetido(correo, usuarios):
    for usuario in usuarios:
        if (correo in usuario.values()):
            return True
    return False

def obtener_datos():
    #Obtener info de usuario
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    
    try:
        edad = int(edad_entry.get())
    except:
        edad = 0

    genero = genero_entry.get()
    pais = pais_entry.get()
    ciudad = ciudad_entry.get()
    correo = correo_entry.get()
    telefono = telefono_entry.get()
    terminos = terminos_status.get()


    validacion_datos(nombre, apellido, edad, genero, pais, ciudad, correo, telefono, terminos)

def validacion_datos(nombre, apellido, edad, genero, pais, ciudad, correo, telefono, terminos):
    global usuarios
    global numero_usuarios

    #Validacion de datos usuario
    
    if terminos == False:
        tkinter.messagebox.showwarning(title="Error - Terminos y condiciones", message="Debe aceptar los términos y condiciones para continuar")
        return
    
    if nombre == "" or apellido == "" or edad == "" or genero == "" or pais == "" or ciudad == "" or correo == "" or telefono == "":
        tkinter.messagebox.showwarning(title="Error - Datos incompletos", message="Debe completar todos los campos")
        return
    
    if validar_nombre(nombre) == None:
        tkinter.messagebox.showwarning(title="Error - Nombre no valido", message="El nombre no es valido")
        return
    
    if validar_nombre(apellido) == None:
        tkinter.messagebox.showwarning(title="Error - Apellido no valido", message="El apellido no es valido")
        return
    
    if(nombre == "Francisco" and apellido == "Molina"):
        tkinter.messagebox.showwarning(title="Error", message="ALERTA. ESTA INTENTANDO REGISTRARSE EL GORDO MARICO Y MOJONEADO DE FRANCISCO\n\nPRESIONE ACEPTAR PARA VER VIDEO DE FRANCISCO BAILANDO. . .")
        pwk.playonyt("Funny fat Gay guy dancing (best one)")
        tkinter.messagebox.showwarning(title="Error", message="Aviso Legal: Victor no fue el autor de este programa. Lo saco de un video tutorial")
        return
    
    if edad > 100:
        tkinter.messagebox.showwarning(title="Error - Edad no valida", message="La edad no es valida.")
        return
    
    elif edad < 18:
        tkinter.messagebox.showwarning(title="Error - Menor de edad", message="Debe ser mayor de edad para registrarse.")
        return
    
    if genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        tkinter.messagebox.showwarning(title="Error - Genero no valido", message="Seleccione un genero valido")
        return
    
    if validar_nombre(pais) == None:
        tkinter.messagebox.showwarning(title="Error - Pais no valido", message="El pais no es valido. Seleccione un pais de la lista")
        return
    
    if validar_nombre(ciudad) == None:
        tkinter.messagebox.showwarning(title="Error - Ciudad no valida", message="La ciudad no es valida")
        return
    
    if validar_correo(correo) == None:
        tkinter.messagebox.showwarning(title="Error - Correo no valido", message="El correo no es valido")
        return
    
    if (correo_repetido(correo, usuarios)):
        tkinter.messagebox.showwarning(title="Error - Correo ya registrado", message=f"El correo {correo} ya esta registrado. Introduzca un correo diferente.")
        return
    
    if validar_telefono(telefono) == None:
        tkinter.messagebox.showwarning(title="Error - telefono no valido", message="El telefono no es valido")
        return

    # Agregar usuario valido. Pasar a otra funcion?? Me da ladilla...
    
    usuario = str({"id":numero_usuarios,"nombre":nombre, "apellido":apellido, "edad":edad, "genero":genero, "pais":pais, "ciudad":ciudad, "correo":correo, "telefono":telefono})

    with open('registro_usuarios.txt', 'a') as archivo_usuarios:
        archivo_usuarios.write(usuario + "\n")

    actualizar_usuarios()

    nombre_entry.delete(0, END)
    apellido_entry.delete(0, END)
    edad_entry.delete(0, END)
    edad_entry.insert(0, 18)
    genero_entry.delete(0, END)
    pais_entry.delete(0, END)
    ciudad_entry.delete(0, END)
    correo_entry.delete(0, END)
    telefono_entry.delete(0, END)
    terminos_status.set(False)

    tkinter.messagebox.showinfo(title="Info", message=f"Usuario {nombre} {apellido} registrado correctamente")

    enviar_mensaje(nombre, apellido, edad, pais, ciudad, correo)

def enviar_mensaje(nombre, apellido, edad, pais, ciudad, correo):
    try:
        pwk.sendwhatmsg_to_group_instantly("IcbEE2VFYsl9Iv11EUZ11K", f"Se registro el usuario: {nombre} {apellido}, de {edad} anos de edad, residenciado en {ciudad} - {pais} y titular del correo: {correo} / Software de Victor Bellera")
        print("Mensaje enviado por Whatsapp de manera satisfactoria.")
        time.sleep(5) 
        keyboard.press_and_release('ctrl+w')
    except:
        print("No se pudo enviar el mensaje por Whatsapp")

def imprimir_tabla():
    global usuarios
    ventana_tabla = Toplevel()
    ventana_tabla.title("Tabla de usuarios")
    # ventana_tabla.geometry("700x200")
    generar_tabla(usuarios, ventana_tabla)

def borrar_datos():
    global usuarios
    usuarios = []
    with open("registro_usuarios.txt", "w") as archivo_usuarios:
        archivo_usuarios.write("")
    tkinter.messagebox.showinfo(title="Info", message="Datos borrados correctamente")



#################################### SECCION DE TKINTER ###############################################

#Aqui use Temas para Tkinter https://ttkthemes.readthedocs.io/en/latest/index.html

ventana = ThemedTk(theme="clearlooks") #Es la ventana padre. Es el widget que contiene los demas widgets.
ventana.title("Registro de Usuario - by vbellera_dev")
ventana.geometry("+700+200")
ventana.resizable(False, False)

#Para cambiar el icono mierdero ese https://stackoverflow.com/questions/33137829/how-to-replace-the-icon-in-a-tkinter-app
icono = Image.open('icono_perfil.png')
foto = ImageTk.PhotoImage(icono)
ventana.wm_iconphoto(True, foto)

principal = ttk.Frame(ventana) #Frame principal que pertenece a la ventana
#Primero guardamos el frame en una variable. El segundo paso seria hacer pack, place or grid (se llaman layout managers)
principal.pack() #Es el mas facil de usar y ademas es responsive

#Recuerda que siempre al anadir un widget hay dos pasos. Uno definir el tipo de widget y el otro hacerlo visible (pack, grid, etc)

#Datos Personales (Nombre, Apellido, Edad, Genero)
datos_personales = ttk.LabelFrame(principal, text="Datos personales")
datos_personales.grid(row=0, column=0, columnspan=2, padx=20, pady=10) #0 es igual a 1

#Etiquetas y Entradas para Datos Personales

nombre_label = ttk.Label(datos_personales, text="Nombre")
nombre_label.grid(row=0, column=0)

nombre_entry = ttk.Entry(datos_personales)
nombre_entry.grid(row=1, column=0)
nombre_tip = Hovertip(nombre_entry, "Ingrese su nombre. No use caracteres especiales ni numeros.")

apellido_label = ttk.Label(datos_personales, text="Apellido")
apellido_label.grid(row=0, column=1)

apellido_entry = ttk.Entry(datos_personales)
apellido_entry.grid(row=1, column=1)
apellido_tip = Hovertip(apellido_entry, "Ingrese su apellido. No use caracteres especiales ni numeros.")

edad_label = ttk.Label(datos_personales, text="Edad")
edad_label.grid(row=2, column=0)

#Aqui defino un valor por default
default = tkinter.StringVar()
default.set("18")

edad_entry = ttk.Spinbox(datos_personales, from_=1, to=100, textvariable=default)
edad_entry.grid(row=3, column=0)
edad_tip = Hovertip(edad_entry, "Ingrese su edad. No puede registrarse si es menor de 18 años.")

genero_label = ttk.Label(datos_personales, text="Género")
genero_label.grid(row=2, column=1)

genero_entry = ttk.Combobox(datos_personales, values=["Masculino", "Femenino", "Otro"])
genero_entry.grid(row=3, column=1)
genero_tip = Hovertip(genero_entry, "Seleccione su genero de la lista desplegable.")

#Aqui vamos a aplicar padding a todos los widgets

for widget in datos_personales.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Datos Contacto (Pais, Ciudad,Correo y Telefono)

datos_contacto = ttk.LabelFrame(principal, text="Datos de contacto")
datos_contacto.grid(row=1, column=0, columnspan=2, sticky="news", padx=20, pady=10) #sticky es para que este nuevo LabelFrame ocupe el mismo espacio que el LabelFrame anterior

#Etiquetas y Entradas para Datos Contacto

pais_label = ttk.Label(datos_contacto, text="Pais")
pais_label.grid(row=0, column=0)

pais_entry = ttk.Combobox(datos_contacto, values=paises)
pais_entry.grid(row=1, column=0)
pais_tip = Hovertip(pais_entry, "Ingrese su pais. Puede usar la lista desplegable. No use caracteres especiales ni numeros.")

ciudad_label = ttk.Label(datos_contacto, text="Ciudad")
ciudad_label.grid(row=0, column=1)

ciudad_entry = ttk.Entry(datos_contacto)
ciudad_entry.grid(row=1, column=1)
ciudad_tip = Hovertip(ciudad_entry, "Ingrese su ciudad. No use caracteres especiales ni numeros.")

correo_label = ttk.Label(datos_contacto, text="Correo")
correo_label.grid(row=2, column=0)

correo_entry = ttk.Entry(datos_contacto)
correo_entry.grid(row=3, column=0)
correo_tip = Hovertip(correo_entry, "Ingrese su correo. Debe seguir el formato: correo@dominio.com")

telefono_label = ttk.Label(datos_contacto, text="Teléfono")
telefono_label.grid(row=2, column=1)

telefono_entry = ttk.Entry(datos_contacto)
telefono_entry.grid(row=3, column=1)
telefono_tip = Hovertip(telefono_entry, "Ingrese su teléfono. Debe seguir el siguiente formato: +XXX-XXX-XXXX")

#Aqui vamos a aplicar padding a todos los widgets

for widget in datos_contacto.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Terminos y Condiciones

terminos_frame = ttk.LabelFrame(principal, text="Términos y condiciones")
terminos_frame.grid(row=2, column=0, columnspan=2, sticky="news", padx=20, pady=10)

terminos_status = tkinter.BooleanVar() #No podemos usar get con Checkbutton. Asi que creamos una variable tipo string y almacenamos el valor de Checkbutton cuando este marcado
terminos_check = ttk.Checkbutton(terminos_frame, text="He leído y acepto los términos y condiciones", variable=terminos_status, onvalue=True, offvalue=False)
terminos_check.grid(row=0, column=0)

#Boton Aceptar

boton_aceptar = ttk.Button(principal, text="ACEPTAR", command= obtener_datos)
boton_aceptar.grid(row=3, column=0, pady=10)

#Boton Borrar

boton_borrar = ttk.Button(principal, text="BORRAR USUARIOS", command= borrar_datos)
boton_borrar.grid(row=3, column=1, pady=10)

#Boton Ver lista de usuarios
boton_usuarios = ttk.Button(principal, text="VER LISTA DE USUARIOS", command=imprimir_tabla)
boton_usuarios.grid(row=4, column=0, columnspan=2, pady=10)

ventana.mainloop() #Loop que se ejecutara siempre que tkinter este activo