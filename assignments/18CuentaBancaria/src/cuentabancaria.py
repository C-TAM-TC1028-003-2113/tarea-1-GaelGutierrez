def main():
    # escribe tu código abajo de esta línea
    saldo_anterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    cheques_exp = int(input('Dame el numero de cheques expedidos: '))
    precio_cheque = 13
    cheques_total = cheques_exp * precio_cheque 
    precant_final = ((saldo_anterior) + (ingresos - egresos) - (cheques_total))
    interes = (precant_final * 0.075)
    cant_final = (precant_final - interes)
    print('El saldo final de la cuenta es de: ', cant_final)
    
if __name__ == '__main__':
    main()