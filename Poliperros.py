import random
import os

numPerros=0
datosPoliPerros={
  "nombre":[],
  "huellaDactilar":[]
}
fotosPoliperros={
  "foto":[]
}
donaciones={
  "donacion":[]
}
print("---------- POLIPERROS ----------")
print("---------- Bienvenido(a) ----------")
print("Que acción desea realizar")
print("1) Registrar poliperros")
print("2) Mostrar poliperros")
print("3) Registrar foto de poliperros")
print("4) Donaciones")
print("5) Salir")
tipoAccion = int(input("Ingrese la opción: "))

while tipoAccion!=5:
  if tipoAccion==1:
    print("Caso 1")
    numPerros = int(input("Ingresa el numero de poliperros: "))
    for i in range(numPerros):
      print("Ingresa los datos del poliperro",i+1)
      nombre=input("Nombre: ")
      huellaDactilar=input("Huella: ")
      datosPoliPerros['nombre'].append(nombre)
      datosPoliPerros['huellaDactilar'].append(huellaDactilar)
    print("---------- POLIPERROS ----------")
    print("---------- Bienvenido(a) ----------")
    print("Que acción desea realizar")
    print("1) Registrar poliperros")
    print("2) Mostrar poliperros")
    print("3) Registrar foto de poliperros")
    print("4) Donaciones")
    print("5) Salir")
    tipoAccion = int(input("Ingrese la opción: "))
  if tipoAccion==2:
    os.system("clear")
    print("Caso 2")
    print("Mostrar los datos de Donaciones")
    print("* Donaciones ",donaciones['donacion'])
    for i in range(numPerros):
      print("----------------------------")
      print("Mostrar los datos del poliperro",i+1)
      print("* Nombre ",datosPoliPerros['nombre'][i])
      print("* HuellaDactilar ",datosPoliPerros['huellaDactilar'][i])
      if "foto" in datosPoliPerros:
        print("* Foto",datosPoliPerros['foto'][i])
      print("----------------------------")

    
    print("---------- POLIPERROS ----------")
    print("---------- Bienvenido(a) ----------")
    print("Que acción desea realizar")
    print("1) Registrar poliperros")
    print("2) Mostrar poliperros")
    print("3) Registrar foto de poliperros")
    print("4) Donaciones")
    print("5) Salir")
    tipoAccion = int(input("Ingrese la opción: "))
  if tipoAccion==3:
    print("Caso 3")
    for i in range(numPerros):
      print("Ingrese la foto del Poliperro",i+1)
      print("¿El Poliperro dispone de foto?")
      foto=input("Ingrese si o no: ")
      if foto == "si":
        foto = input("Foto: ")
        fotosPoliperros['foto'].append(foto)
      else:
        fotosPoliperros['foto'].append("Foto-prueba.png")

    datosPoliPerros.update(fotosPoliperros)
    print("---------- POLIPERROS ----------")
    print("---------- Bienvenido(a) ----------")
    print("Que acción desea realizar")
    print("1) Registrar poliperros")
    print("2) Mostrar poliperros")
    print("3) Registrar foto de poliperros")
    print("4) Donaciones")
    print("5) Salir")
    tipoAccion = int(input("Ingrese la opción: "))
  if tipoAccion==4:
    print("Que donacion desea realizar")
    print("1) Alimentos")
    print("2) Juguetes")
    print("3) Dinero")
    print("4) Medicinas")
    accion=int(input("Ingrese la opcion: "))
    if accion==1:
      alimento=input("Ingrese las libras y marca de la comida que desea donar: ")
      donaciones["donacion"].append(alimento)
    if accion==2:
      juguetes=input("Ingrese que juguete desea donar: ")
      donaciones["donacion"].append(juguetes)
    if accion==3:
      dinero=input("Ingrese cuanto dinero desea donar: ")
      donaciones["donacion"].append(dinero)
    if accion==4:
      medicina=input("Ingrese que medicina desea donar: ")
      donaciones["donacion"].append(medicina)
    print("---------- POLIPERROS ----------")
    print("---------- Bienvenido(a) ----------")
    print("Que acción desea realizar")
    print("1) Registrar poliperros")
    print("2) Mostrar poliperros")
    print("3) Registrar foto de poliperros")
    print("4) Donaciones")
    print("5) Salir")
    tipoAccion = int(input("Ingrese la opción: "))

os.system("clear")   
print("Muchas gracias")
    

