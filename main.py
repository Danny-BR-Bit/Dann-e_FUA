#J: Idea principal: una calculadora de notas que permita calcular el promedio de n cantidad de notas.
#J: Ideas secundarias: que se pueda elegir entre un promedio de notas que solo reciba notas cuantitativas y otro que solo reciba notas cualitativas; 
try:

    from functions import promedio_notas_cuantitativas_todas
    from functions import promedio_notas_cuantitativas_faltan
    from functions import promedio_notas_cualitativas_todas
    from functions import promedio_notas_cuanlitativas_faltan

    print("\n"+">"*17+" ¡Bienvenido a Dann-E, tu calculadora de notas de confianza! "+"<"*17+"\n")
    while True:
        print("¿Que proceso deseas realizar hoy?"+"\n"+"\n"+"1. Calculo de promedio de notas cuantitativas."+"\n"+"2. Calculo de promedio de notas cualitativas."+"\n"+"3. Salir"+"\n")
        decision = int(input("Ingrese su decision: "))
        if decision == 1: #J: Calculo de promedio de notas cuantitativas.
           print("\n"+"¿Que desea hacer?"+"\n"+"\n"+"1. Promedio de notas."+"\n"+"2. Calculo de notas necesarias para pasar."+"\n"+"3. Salir"+"\n")
           decision = int(input("Ingrese su decision: ")) 
           print("")
           if decision == 1:
              cantidad_notas = int(input("Ingrese la cantidad de notas que va a promediar: "))
              if 1 <= cantidad_notas <= 30: #J: Defini un maximo de 30 notas para promediar, aunque esto puede cambiar
                 print("\n"+f"Su promedio cuantitativo es de: {promedio_notas_cuantitativas_todas(cantidad_notas)}"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")
           elif decision == 2:
              cantidad_notas = int(input("Ingrese la cantidad total de notas que va a promediar: "))
              if 1 <= cantidad_notas <= 30: #J: Defini un maximo de 30 notas para promediar, aunque esto puede cambiar
                 print("")
                 notas_que_faltan = int(input("Ingrese las notas que no tiene de la cantitad de notas que ingreso: "))
                 if notas_que_faltan <= cantidad_notas:
                     print("\n"+f"El valor que debe tener cada una de la(s) {notas_que_faltan} nota(s) que te falta(n) es {promedio_notas_cuantitativas_faltan(cantidad_notas,notas_que_faltan)} para pasar con 3.0"+"\n")
                 else:
                    print("\n"+"La cantidad de notas que faltan no puede ser mayor a la cantidad de notas que desea calcular"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")  
           elif decision == 3:
              print("\n"+"¡Hasta luego!"+"\n")
              break
           else:
              print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")


        elif decision == 2: #J: Calculo de promedio de notas cualitativas.
           print("\n"+"¿Que desea hacer?"+"\n"+"\n"+"1. Promedio de notas."+"\n"+"2. Calculo de notas necesarias para pasar."+"\n"+"3. Salir"+"\n")
           decision = int(input("Ingrese su decision: ")) 
           if decision == 1:
              cantidad_notas_cualitativas = int(input("Ingrese la cantidad de notas que va a promediar: "))
              if 1 <= cantidad_notas_cualitativas <= 30: #J: Defini un maximo de 30 notas para promediar, aunque esto puede cambiar
                 print("\n"+f"Su promedio cualitativo es de: {promedio_notas_cualitativas_todas(cantidad_notas_cualitativas)}"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")
           elif decision == 2:
              print("\n"+"Todavia no hay nada aca"+"\n"+"Vuelve pronto"+"\n") #D: todavia no hay codigo 
           elif decision == 3:
              print("\n"+"¡Hasta luego!"+"\n")
              break
           else:
              print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
           
        elif decision == 3: #J: Salir
           print("\n"+"¡Hasta luego!"+"\n")
           break
        else:
           print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
except:
  print("")
  print("*"*15+"ERROR EN EL SISTEMA"+"*"*15)
  print("")
