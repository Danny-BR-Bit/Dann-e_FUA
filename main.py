#J: Idea principal: una calculadora de notas que permita calcular el promedio de n cantidad de notas.
#J: Ideas secundarias: que se pueda elegir entre un promedio de notas que solo reciba notas cuantitativas y otro que solo reciba notas cualitativas; 
try:

    from functions import promedio_notas_cuantitativas

    print("\n"+">"*17+" ¡Bienvenido a Dann-E, tu calculadora de notas de confianza! "+"<"*17+"\n")
    print("¿Que proceso deseas realizar hoy?"+"\n"+"\n"+"1. Calculo de promedio de notas cuantitativas."+"\n"+"2. Calculo de promedio de notas cualitativas."+"\n"+"3. Salir"+"\n")
    while True:
        decision = int(input("Ingrese su decision: "))
        if decision == 1:
           cantidad_notas = int(input("Ingrese la cantidad de notas que va a promediar: "))
           print("\n"+f"Su promedio cuantitativo es de: {promedio_notas_cuantitativas(cantidad_notas)}"+"\n")
        elif decision == 2:
           print("Hola Mundo") #J: Aqui toca programar la segunda opcion que es la cualitativa, pero mientras hacemos eso puse este hola mundo para que el codigo no diera error :)
        elif decision == 3:
           print("\n"+"¡Hasta luego!"+"\n")
           break
        else:
           print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
except:
  print("")
  print("*"*15+"ERROR EN EL SISTEMA"+"*"*15)
  print("")

