#los solicitantes son un diccionario del 0 al n y cada uno tiene  una lista con su ranking de los requeridos
#los requeridos son un diccionario del 0 al n y cada uno tiene una tupla, una lista con su ranking de los solicitantes y su pareja

def gale_shapley_empajeramiento(solicitantes, requeridos, matching, desocupados): #hecho por mi
    s = desocupados[-1]
    for r in solicitantes[s]:
        if requeridos[r][1] == None:
            matching.append((s,r))
            requeridos[r] = (requeridos[r][0], s)
            desocupados.pop()
            break
        else:
            p = requeridos[r][1]
            if requeridos[r][0].index(s) < requeridos[r][0].index(p):
                matching.remove((p,r))
                matching.append((s,r))
                desocupados.pop()
                desocupados.append(p)
                requeridos[r] = (requeridos[r][0], s)
                break


def gale_shapley(solicitantes, requeridos):
    matching = []
    desocupados = list(solicitantes.keys())
    while len(desocupados) != 0:
        gale_shapley_empajeramiento(solicitantes, requeridos, matching, desocupados)
    return matching

solicitantes = {1:[2,3,1,4],2:[3,2,1,4],3:[3,1,2,4],4:[1,2,3,4]}
requeridos = {1:([4,3,1,2],None),2:([2,1,4,3],None),3:([1,2,3,4],None),4:([1,2,3,4],None)}

print(gale_shapley(solicitantes, requeridos))
