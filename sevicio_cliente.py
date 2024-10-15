import random
import time
cola1=[1,2,3,4,5,6,7,8,9]
cola2=[1,2,3,4,5,6,7,8,9]
colas3=[1,2,3,4,5,6,7,8,9]
lista= [1,2,3,4,5,6,7,8,9]
def menu_servicos():
    print("Elige que servicio quieres:")
    print("1.Servicio 1")
    print("2.Servicio 2")
    print("3.Servicio 3")
    opcion= int(input("Seleciona el numero de servicio (1-3):"))
    if opcion ==1:
        return cola1
    if opcion ==2:
        return cola2
    if opcion ==3:
        return colas3
    else:
        print("Opcion invalida.Por favor seleciones una opcion valida")
        return menu_servicos()


def numero_lista():
        iniciar=str(input("Ingrese C para darle su numero de lista"))
        if iniciar.upper() == "C":
            elemento1=random.choice(lista)
            print(f"Numero de lista es: C{elemento1}")
            return elemento1
        else:
            print("Debe ingresar la leta C para asignarle un numero de lisata")


def hacer_cola(cola):
    numero_asignado=numero_lista()
    if numero_asignado is None:
        return
    i =0
    while  i < len(cola):
        numero= f"A{i+1}"
        print(f"Atendiento al cliente {numero}")
        time.sleep(1)
        if i + 1== numero_asignado:
            print("Puedes pasar")
            break
        i +=1
servicio=menu_servicos()
hacer_cola(servicio)