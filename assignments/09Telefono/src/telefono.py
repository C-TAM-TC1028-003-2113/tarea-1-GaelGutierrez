def main():
    # escribe tu código abajo de esta línea
    msj = int(input('Dame el numero de mensajes: '))
    megas = float(input('Dame el numero de megas: '))
    minutos = int(input('Dame el numero de minutos: '))
    precio_fijo = 0.80
    costo_mensual = (msj * precio_fijo) + (megas * precio_fijo) + (minutos * precio_fijo)
    print('El costo mensual es de: ', costo_mensual)


if __name__ == '__main__':
    main()