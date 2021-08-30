def main():
    # escribe tu código abajo de esta línea
    juego_nuevo = 1000
    juego_usado = 350
    result_nuevos = int(input('Dame la cantidad de juegos nuevos que compraste: '))
    result_usados = int(input('Dame la canitdad de juegos usados que compraste: '))
    print('El total de la compra es:', (result_nuevos * juego_nuevo) + (result_usados * juego_usado)) 


if __name__ == '__main__':
    main()
