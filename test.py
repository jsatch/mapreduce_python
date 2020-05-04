import mapreduce

def f_map(nombre_archivo):
        f = open(nombre_archivo , "r")
        lines = f.readlines()
        respuesta = []
        for l in lines:
            palabras = l.split(" ")
            for p in palabras:
                respuesta.append([p, 1])
        return respuesta

def f_reduce(key, lista):
    cont = 0
    for elemento in lista:
        cont += 1

    return (key, cont)

def main():
    archivos = ['archivo1.txt', 'archivo2.txt', 'archivo3.txt']

    res = mapreduce.mapreduce(archivos, f_map, f_reduce)

    mapreduce.printb(res)

main()
