#J: Idea principal: una calculadora de notas que permita calcular el promedio de n cantidad de notas.
#J: Ideas secundarias: que se pueda elegir entre un promedio de notas que solo reciba notas cuantitativas y otro que solo reciba notas cualitativas; 
try:

    from functions import promedio_notas_cuantitativas_todas
    from functions import promedio_notas_cuantitativas_faltan
    from functions import promedio_notas_cualitativas_todas
    from functions import promedio_notas_cualitativas_faltan #D: Querido Jhonatan, por favor, implementa la funcion en el codigo, quedo 100% hecho :D
    from functions import conversor_a_cuantitativo
    from functions import conversor_a_cualitativo
    print("\n"+">"*17+" ¡Bienvenido a Dann-E, tu calculadora de notas de confianza! "+"<"*17+"\n")
    while True:
        print("¿Que proceso deseas realizar hoy?"+"\n"+"\n"+"1. Calculo de promedio de notas cuantitativas."+"\n"+"2. Calculo de promedio de notas cualitativas."+"\n"+"3. Conversor de notas (Cualitativo a Cuantitativo y viceversa)."+"\n"+"4. Salir"+"\n")
        decision = int(input("Ingrese su decision: "))
        if decision == 1: #J: Calculo de promedio de notas cuantitativas.
           print("\n"+"¿Que desea hacer?"+"\n"+"\n"+"1. Promedio de notas."+"\n"+"2. Calculo de notas necesarias para pasar."+"\n"+"3. Volver"+"\n")
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
                 if 0 < notas_que_faltan <= cantidad_notas:
                     print("\n"+f"El valor que debe tener cada una de la(s) {notas_que_faltan} nota(s) que te falta(n) es {promedio_notas_cuantitativas_faltan(cantidad_notas,notas_que_faltan)} para pasar con 3.0"+"\n")
                 elif notas_que_faltan == 0:
                    print("\n"+f"Su promedio cuantitativo es de: {promedio_notas_cuantitativas_todas(cantidad_notas)}"+"\n")
                 else:
                    print("\n"+"La cantidad de notas que faltan no puede ser mayor a la cantidad de notas que desea calcular"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")  
           elif decision == 3:
              None
           else:
              print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
           print("\n"+"Regresando..."+"\n"+"\n")


        elif decision == 2: #J: Calculo de promedio de notas cualitativas.
           print("\n"+"¿Que desea hacer?"+"\n"+"\n"+"1. Promedio de notas."+"\n"+"2. Calculo de notas necesarias para pasar."+"\n"+"3. Volver"+"\n")
           decision = int(input("Ingrese su decision: ")) 
           print("")
           if decision == 1:
              cantidad_notas_cualitativas = int(input("Ingrese la cantidad de notas que va a promediar: "))
              if 1 <= cantidad_notas_cualitativas <= 30: #J: Defini un maximo de 30 notas para promediar, aunque esto puede cambiar
                 print("\n"+f"Su promedio cualitativo es de: {promedio_notas_cualitativas_todas(cantidad_notas_cualitativas)}"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")
           elif decision == 2:
              cantidad_notas = int(input("Ingrese la cantidad total de notas que va a promediar: "))
              if 1 <= cantidad_notas <= 30: #J: Defini un maximo de 30 notas para promediar, aunque esto puede cambiar
                 print("")
                 notas_que_faltan = int(input("Ingrese las notas que no tiene de la cantitad de notas que ingreso: "))
                 if 0 < notas_que_faltan <= cantidad_notas:
                     print("\n"+f"El valor que debe tener cada una de la(s) {notas_que_faltan} nota(s) que te falta(n) es {promedio_notas_cualitativas_faltan(cantidad_notas,notas_que_faltan)} para pasar con 'Regular'"+"\n")
                 elif notas_que_faltan == 0:
                     print("\n"+f"Su promedio cualitativo es de: {promedio_notas_cualitativas_todas(cantidad_notas)}"+"\n")
                 else:
                    print("\n"+"La cantidad de notas que faltan no puede ser mayor a la cantidad de notas que desea calcular"+"\n")
              else:
                 print("\n"+f"¿{cantidad_notas} notas? No creo que pueda hacer eso"+"\n")  
           elif decision == 3:
              None
           else:  
              print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
           print("\n"+"Regresando..."+"\n"+"\n")
                  
        elif decision == 3: #J: Conversor de notas (Cualitativo a cuantitativo y viceversa) nueva funcion yipeeeeeeeee
           print("\n"+"¿Que desea hacer?"+"\n"+"\n"+"1. Convertir una nota Cualitativa a Cuantitativa."+"\n"+"2. Convertir una nota Cuantitativa a Cualitativa."+"\n"+"3. Volver."+"\n")
           decision = int(input("Ingrese su decision: "))
           if decision == 1:
              print("\nPor favor, ingrese su nota:\n \n(1) Sobresaliente\n(2) Muy Bueno\n(3) Bueno\n(4) Aceptable\n(5) Regular\n(6) No Acreditable\n")
              decision = int(input("Ingrese su decision: "))
              if 1 <= decision <= 6:
                 print(f"Su nota {conversor_a_cuantitativo(decision)}.")
              else:
                 print("\n"+"La decision que ingreso es invalida."+"\n")
           elif decision == 2:
              print("\n"+"La nota que va a ingresar debe estar entre 0.0 y 5.0"+"\n")
              nota = float(input("Ingrese su nota: "))
              if 0 <= nota <= 5:
                 print("\n"+"\n"+f"Su nota {round(nota,1)} equivale a {conversor_a_cualitativo(nota)} en la escala cualitativa."+"\n")
              else:
                 print("\n"+"La nota que ingreso es invalida."+"\n")
           elif decision == 3:
              None
           else:
              print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
           print("\n"+"Regresando..."+"\n"+"\n")

        elif decision == 4: #J: Salir
           print("\n"+"¡Hasta luego!"+"\n")
           break
        else:
           print("\n"+"La decision debe ser: 1, 2 o 3."+"\n")
except:
  print("")
  print("*"*15+"ERROR EN EL SISTEMA"+"*"*15)
  print("")
