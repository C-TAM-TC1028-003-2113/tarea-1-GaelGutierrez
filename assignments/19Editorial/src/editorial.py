def main():
    # escribe tu código abajo de esta línea
    import math
    num_palabras = int(input('Dame el numero de palabras: '))
    total_paginas = math.ceil(num_palabras / 475)
    final = total_paginas * 60
    final_desc = final - (final * 0.10)
    print('El precio de la publicacion es de: ', final_desc)
    
if __name__ == '__main__':
    main()