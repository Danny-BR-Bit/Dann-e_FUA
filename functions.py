#j: Aqui van las funciones que usemos para esto :D
def promedio_notas_cuantitativas(cantidad_notas):
    cont = 1
    prom = []
    while cont <= cantidad_notas:
        print("")
        nota = float(input(f"Ingrese su nota {cont}: "))
        if 0 <= nota <= 5:  #J: Aqui confirma que la nota este entre 0 y 5, y si no lo esta dice que no esta y no cuenta el valor ingresado dentro de las notas
            prom.append(nota)
            cont += 1
        else:
            print("La nota debe estar entre 0.0 y 5.0")
        
    promedio = round(sum(prom)/len(prom),1)
    return promedio
