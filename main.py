#Idea principal: una calculadora de notas que permita calcular el promedio de n cantidad de notas.
#Ideas secundarias: que se pueda elegir entre un promedio de notas que solo reciba notas cuantitativas y otro que solo reciba notas cualitativas; 

from functions import promedio_notas

cantidad_notas = int(input("Ingrese la cantidad de notas que va a promediar: "))

print(promedio_notas(cantidad_notas))

