# Cierre de calificaciones del Primer Semestre Duoc
# Programa que muestra de cada estudiante los promedios 
# por asignatura y general, además un promedio de las notas
# de cada asignatura. También, permite visualizar los
# estudiantes que aprobaron y reprobaron.
 
import os
os.system("cls")
import re

# Variable estudiantes usando Conjuntos
rut = set()

# Variable nombre y apellido usando Conjunto
estudiantes = {"Ana zuñiga", "Juan Perez"}, {"Carlos Soto"}, {"Pedro Alvarez"}

# Variable notas usando Lista
nombres = []

prom_asign = []

# Tupla de asignaturas
asignaturas_curso = ("Bases de Innovación", "Fundamentos de Programación", "Introducción a Cluod Computing")

# Diccionario de notas: Llave -> nombre, Valor -> lista de tuplas (asignatura, calificación)
calificaciones = {
    "Ana zuñiga": [("Bases", 45), ("Programación", 50), ("Cloud", 68)],
    "Juan Perez": [("Bases", 50), ("Programación", 66), ("Cloud", 60)],
    "Carlos Soto": [("Bases", 60), ("Programación", 48), ("Cloud", 55)],
    "Pedro Alvarez": [("Bases", 55), ("Programación", 65), ("Cloud", 62)],
}

# Calcular promedios por asignatura
for asignatura in asignaturas_curso:
    suma_calificaciones = 0
    for estudiante in estudiantes:
        for materia, calificacion in calificaciones(estudiantes):
            if materia == asignatura:
                suma_calificaciones += calificacion
    promedio = suma_calificaciones // len(estudiantes)
    prom_asign.append([asignatura, promedio])

os.system("cls")

print("")
print("DUOC UC - SEDE SAN BERNARDO")
print("CARRERA: INGENIERÍA EN INFORMÁTICA")
print("----------------------------------")
print("\n                      PROMEDIO DE NOTAS SEMESTRAL")
print("_____________________________________________________________________________")
print("                      Bases de     Fund. de        Introd. a         Promedio")
print("   Nombre            Innovación  Programación   Cloud Computing       General")
print("_____________________________________________________________________________")

# Mostrar los promedios por asignatura
for asignatura, promedio in prom_asign:

# Promedios por asignatura de cada estudiante
    for estudiante, notas in calificaciones.items():
        print(f"{estudiante} {notas[0]} {notas[1]} {notas[2]}")
print("")


# Promedios por asignatura
for asignatura in asignaturas_curso:
    suma_notas = 0
    for nombre in estudiantes:
        for materia, nota in calificaciones[nombre]:
            if materia == asignaturas_curso:
                suma_notas += nota 
    promedio = suma_notas / len(calificaciones)
