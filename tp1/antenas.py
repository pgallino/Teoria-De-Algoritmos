"""arranco con km_actual = 0
miro todos los intervalos y los que tengan ki <= km_actual los voy viendo y me quedo con el que tenga kf mayor
km_actual = kf_mayor
repito hasta que km_actual sea mayor o igual a k"""

from mergesortkmi import mergeSortKMI

def cargar_contratos(archivo): #toma la info del archivo con los contratos

    """Recibe por parametro un archivo con los contratos disponibles
    archivo txt de la forma contrato,posición,radio.
    retorna lista con los intervalos de cada contrato ordenados 
    por comienzo de tramo, de menor a mayor"""

    lista_antenas = []
    with open(archivo, "r") as f:
        for linea in f:
            linea = linea.rstrip("\n").split(",")
            nro, posicion, radio = linea
            kmi = int(posicion) - int(radio)
            kmf = int(posicion) + int(radio)
            lista_antenas.append([int(nro),kmi,kmf])
    mergeSortKMI(lista_antenas)
    return lista_antenas

def distribuir_antenas(k,lista_antenas):

    """recibe la cantidad de kilometros de la ruta, y la lista de contratos
    ordenada, retornada por cargar_contratos.
    selecciona los contratos necesarios y los retorna en una lista"""

    elegidas = []
    km_actual = 0
    km_actual_provisorio = 0
    for i in range(len(lista_antenas)):

        if lista_antenas[i][1] <= km_actual:                        #chequeo las candidatas a antena actuales
            if lista_antenas[i][2] > km_actual_provisorio:
                km_actual_provisorio = lista_antenas[i][2]
                indice = i

        if km_actual_provisorio >= k:                      #si el km_actual_provisiorio ya alcanza para cubrir la ruta, elijo la antena y retorno
            elegidas.append(lista_antenas[indice][0])
            return elegidas
        
        if i == len(lista_antenas)-1 or lista_antenas[i+1][1] > km_actual_provisorio:  #si el inicio del siguiente es mayor al km_actual_provisorio no me alcanza
            print("No se puede cubrir toda la ruta.")
            return

        if lista_antenas[i+1][1] > km_actual:              #si ya chequee todas las candidatas actuales me quedo con la mayor y actualizo km_actual
            elegidas.append(lista_antenas[indice][0])
            km_actual = km_actual_provisorio+1             #sumo uno porque ya estaria cubierto el km_actual_provisorio

    return elegidas

def elegir_contratos(k, archivo):

    """Recibe archivo con los contratos disponibles y el largo de la ruta.
    Retorna la selección de contratos óptima"""
    
    contratos_seleccionados = distribuir_antenas(k,cargar_contratos(archivo))
    print(contratos_seleccionados)
    return(contratos_seleccionados)

#es o(nlogn) por usar mergesort para ordenar por comienzo de intervalo y luego hacer una iteracion o(n)

#pruebas ejemplo del informe

assert elegir_contratos(10, "contratos.txt") == [1]
assert elegir_contratos(50,"contratos.txt") == [1]
assert elegir_contratos(100,"contratos.txt") == [5]
assert elegir_contratos(160,"contratos.txt") == [5]
assert elegir_contratos(161,"contratos.txt") == [5,4]
assert elegir_contratos(180,"contratos.txt") == [5,4]
assert elegir_contratos(254,"contratos.txt") == [5,6]
assert elegir_contratos(460,"contratos.txt") == [5,6]
assert elegir_contratos(461,"contratos.txt") == [5,6,2]
assert elegir_contratos(552,"contratos.txt") == [5,6,2]
assert elegir_contratos(553,"contratos.txt") == None
assert elegir_contratos(1000,"contratos.txt") == None

#prueba con tramo en el medio sin poder cubrir

assert elegir_contratos(50, "contratos1.txt") == None

#prueba con inicio fuera de alcance

assert elegir_contratos(60, "contratos2.txt") == None

print("todo OK")
    