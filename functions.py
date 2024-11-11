#J: Aqui van las funciones que usemos para esto :D


def promedio_notas_cuantitativas_todas(cantidad_notas): #J: Calcula el promedio de notas cuando se tienen todas las notas
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

def promedio_notas_cuantitativas_faltan(cantidad_notas,notas_que_faltan):
    cont = 1
    prom = []
    cantidad_notas_total = cantidad_notas-notas_que_faltan
    while cont <= cantidad_notas_total:
        print("")
        nota = float(input(f"Ingrese su nota {cont}: "))
        if 0 <= nota <= 5:  #J: Aqui confirma que la nota este entre 0 y 5, y si no lo esta dice que no esta y no cuenta el valor ingresado dentro de las notas
            prom.append(nota)
            cont += 1
        else:
            print("La nota debe estar entre 0.0 y 5.0")
    
    promedio = sum(prom)/cantidad_notas
    minimo_cada_nota = round((((3-promedio)*cantidad_notas)/notas_que_faltan)+0.1,1)
    if minimo_cada_nota > 5:
        return "mayor a 5.0, lo cual es imposible de obtener, ya que el maximo que puedes sacar en cada nota es 5.0"
    else:
        return f"de {minimo_cada_nota}"

