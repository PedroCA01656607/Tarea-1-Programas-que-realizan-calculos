def main():
    #escribe tu código abajo de esta línea
    minu=float(input('Dame los minutos: '))

    v=5.7*60*0.1
    resultado=v*minu
    cm=round(resultado,5)
    print('Centímetros recorridos:',cm)


if __name__ == '__main__':
    main()
