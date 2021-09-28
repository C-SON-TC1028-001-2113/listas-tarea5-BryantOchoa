def main():
    #escribe tu código abajo de esta línea
    x = int(input())
    i = 0
    lista = []

    if x>0:
        while i<x :
            valor = input()
            lista.append(valor)
            i = i+1
        print(lista)
        sindups = []
        for i in lista :
            if i not in sindups:
                sindups.append(i)
        print(sindups)
    else:
        print('Error')
    pass

if __name__=='__main__':
    main()
