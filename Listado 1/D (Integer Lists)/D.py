from collections import deque
#R reversE al deque
#D drop el primer elemento y retorna el resto, "error" si está vacío
#Las funciones pueden ser anidadas en una pura palabra
"""Se recibe el input del numero de casos y se declara una variable
de control de errores"""
number_test_cases = int(input())
errorcito = False
invertido = False
"""Se itera el numero de casos y se recibe el input con las instrucciones y
los elementos del input, luego se transforma a deque, se verfifica si el largo
del deque es igual al especificado anteriormente por el usuario, si no lo es
entonces la variable de control de errores queda como True para imprimir el error
posteriormente.

En el segundo for se itera sobre cada letra de la instruccion, haciendo las
respectivas operaciones y verificando que la deque no esté vacía, si lo está
entonces la variable de control de errores queda como True"""
for i in range(number_test_cases):
    instrucciones = str(input())
    num_elementos_input = int(input())
    if (num_elementos_input > 0):
        elementos_input_deque = deque(map(int, input().strip("[]").split(",")))
    else:
        elementos_input_deque = deque()
        algo = input()
    for instruccion in instrucciones:
        if (instruccion == "R"):
            invertido = not invertido
        elif (instruccion == "D"):
            if (len(elementos_input_deque) == 0):
                errorcito = True
                break
            if (invertido == True):
                elementos_input_deque.pop()
            else:
                elementos_input_deque.popleft()
    if (errorcito == True):
        print("error")
    else:
        print("[{}]".format(",".join(map(str, reversed(elementos_input_deque) if (invertido == True) else elementos_input_deque))))
    errorcito = False
    invertido = False