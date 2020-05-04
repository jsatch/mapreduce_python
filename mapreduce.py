import itertools

def _organizeByKey(orderList):
    resp = {}
    for entry in orderList:
        key = entry[0]
        value = entry[1]

        if key not in resp:
            resp[key] = []
        resp[key].append(value)

    return resp

def printb(lista):
    '''
    Function that prints list's elements line by line
    '''
    for e in lista:
        print(e)

def mapreduce(listaIni, f_map, f_reduce):
    '''
    Function that receive a list and performs a  map
    reduce task.
    f_map: function that will be apply to every
            element from a list. It must return a
            pair of a key and a value.
            eg. ["key1", 23]
    f_reduce: function that will be apply to the list
            received from f_map. It has to receive
            2 args: a key and the list of values for that
            key.
            It will return a list with a pair with the
            key and values reduced.
    '''
    intermedios2D = map(f_map, listaIni)

    # Rebajamos una dimension
    intermedios = itertools.chain(*list(intermedios2D))
    intermedios_ordenada = sorted(intermedios, key=lambda x : x[0] )

    intermedios_organizada = _organizeByKey(intermedios_ordenada)

    resp = []

    for k,v in intermedios_organizada.items():
        r = f_reduce(k, v)
        resp.append([r[0], r[1]])

    return resp

