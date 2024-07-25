def decimal_a_romano(num):
    # Mapa de valores decimales a números romanos
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
 
    # Cadena resultante
    resultado = ""
 
    # Iterar sobre el mapa de valores
    for (decimal, romano) in valores:
        # Mientras el número actual sea mayor o igual al valor decimal
        while num >= decimal:
            # Añadir el símbolo romano a la cadena resultado
            resultado += romano
            # Restar el valor decimal del número
            num -= decimal
 
    return resultado
 
# Ejemplo de uso
numero_decimal = 1987
numero_romano = decimal_a_romano(numero_decimal)
print(f"El número {numero_decimal} en números romanos es {numero_romano}")
