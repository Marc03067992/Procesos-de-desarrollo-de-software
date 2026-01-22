import random 

def selection_sortPasoA(lista):
    for i in range(len(lista)-1):    
        for j in range(len(lista)-1-i):
            print(lista)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sortPasoD(lista):
    for i in range(len(lista)-1):    
        for j in range(len(lista)-1-i):
            print(lista)
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


continuar = True

while continuar:
    
    print("Elige la forma de la lista")
    Decision = input("Descendente(D) / Ascendente(A): ").upper()
    lista = [random.randint(1, 100) for x in range(5)]
    lista2= list(lista)
    
    if Decision == "D":
        selection_sortPasoD(lista)
        
        
    elif Decision == "A": 
        selection_sortPasoA(lista)
        
    continuar = input("¿Deseas salir(S/N)? ").upper() == "N"

