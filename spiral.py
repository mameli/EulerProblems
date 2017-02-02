import sys

# Dato un numero dispari positivo n, la matrice associata ad n e' la
# matrice bidimensionale di dimensione nxn, riempita con i numeri da
# 1 a nxn a partire dall'elemento in alto a sinistra e procedendo da
# sinistra verso destra e dall'alto verso il basso. Ad esempio,
# la matrice associata a 3 e' la seguente matrice:
#
#   1 2 3
#   4 5 6
#   7 8 9
#
# mentre la matrice associata a 5 e' la seguente matrice:
#
#   1  2  3  4  5
#   6  7  8  9 10
#  11 12 13 14 15
#  16 17 18 19 20
#  21 22 23 24 25
#
# La visita a spirale della matrice associata a n consiste nel visitare,
# una e una sola volta, tutti gli elementi della matrice partendo
# dall'elemento "al centro" e proseguendo secondo una spirale in senso
# antiorario, ossia avanzando nel seguente ordine: in alto, a sinistra,
# in basso e a destra, il numero di volte necessario per ciascuna direzione,
# e ricominciando. Ad esempio, la visita a spirale della matrice associata a 3
# visita i suoi elementi secondo il seguente ordine:
#
# 5 2 1 4 7 8 9 6 3
#
# mentre la visita a spirale della matrice associata a 5 visita i suoi elementi
# secondo il seguente ordine:
#
# 13 8 7 12 17 18 19 14 9 4 3 2 1 6 11 16 21 22 23 24 25 20 15 10 5
#
# Scrivere un metodo, chiamato spirale, che dato in input un numero
# dispari positivo e dato un numero positivo i tale che 1<=i<=nxn,
# restituisca l'elemento della matrice corrispondente ad n che viene
# visitato per i-esimo. Ad esempio, con n=3 e i=2, il metodo deve
# restituire il valore 2, con n=3 e i=5, il metodo deve
# restituire il valore 7, e, con n=3 e i=8, il metodo deve
# restituire il valore 6. Invece, con n=5 e i=2, il metodo deve
# restituire il valore 8, con n=5 e i=8, il metodo deve
# restituire il valore 14, e, con n=5 e i=15, il metodo deve
# restituire il valore 11.


def generateDistances(n):
    """
    Il problema si puo' risolvere iterando la matrice con una visita spirale, ma
    si puo' anche vedere che c'e' un pattern tra i numeri.
    Ad esempio prendendo la matrice 5x5, i corrispettivi valori della visita
    spirale sono:
    [ 13,  8,  7, 12, 17, 18, 19, 14,  9,  4,   3,   2,   1,  6, 11, 16, 21, 22, 23, 24, 25, 20, 15, 10,  5]
    e le distanze dal centro (13) sono:
    [  0, -5, -6, -1,  4,  5,  6,  1, -4, -9, -10, -11, -12, -7, -2,  3,  8,  9, 10, 11, 12,  7,  2, -3, -8]
    Si puo' notare un patter che lega la dimensione della matrice e il centro:
    [  0, -5, -1,  5,  5,  1,  1, -5, -5, -5,  -1,  -1,  -1,  5,  5,  5,  5,  1,  1,  1,  1, -5, -5, -5, -5]
    -5 e -1 per una volta
     5 e  1 per due volte
    -5 e -1 per tre volte etc.
    Per risolvere il problema si puo' quindi generare una lista contenente le distanze dal centro in O(n)
    e ricavare il risultato in O(1) con center + lista[i - 1]
    """
    countN = 1
    count1 = 1
    sign = -1
    lista = []
    listIndex = 0
    lista.append(0)
    for iterations in range(n):
        for i in range(countN):
            lista.append(n * sign + lista[listIndex])
            listIndex += 1
        for i in range(count1):
            lista.append(1 * sign + lista[listIndex])
            listIndex += 1
        countN += 1
        count1 += 1
        sign *= -1
    return lista[:n**2]


def spiral(listaDistanze, n, i):
    center = (n**2 + 1) / 2
    if i == 0:
        return center
    return center + listaDistanze[i - 1]


if __name__ == '__main__':
    # per eseguire lo script:
    # python spiral.py 5 25
    args = sys.argv
    n = int(args[1])
    i = int(args[2])
    distances = generateDistances(n)
    print "Distanze dal centro ", distances
    print "n: ", n, "i: ", i, " result: ", spiral(distances, n, i)
