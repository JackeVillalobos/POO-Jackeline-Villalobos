def convertir(celsius):
    return 9/5 * celsius + 32

leyendo = True
while leyendo:
    try:
        celsius = float(input("Introduzca temperatura en grados Celsius: "))
        leyendo = False
    except:
        print("Introduzca un valor numérico\n")

print ("La temperatura equivalente en grados Fahrenheit es :", convertir(celsius))