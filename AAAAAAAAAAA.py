def validar(programa):
    ok = len(programa) >=5 and programa[0] == "#" and programa[-1] == "#"
    if ok:
        for c in programa[1:4]:
            if c not in "0123456789":
                ok = False
    if ok:
        i=4
        while ok and i<len(programa)-1:
            if programa[i] not in "+-P":
                ok = False
            i += 1
    return ok

def procesar(programa):
    if validar(programa) != True:
        print ("ERROR")
    numero_inicial = int (programa[1:4])

    # Cantidad de P's
    lista_de_P = []
    for i in range(len(programa)):
        if programa[i] == "P":
            lista_de_P.append(i)

    for i in range(len(lista_de_P) + 1):
        cantidad_de_mas = 0
        cantidad_de_menos = 0
        if i == 0:
            j = 4
        else:
            j = lista_de_P[i-1] + 1
        if i == len(lista_de_P):
            k = len(programa) - 1
        else:
            k = lista_de_P[i]
        for c in programa[j:k]:
            if c in "+":
                cantidad_de_mas += 1
            elif c in "-":
                cantidad_de_menos += 1
        
        if i != len(lista_de_P):
            print("Cuac ", end="")
        else:
            print("Valor final ", end="")
        numero_inicial += (cantidad_de_mas - cantidad_de_menos)
        print (numero_inicial)
    return numero_inicial


def inicio ():
    programa = ""
    lista_resultados = []
    while programa != "FIN":
        programa = input("Ingrese programa: ")
        if validar(programa):
            resultado = procesar(programa)
            lista_resultados.append(resultado)
        else:
            print("Error de sintaxis")
    
    # Obtener menor y mayor
    numero_resultado = []
    for i in range(len(lista_resultados)):
        numero_resultado.append(i)
    
    for i in range(len(lista_resultados)):
        if i == len(lista_resultados) - 1:
            continue
        if lista_resultados[i] > lista_resultados[i+1]:
            temp = lista_resultados[i]
            lista_resultados[i] = lista_resultados[i+1]
            lista_resultados[i+1] = temp
            temp2 = numero_resultado[i]
            numero_resultado[i] = numero_resultado[i+1]
            numero_resultado[i+1] = temp2

    i = len(lista_resultados) - 1
    while i > 0:
        if lista_resultados[i] < lista_resultados[i-1]:
            temp = lista_resultados[i]
            lista_resultados[i] = lista_resultados[i-1]
            lista_resultados[i-1] = temp
            temp2 = numero_resultado[i]
            numero_resultado[i] = numero_resultado[i-1]
            numero_resultado[i-1] = temp2
        i -= 1
    
    print(f"El menor valor corresponde al programa {numero_resultado[0]+1} y fue {lista_resultados[0]}")
    print(f"El mayor valor corresponde al programa {numero_resultado[-1]+1} y fue {lista_resultados[-1]}")
    

inicio()