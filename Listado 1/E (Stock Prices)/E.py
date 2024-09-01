#Ask price el minimo
#Bid price el maximo
#Stock price el ultimo precio acordado y hecho
#Si bid price es mejor o igual al ask price, se hace el trato
#Una orden de compra se iguala con uno de venta que exige el precio de venta
num_ord = int(input())
for i in range(num_ord):
    ord_type = int(input())
    ultimo_trato = "-"
    ventas = {}
    compras = {}
    for j in range(ord_type):
        inputcito = input().strip().split()
        tipo = inputcito[0]
        cuanto = int(inputcito[1])
        precio = int(inputcito[-1])
        if (tipo == "sell"):
            if (precio in ventas):
                ventas[precio] += cuanto
            else:
                ventas[precio] = cuanto
        elif (tipo == "buy"):
            if (precio in compras):
                compras[precio] += cuanto
            else:
                compras[precio] = cuanto
        #Siempre que no esté vacío, iterar
        while (compras and ventas):
            max_compra = max(compras.keys())
            min_venta = min(ventas.keys())
            if (max_compra >= min_venta):
                ultimo_trato = min_venta
                if (compras[max_compra] > ventas[min_venta]):
                    compras[max_compra] -= ventas[min_venta]
                    del ventas[min_venta]
                elif (compras[max_compra] < ventas[min_venta]):
                    ventas[min_venta] -= compras[max_compra]
                    del compras[max_compra]
                else:
                    del compras[max_compra]
                    del ventas[min_venta]
            else:
                break
        #Datos a imprimir
        venta_ac = min(ventas.keys()) if ventas else "-"
        compra_ac = max(compras.keys()) if compras else "-"
        print(f"{venta_ac} {compra_ac} {ultimo_trato}")
