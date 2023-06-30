lista_rut=[]
lista_nombre_d=[]
lista_id_unic=[]
lista_nombre_masc=[]
lista_cantidad=[]
lista_habitacion=[1,2,3,4,5,6,7,8,9,10]
cant_uni = 0


import numpy as np









def saludo():
    input("""Bienvenida/o a la guarderia “Mascota Segura”
        
    PRECIONE (ENTER) PARA CONTINUARR...""")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        lista_rut.append[rut]


def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        lista_nombre_d.append[nom]


def id_unico():
    while True:
        id_uni = cant_uni + 1
        cant_uni = cant_uni + 1
        lista_id_unic.append[id_unico]
        break

def validar_nombre_mascota():
    while True:
        nom_m = input("Ingrese nombre de su mascota: ")
        if len(nom_m.strip()) >= 3 and nom_m.isalpha():
            return nom_m
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
        lista_nombre_masc.append[nom_m]



def validar_cantidad_dias():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de dias: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
        lista_cantidad.append[cantidad]


def validar_habitaciones():
    while True:
        b=np.array([(1,2,3,4,5),(6,7,8,9,10)])
        print(b)
        habt = input(f"Ingrese habitacion {lista_habitacion}: ")
        if habt.upper() in lista_habitacion:
            lista_habitacion.remove(habt)
            
        else:
            print("ERROR! HABITACION INCORRECTA!/HABITACION NO DISPONIBLE!")






def validar_todo():
    while True:
        try:
            opcion=int(input("""
            1- Grabar
            2- Buscar
            3- Retirarse
            4- Salir




            ingrese opcion: """))
            if opcion in(1,2,3,4):
                if opcion == 1:
                    while True:
                        try:
                            rut = int(input("Ingrese rut: "))
                            if rut >= 1000000 and rut <= 99999999:
                                nom = input("Ingrese nombre: ")
                                if len(nom.strip()) >= 3 and nom.isalpha():
                                    id_uni = cant_uni + 1
                                    cant_uni = cant_uni + 1
                                    lista_id_unic.append[id_unico]
                                    nom_m = input("Ingrese nombre de su mascota: ")
                                    if len(nom_m.strip()) >= 3 and nom_m.isalpha():
                                        try:
                                            cantidad = int(input("Ingrese cantidad de dias: "))
                                            if cantidad >= 0:
                                                pass
                                            else:
                                                print("ERROR! CANTIDAD DEBE SER 0 O POSITIVA!")
                                        except:
                                            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
                                        lista_cantidad.append[cantidad]
                                        b=np.array([(1,2,3,4,5),(6,7,8,9,10)])
                                        print(b)
                                        habt = input(f"Ingrese habitacion {lista_habitacion}: ")
                                        if habt.upper() in lista_habitacion:
                                            lista_habitacion.remove(habt)
            
                                        else:
                                            print("ERROR! HABITACION INCORRECTA!/HABITACION NO DISPONIBLE!")
                                    else:
                                        print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
                                    lista_nombre_masc.append[nom_m]
                                else:
                                    print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
                                lista_nombre_d.append[nom]
                            else:
                                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
                        except:
                             print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
                        lista_rut.append[rut]
                    
                        
                        
                        
                        
                        
                        

                        


                if opcion ==2:
                    pass
                if opcion ==3:
                    pagar = cantidad * 15000
                    print(f"su total a pagar {pagar}")
                if opcion ==4:
                    break
  
            else:
                print("ERROR! debe ingresar una de las opciones")
        except:
            print("ERROR! debe ser un numero entero")