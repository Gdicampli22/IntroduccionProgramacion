"""Actividades parte 1: Iniciando
Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:
Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 
Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo
Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.
En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)
Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.
Nota: para saber si el número i es par hacer i % 2 == 0
"""
nombres = []
while len(nombres) < 10:
    nombre = input("Ingrese un nombre (debe ser único): ").strip()
    if nombre in nombres:
        print("El nombre ya ha sido ingresado. Intente con otro.")
    else:
        nombres.append(nombre)
print("Nombres ingresados:", nombres)

