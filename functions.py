#Aqui van las funciones que usemos para esto :D
def promedio_notas(cantidad_notas):
    cont = 1
    prom = []
    while cont <= cantidad_notas:
        nota = float(input(f"Ingrese su nota {cont}: "))
        prom.append(nota)
        cont += 1
    promedio = round(sum(prom)/len(prom),1)
    return promedio
