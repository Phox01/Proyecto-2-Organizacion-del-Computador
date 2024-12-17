import pickle
import Funciones as f

def main():
    try:
        Pinturas=pickle.load(open("Pinturas.txt","rb"))

    except:
        Pinturas=list()

    try:
        Cotas=pickle.load(open("Cotas.txt","rb"))

    except:
        Cotas=list()
    
    while(True):
        Opcion_Menu = input("\n\n\t\tBienvenido\n\nColoca una opcion para la gestion de pinturas\n\n1. Inserción de una nueva pintura a la Base de Datos\n2. Consulta de una pintura\n3. Puesta en Mantenimiento\n4. Puesta en Exhibición\n5. Eliminación\n6. Compactador\n7. Salir (Guardado TXT)\n\n------> ")

        if Opcion_Menu == "1":
            Pinturas,Cotas = f.opcion1(Pinturas,Cotas)
              
        elif Opcion_Menu == "2":
            f.opcion2(Pinturas)
            
        elif Opcion_Menu == "3":
            f.opcion3(Pinturas)
        
        elif Opcion_Menu == "4":
            f.opcion4(Pinturas)

        elif Opcion_Menu == "5":
            f.opcion5(Pinturas)

        elif Opcion_Menu == "6":
            f.opcion6(Pinturas, Cotas)

        elif Opcion_Menu == "7":
            pickle.dump(Pinturas,open("Pinturas.txt","wb"))
            pickle.dump(Cotas,open("Cotas.txt","wb"))
            break

        else:
            print("\n----ERROR----\nNo colocaste ninguna de las opciones validas\n")

main()