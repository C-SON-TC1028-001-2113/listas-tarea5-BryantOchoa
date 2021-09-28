def main():
    x = int(input(''))
    y = int(input(''))
    z = x*y
    lista = []
    i=1
    while i<=z:
        i=i+1
        w = int(input(''))
        if w<10:
            lista.append(w)
    print(lista)

if __name__=='__main__':
    main()
