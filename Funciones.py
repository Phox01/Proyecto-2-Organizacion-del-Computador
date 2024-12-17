import random
from Pintura import Pintura

#################### OPCION 1  ####################

def opcion1(Pinturas,Cotas):

    cota,Cotas = Codigo_Cota(Cotas)

    print("\n\n\tINSERTANDO PINTURA\n\n- El numero de cota de esta pintura va ser: ",cota)
    nombre = Nombre_Pintura()
    precio = Precio_pintura()
    anio = Anio_pintura()
    status = Status_pintura()
    pintura = Pintura(cota,nombre,precio,anio,status,False)
    pintura.mostrar()
    
    Pinturas.append(pintura)
    print("------La pintura se agrego correctamente---------")

    return Pinturas,Cotas

def Codigo_Cota(Cotas):
    while True:
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num = "0123456789"
        letrasUnion = f'''{letras}'''
        numUnion = f'''{num}'''
        ext1 = random.sample(letrasUnion, 4)
        ext2 = random.sample(numUnion,4)
        codigo = "".join(ext1), "".join(ext2)
        cod = "".join(codigo)
        
        if cod not in Cotas:
            break
    
    Cotas.append(cod)

    return cod, Cotas

def Nombre_Pintura():
    nombre = input("\n- Coloca el nombre de la pintura (Maximo 10 caracteres y en una sola palabra): ")
    while not nombre.isalpha() or len(nombre) > 10:
        print("\n\n\t\t\tERROR\n\n Tu nombre no puede tener: numeros, espacios o ser mayor a 10 letras")
        nombre = input("\n\n- Coloca el nombre de la pintura (Maximo 10 caracteres y en una sola palabra): ")
    return nombre

def Precio_pintura():
    precio = input("\n- Coloca el precio de la pintura (No puede ser negativo): ")
    
    while True:
        try:
            precio = float(precio)
            if precio > 0:
                break
            else:
                print("\n\n\t\t\tERROR\n\n\t\tTu precio es negativo o igual 0")
                precio = input("\n\n- Coloca el precio de la pintura (No puede ser negativo): ")

        except:
            print("\n\n\t\t\tERROR\n\n\t\tTu precio no es un numero")
            precio = input("\n\n- Coloca el precio de la pintura (No puede ser negativo): ")


    return precio

def Anio_pintura():
    anio = input("\n- Coloca el año de la pintura: ")

    while True:
        try:
            if len(anio)>4:
                print("\n\n\t\t\tERROR\n\n\t\tTu año es negativo o igual 0")
                anio = input("\n\n- Coloca el año de la pintura: ")
            
            else:
                anio = int(anio)
                if anio > 0 and anio <= 2023:
                    break

                else:
                    print("\n\n\t\t\tERROR\n\n\t\tTu año es negativo o igual 0")
                    anio = input("\n\n- Coloca el año de la pintura: ")

        except:
            print("\n\n\t\t\tERROR\n\n\t\tTu año no es un numero")
            anio = input("\n\n- Coloca el año de la pintura: ")

    return anio

def Status_pintura():
    opcion = input("\n- Coloca:\n\n1. Para colocarla en exhibicion\n2. Mantenimiento\n\n----> ")

    while opcion not in ["1", "2"]:
        print("\n\n\t\tERROR\n\n\tEscoge una de las opciones seleccionadas")
        opcion = input("\n\n-  Coloca:\n\n1. Para colocarla en exhibicion\n2. Mantenimiento\n\n----> ")

    if opcion == "1":
        return True
    elif opcion == "2":
        return False
    else:
        print("\n\n\t\tError\n\n\tColoca exclusivamente el 1 o 2")

#################### OPCION 2  ####################

def opcion2(Pinturas):
    op =metodo_busqueda()

    if op == "1":
        pintura = Busqueda_Cota(Pinturas)
        if pintura  != None:
            imprimir(pintura)
        
    if op == "2":
        pintura = Busqueda_Nombre(Pinturas)
        if pintura  != None:
            imprimir(pintura)

#################### OPCION 3  ####################
def opcion3(Pinturas):
    op =metodo_busqueda()

    if op == "1":
        opcion3_1(Pinturas)
        
    if op == "2":
        opcion3_2(Pinturas) 

def opcion3_1(Pinturas):
    pintura = Busqueda_Cota(Pinturas)
    if pintura != None:
        if pintura.status:
            pintura.status = False
            imprimir(pintura)
        
        else:
            print("La pintura ya se encuentra en manteminiento")
        
