
my_other_list = [35, 1.77, "Stephanie", "Sourname"]

### Lists ###

# Definición
# Declaración de una lista
print("Declaración de listas vacías")
my_list = list()
my_other_list = []

print(len(my_list))

print("Asignación de valores a my_list")
my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

print("***Asignación de valores a my_other_list***")
my_other_list = [35, 1.77, "Stephanie", "Sourname"]

print(type(my_list))
print(type(my_other_list))
print("------")
# Acceso a elementos y búsqueda
print("***Acceso a elementos y búsqueda en my_other_list***")
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Sourname"))

print("***Desempaquetado de my_other_list***")
age, height, name, surname = my_other_list
print(surname)

print("***Asignación de elementos de my_other_list a variables***")
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(height)
print("------")
print("***Creación de una nueva lista mi_lista***")
mi_lista = [10, 20, 30, 40]
longitud = len(mi_lista)
print(longitud)  # Salida: 4
print("------")
# Concatenación
print("***Concatenación de my_list y my_other_list***")
print(my_list + my_other_list)
# print(my_list - my_other_list)
print("------")
# Creación, inserción, actualización y eliminación
print("***Añadir un elemento a my_other_list***")
my_other_list.append("Agregar_elemento")
print(my_other_list)
print("------")
print("***Insertar un elemento en my_other_list***")
my_other_list.insert(1, "Rojo")
print(my_other_list)
print("------")
print("***Actualizar un elemento en my_other_list***")
my_other_list[1] = "Azul"
print(my_other_list)
print("------")
print("***Eliminar un elemento de my_other_list***")
my_other_list.remove("Azul")
print(my_other_list)
print("------")
print("***Eliminar un elemento de my_list***")
my_list.remove(30)
print(my_list)
print("------")
print("***Eliminar el último elemento de my_list***")
print(my_list.pop())
print(my_list)
print("------")
print("***Eliminar un elemento específico de my_list***")
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
print("------")
print("***Eliminar el último elemento de mi_lista***")
mi_lista = [1, 2, 3, 10]
ultimo_elemento = mi_lista.pop()  # 4
print(ultimo_elemento)
print(mi_lista)
print("------")
"""
Comportamiento de pop():
Si no se proporciona un índice, se elimina y devuelve el último elemento de la lista.
Si se proporciona un índice, pop() eliminará el elemento en esa posición y lo devolverá.
Si intentas hacer pop() en una lista vacía, se lanzará un error IndexError.
"""

print("***Eliminar un elemento por índice en my_list***")
del my_list[2]
print(my_list)
print("------")


# Operaciones con listas
print("***Copiar my_list a my_new_list***")
my_new_list = my_list.copy()
print("------")

print("***Limpiar my_list***")
my_list.clear()
print(my_list)
print(my_new_list)
print("------")

print("***Revertir my_new_list***")
my_new_list.reverse()
print(my_new_list)
print("------")

print("***Ordenar my_new_list***")
my_new_list.sort()
print(my_new_list)
print("------")
# Sublistas
print("***Obtener una sublista de my_new_list***")
print(my_new_list[1:3])
print("------")


# Cambio de tipo
print("***Cambiar el tipo de my_list a string***")
my_list = "Hola Python"
print(my_list)
print(type(my_list))
print("------")
"""
1. DECLARAR UNA LISTA 
2. Declarar una lista con mas de 5 elementos
3. Encontrar la longitud de la lista
4.Obtener el primer elemento, el elemento de en medio y el último elemento de la lista
5. Declarar una lista llamada datos_mixtos en el que se ponga su nombre, edad, altura, estado
"""

print("***Declarar una lista datos_lista***")
datos_lista = [10, 20, 30, 40, 50, 60]
print(datos_lista)
print("------")
print("***Encontrar la longitud de datos_lista***")
longitud = len(datos_lista)
print(longitud)
print("------")
print("***Obtener el primer, medio y último elemento de datos_lista***")
elemento_medio = datos_lista[len(datos_lista) // 2]
print(datos_lista[0])
print(datos_lista[2])
print(datos_lista[5])
print("Elemento del medio", elemento_medio)
print("------")
print("***Declarar una lista de datos mixtos***")
datos_mixtos = ["mitzi", 20, 1.70, "yucatan"]
print(datos_mixtos)
print("------")
print("Declarar una lista vacía mi_lista_a")
mi_lista_a = []
print(f"Mi Lista: {mi_lista_a}")

print("Declarar una lista vacía mi_lista_a")
mi_lista_a = []
print(f"Mi Lista: {mi_lista_a}")

print("Declarar una lista mi_lista_b con elementos")
mi_lista_b = [1, 3, 5, 7, 9, 11, 13, 15]
print(f"Mi Lista: {mi_lista_b}")

print("Encontrar la longitud de mi_lista_b")
longitud = len(mi_lista_b)
print(f"La longitud de mi Lista: {longitud}")

print("Obtener el primer, medio y último elemento de mi_lista_b")
print(f"El primer elemento es: {mi_lista_b[0]}")
print(f"El medio elemento es: {mi_lista_b[4]}")
print(f"El último elemento es: {mi_lista_b[-1]}")

print("Declarar una lista mi_lista_a con datos mixtos")
mi_lista_a = ["Raul", 60, 1.77, "Guanajuato"]
print(f"Mi Lista: {mi_lista_a}")

