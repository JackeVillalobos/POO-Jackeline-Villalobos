
def compute_pay(horas, tarifa):
    if (horas > 40):
        return 40 * tarifa + (horas - 40) * tarifa * 1.5
    else:
        return 40 * tarifa

try:
    horas = float(input('Ingrese el número de horas: '))
    tarifa = float(input('Ingrese la tarifa: '))
    
    print('Salario es igual: ', compute_pay(horas, tarifa))
except ValueError:
   print ("Error, introduzca un numero")