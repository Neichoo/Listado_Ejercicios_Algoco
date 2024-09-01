#Dado n niños, los niños van desde 0 a n-1
#Se mueve hacia la derecha, si es negativo hacia la izquierda
#Undo m, deshacer m tiros de los huevos
ultimas_jugadas = []
#Primer Input almacenado en "ninios" y "numero_pases"
inputcito = str(input())
inputcito_renovao = inputcito.strip().split(" ")
ninios = int(inputcito_renovao[0])
numero_pases = int(inputcito_renovao[1])
#Segundo Input trabajado en un for
inputcito = str(input())
inputcito_renovao = inputcito.strip().split(" ")
input_final = []
contador = 0
pos_huevo = 0
flag = False
for instruccion in inputcito_renovao:
    if (flag == False):
        if (instruccion == "undo"):
            flag = True
            instruccion = inputcito_renovao[contador] + " " + inputcito_renovao[contador + 1]
            input_final.append(instruccion)
        else:
            input_final.append(instruccion)
    else:
        flag = False
    contador += 1
contador = 0
max = ninios - 1
min = 0
for instruccion in input_final:
    if ("undo" in instruccion) and (contador > 0):
        numero_undo = int(instruccion.split(" ")[1])
        for i in range(numero_undo):
            ultima_jugada_ac = ultimas_jugadas.pop()
            if "undo" not in ultima_jugada_ac:
                ultima_jugada_ac = int(ultima_jugada_ac)
                if (ultima_jugada_ac % ninios == 0):
                    pass
                else:
                    pos_huevo = pos_huevo - ultima_jugada_ac
                    while (pos_huevo > max):
                        pos_huevo = pos_huevo - ninios
                    while (pos_huevo < min):
                        pos_huevo = pos_huevo + ninios
    else:
        ultimas_jugadas.append(instruccion)
        pos_huevo = pos_huevo + int(instruccion)
        while (pos_huevo > max):
            pos_huevo = pos_huevo - ninios
        while (pos_huevo < min):
            pos_huevo = pos_huevo + ninios
    contador += 1
print(pos_huevo)