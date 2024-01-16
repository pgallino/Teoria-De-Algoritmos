"""MergeSort por kilómetro de inicio"""
"""https://www.educative.io/edpresso/merge-sort-in-python"""
"""Funciona en O(nlogn) siendo n los elementos de la lista a ordenar"""

def mergeSortKMI(myList): #ordena las antenas por inicio de sus rangos

    """Recibe lista con los contratos disponibles y sus tramos
    Retorna una lista con los contratos ordenados por inicio de tramo"""
    
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSortKMI(left)
        mergeSortKMI(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1