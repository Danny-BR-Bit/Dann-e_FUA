#J: Aqui van las funciones que usemos para esto :D


def promedio_notas_cuantitativas_todas(cantidad_notas): #J: Calcula el promedio de notas cuando se tienen todas las notas
    cont = 1
    prom = []
    #s = 0
    print("\n"+"La nota debe estar entre 0.0 y 5.0"+"\n")
    while cont <= cantidad_notas:
        nota = float(input(f"Nota #{cont}: ")) #D: Introduje un parche para una mejor visualizacion
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
    print("\n"+"La nota debe estar entre 0.0 y 5.0"+"\n")
    while cont <= cantidad_notas_total:
        print("")
        nota = float(input(f"Nota #{cont}: ")) #D: Lo mismo aqui, parche de visualizacion
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
    
def promedio_notas_cualitativas_todas(cantidad_notas_cualitativas): #D: Aqui se calcula el promedio de notas cualitativas, arrojando un resultado cualitativo
    cont = 1
    Cant_not = 0 #Cantidad de notas
    Sobresaliente = 0
    Muy_Bueno = 0
    Bueno = 0
    Aceptable = 0
    Regular = 0 
    No_Acreditable = 0
    while cont <= cantidad_notas_cualitativas:
        print("")
        print("\nPor favor, ingrese su nota:\n \n(1) Sobresaliente\n(2) Muy Bueno\n(3) Bueno\n(4) Aceptable\n(5) Regular\n(6) No Acreditable\n")
        nota = int(input(f"Nota #{cont}: "))
        if nota == 1:
            Sobresaliente += 1
            Cant_not += 1
            cont += 1
        elif nota == 2:
            Muy_Bueno += 1
            Cant_not += 1
            cont += 1
        elif nota == 3:
            Bueno += 1
            Cant_not += 1
            cont += 1
        elif nota == 4:
            Aceptable += 1
            Cant_not += 1
            cont += 1
        elif nota == 5:
            Regular += 1
            Cant_not += 1
            cont += 1
        elif nota == 6:
            No_Acreditable += 1
            Cant_not += 1
            cont += 1
        else:
            print("La nota ingresada no es valida")
    S = Sobresaliente * 5
    MB = Muy_Bueno * 4.5
    B = Bueno * 4
    A = Aceptable * 3.5
    R = Regular * 3
    NA = No_Acreditable * 1
    Prom = S + MB + B + A + R + NA
    num_prom = round(Prom/Cant_not,1)
    if 0 <= num_prom < 3:
        promedio = "No Acreditable"
    elif 3 <= num_prom < 3.5:
        promedio = "Regular"
    elif 3.5 <= num_prom < 4:
        promedio = "Aceptable"
    elif 4 <= num_prom < 4.5:
        promedio = "Bueno"
    elif 4.5 <= num_prom < 5:
        promedio = "Muy Bueno"
    elif num_prom == 5:
        promedio = "Sobresaliente"
    else:
        print(f"Su promedio se encuentra fuera de los limites del programa y la universidad")
    return promedio

def promedio_notas_cualitativas_faltan(cantidad_notas_cual,notas_que_faltan_cual): #D:Test notas cualitativas
    cont = 1
    Cant_not = 0 #Cantidad de notas
    Sobresaliente = 0
    Muy_Bueno = 0
    Bueno = 0
    Aceptable = 0
    Regular = 0 
    No_Acreditable = 0

    cantidad_notas_total = cantidad_notas_cual-notas_que_faltan_cual
    while cont <= cantidad_notas_total:
        print("")
        print("\nPor favor, ingrese su nota:\n \n(1) Sobresaliente\n(2) Muy Bueno\n(3) Bueno\n(4) Aceptable\n(5) Regular\n(6) No Acreditable\n")
        nota = int(input(f"Nota #{cont}: "))
        if nota == 1:
            Sobresaliente += 1
            Cant_not += 1
            cont += 1
        elif nota == 2:
            Muy_Bueno += 1
            Cant_not += 1
            cont += 1
        elif nota == 3:
            Bueno += 1
            Cant_not += 1
            cont += 1
        elif nota == 4:
            Aceptable += 1
            Cant_not += 1
            cont += 1
        elif nota == 5:
            Regular += 1
            Cant_not += 1
            cont += 1
        elif nota == 6:
            No_Acreditable += 1
            Cant_not += 1
            cont += 1
        else:
            print("La nota ingresada no es valida")
        print("")
    S = Sobresaliente * 5
    MB = Muy_Bueno * 4.5
    B = Bueno * 4
    A = Aceptable * 3.5
    R = Regular * 3
    NA = No_Acreditable * 1
    Prom = S + MB + B + A + R + NA
    num_prom = round(Prom/cantidad_notas_cual,1)

    minimo_cada_nota_cual = round((((3-num_prom)*cantidad_notas_cual)/notas_que_faltan_cual)+0.1,1)
    
    if 0 <= minimo_cada_nota_cual < 3:
        mcnc = "No Acreditable"
        return f"de {mcnc}"
    elif 3 <= minimo_cada_nota_cual < 3.5:
        mcnc = "Regular"
        return f"de {mcnc}"
    elif 3.5 <= minimo_cada_nota_cual < 4:
        mcnc = "Aceptable"
        return f"de {mcnc}"
    elif 4 <= minimo_cada_nota_cual < 4.5:
        mcnc = "Bueno"
        return f"de {mcnc}"
    elif 4.5 <= minimo_cada_nota_cual < 5:
        mcnc = "Muy Bueno"
        return f"de {mcnc}"
    elif minimo_cada_nota_cual == 5:
        mcnc = "Sobresaliente"
        return f"de {mcnc}"
    else:
        return "mayor a sobresaliente, lo cual es imposible de obtener, ya que el maximo que puedes sacar en cada nota es sobresaliente"

def conversor_a_cuantitativo(decision):
    
    if decision == 1:
        cualitativa = "'Sobresaliente' se encuentra entre el siguiente rango: 4.8 a 5.0"
    if decision == 2:
        cualitativa = "'Muy Bueno' se encuentra entre el siguiente rango: 4.5 a 4.7"
    if decision == 3:
        cualitativa = "'Bueno' se encuentra entre el siguiente rango: 4.0 a 4.4"
    if decision == 4:
        cualitativa = "'Aceptable' se encuentra entre el siguiente rango: 3.5 a 3.9"
    if decision == 5:
        cualitativa = "'Regular' se encuentra entre el siguiente rango: 3.0 a 3.4"
    if decision == 6:
        cualitativa = "'No Acreditable' se encuentra entre el siguiente rango: 0.0 a 2.9"
    return cualitativa

def conversor_a_cualitativo(nota): #J: Aqui tome parte de un codigo que usted habia hecho para ahorrar tiempo, por eso las variables tienen un nombre similar
    
    if 0 <= nota < 3:
        mcnc = "No Acreditable"
        return f"de {mcnc}"
    elif 3 <= nota < 3.5:
        mcnc = "Regular"
        return f"de {mcnc}"
    elif 3.5 <= nota < 4:
        mcnc = "Aceptable"
        return f"de {mcnc}"
    elif 4 <= nota < 4.5:
        mcnc = "Bueno"
        return f"de {mcnc}"
    elif 4.5 <= nota < 5:
        mcnc = "Muy Bueno"
        return f"de {mcnc}"
    elif nota == 5:
        mcnc = "Sobresaliente"
        return f"de {mcnc}"
    else:
        return "mayor a sobresaliente, lo cual es imposible de obtener, ya que el maximo que puedes sacar en cada nota es sobresaliente"
