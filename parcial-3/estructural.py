def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:  # Uso correcto del operador de comparación
            contador += 1
    return contador

print(cuenta_pares([1, 2, 3, 4, 5, 6]))

Este ejercicio muestra cómo un detalle pequeño puede hacer que un programa no funcione.
En este caso, el error fue usar el signo de igual (=) en lugar de doble igual (==). Aunque parece una diferencia mínima, el primero sirve para dar un valor y el segundo para preguntar si algo es igual.
