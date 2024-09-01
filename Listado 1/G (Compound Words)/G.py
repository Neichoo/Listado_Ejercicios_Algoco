"""Lista con las palabras hasta que se acaben las lineas"""
words = []
while True:
    try:
        words += input().split()
    except:
        break
"""Diccionario para guardar las palabras creadas y poder verificar que
no se encuentren repetidas"""
dic = {}
for i, word1 in enumerate(words):
    for j, word2 in enumerate(words):
        if (i != j) or ((word1 + word2) in dic):
            dic[word1 + word2] = 1
            dic[word1 + word2] = 1
"""Transformar el diccionario en una lista y ordenarla"""
lista_d = list(dic.keys())
lista_d.sort()
"""Imprimir las palabras"""
for i in lista_d:
    print(i)