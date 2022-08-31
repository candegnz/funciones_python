# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada

# --------------------------------
def generar_invitados(cantidad_invitados):
    invitados = []

    for i in range(cantidad_invitados):
        print("Ingrese el nombre del invitado", i+1)
        nombre_invitados = str(input())
        invitados.append(nombre_invitados)
    return invitados

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    # lista_invitados = generar_invitados()

    cantidad_invitados = 3
    lista_invitados = generar_invitados(cantidad_invitados)

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)

    lista_invitados_ordenada = ordenar(lista_invitados)

    print("La lista de invitados ordenada es", lista_invitados_ordenada)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("terminamos")
