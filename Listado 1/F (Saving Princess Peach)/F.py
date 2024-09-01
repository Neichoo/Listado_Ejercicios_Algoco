"""Se recibe el primer input y se separa en variables"""
inputcito = str(input()).split()
total_obstaculos = int(inputcito[0])
obstaculos_vistos = int(inputcito[1])
"""Inicializar lista para obstaculos saltados, un contador para verificar que no se repitan,
y una lista para los obstaculos que no logro saltar"""
obstaculos_saltados = []
contador_obs_saltados = 0
obstaculos_misseados = []
"""Se itera sobre los obstaculos vistos y se verifica que no se hayan saltado antes, guardandolos
#en la lista de obstaculos saltados y aumentando el contador de obstaculos saltados"""
for i in range(obstaculos_vistos):
    lo_que_mario_salta = int(input())
    if lo_que_mario_salta not in obstaculos_saltados:
        obstaculos_saltados.append(lo_que_mario_salta)
        contador_obs_saltados += 1
"""Se itera sobre el total de obstaculos y se verifica que no se hayan saltado, guardandolos en
la lista de obstaculos que no se lograron saltar"""
for i in range(total_obstaculos):
    if i not in obstaculos_saltados:
        obstaculos_misseados.append(i)
"""Se imprimen todos los obstaculos que no se saltaron y se informa finalmente el total de obstaculos
saltados"""
for obstaculo_misseado in obstaculos_misseados:
    print(obstaculo_misseado) 
print(f"Mario got {contador_obs_saltados} of the dangerous obstacles.")   