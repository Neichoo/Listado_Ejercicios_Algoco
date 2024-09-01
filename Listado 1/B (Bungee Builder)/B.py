#N montañas de alturas H1, H2, ..., HN
"""Un puente puede existir entre dos montañas si la altura del puente es a lo más la
altura de la montaña más baja y todas las montañas bajo el puente son más bajas"""
num_mont = int(input())
alturas = list(map(int, input().strip().split()))
maxima_altura = 0
"Inicializar las listas leftarray y rightarray con ceros"
leftarray = [0] * num_mont
rightarray = [0] * num_mont
leftarray[0] = alturas[0]
rightarray[num_mont - 1] = alturas[num_mont - 1]
"Recorrer de izquierda a derecha y de derecha izquierda buscando la mejor altura"
for i in range(1, num_mont):
    leftarray[i] = max(leftarray[i-1], alturas[i])
for i in range(num_mont - 2, -1, -1):
    rightarray[i] = max(rightarray[i + 1], alturas[i])
"Recorrer las alturas y calcular la mejor altura"
for i in range(num_mont):
    altura_puente = min(leftarray[i], rightarray[i])
    maxima_altura = max(maxima_altura, altura_puente - alturas[i])
print(maxima_altura)