def opcion3_2(Pinturas):
    pintura = Busqueda_Nombre(Pinturas)
    if pintura != None:
        if pintura.status:
            pintura.status = False
            imprimir(pintura)
        
        else:
            print("La pintura ya se encuentra en manteminiento")

#################### OPCION 4  ####################
def opcion4(Pinturas):
    op =metodo_busqueda()

    if op == "1":
        opcion4_1(Pinturas)
        
    if op == "2":
        opcion4_2(Pinturas) 

def opcion4_1(Pinturas):
    pintura = Busqueda_Cota(Pinturas)
    if pintura != None:
        if not pintura.status:
            pintura.status = True
            imprimir(pintura)
        
        else:
            print("La pintura ya se encuentra en exhibicion")

def opcion4_2(Pinturas):
    pintura = Busqueda_Nombre(Pinturas)
    if pintura != None:
        if not pintura.status:
            pintura.status = True
            imprimir(pintura)
        
        else:
            print("La pintura ya se encuentra en exhibicion")

#################### OPCION 5  ####################      
def opcion5(Pinturas):
    op =metodo_busqueda()

    if op == "1":
        opcion5_1(Pinturas)
        
    if op == "2":
        opcion5_2(Pinturas) 

def opcion5_1(Pinturas):
    pintura = Busqueda_Cota(Pinturas)

    if pintura != None:
        if not pintura.eliminate:
            pintura.eliminate = True
            pintura.mostrar()

        else:
            print("La pintura ya se encuentra en eliminado")

def opcion5_2(Pinturas):
    pintura = Busqueda_Nombre(Pinturas)
    if pintura != None:
        if not pintura.eliminate:
            pintura.eliminate = True
            pintura.mostrar()

        else:
            print("La pintura ya se encuentra en eliminado")  

#################### OPCION 6  ####################
def opcion6(Pinturas, Cotas):
    for x in Pinturas:
        if x.eliminate==True:
            for y in Cotas:
                if y==x.cota:
                    Cotas.remove(y)
            Pinturas.remove(x)
    
    print('\n-----------------------------------------\nCompresión de archivos realizada\n-----------------------------------------\n')




#################### FUNCIONES VARIAS  ####################
def metodo_busqueda():
    op = input("\n\n\t\tBienvenido a consulta de Pinturas\n\n- Deseas Buscar por:\n\n1. Cota\n2. Nombre\n\n---> ")

    while op not in ["1", "2"]:
        print("\n\n\t\tError\n\n\tEscoge una de las opciones seleccionadas")
        op = input("\n\n- Deseas Buscar por:\n\n1. Cota\n2. Nombre\n\n---> ")

    return op

def imprimir(pintura):
    if pintura.eliminate == False:
        pintura.mostrar()

    else:
        print("Lo encontre pero ya esta en eliminado") 

def crear_index_nombre(pinturas):
    cont=0
    pintura_index = []
    for x in pinturas:
        lista = []
        lista.append(cont)
        lista.append(x.nombre)
        pintura_index.append(lista)
        cont+=1

    return pintura_index

def Busqueda_Cota(Pinturas):
    cota = input("\n- Ingrese la cota de la pintura que desea buscar: ")
    pintura_index = crear_index_cota(Pinturas)
    tupla = BusquedaBinaria(pintura_index, cota)

    if tupla is None:
        print("\n\n\t\tERROR\n\n\tNo se encontró ninguna pintura con esa cota.")

    else:
        return Pinturas[tupla[0]]

def Busqueda_Nombre(Pinturas):
    nombre = input("\n- Ingrese el nombre de la pintura que desea buscar: ")
    pintura_index = crear_index_nombre(Pinturas)
    tupla = BusquedaBinaria(pintura_index, nombre)

    if tupla is None:
        print("\n\n\t\tERROR\n\n\tNo se encontró ninguna pintura con esa cota.")

    else:
        return Pinturas[tupla[0]]

def crear_index_cota(pinturas):
    cont=0
    pintura_index = []
    for x in pinturas:
        lista = []
        lista.append(cont)
        lista.append(x.cota)
        pintura_index.append(lista)
        cont+=1

    return pintura_index

def BusquedaBinaria(pintura_index, objetivo):
    pintura_index = sorted(pintura_index, key=lambda pintura: pintura[1])
    inicio = 0
    fin = len(pintura_index) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2

        if pintura_index[medio][1] == objetivo:
            return pintura_index[medio]
        
        elif pintura_index[medio][1] < objetivo:
            inicio = medio + 1

        else:
            fin = medio - 1
    
    return None
