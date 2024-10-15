
cola1=[]
cola2=[]
cola3=[]
rango=int(input("Ingrese de cuanto numeros quiere la colas: "))
def encolar():
    for i in range(rango):
        elemento=int(input(f"Ingrese un numero para la cola 1(posicion{i+1}): "))
        cola1.append(elemento)
        print(f"Cola 1:{cola1}")
        elemento2=int(input(f"Ingrese un numero para la cola 2(posicion{i+1}): "))
        cola2.append(elemento2)
        print(f"Cola 2:{cola2}")

def sumar():
    
    for i in range(len(cola1)):
        suma= cola1[i] + cola2[i]
        cola3.append(suma)
        print(f"Cola 3(suma de la cola1 y la cola2):{cola3}")


encolar()
sumar()



