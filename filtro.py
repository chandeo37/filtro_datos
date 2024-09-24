#lista inicial de nombres

lista_original = [
"Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes"
]
#separar nombres en grupos
def dividir_nombres(lista_original):
    magos = []
    cientificos = []
    otros = []

    for personajes in lista_original:
        if personajes in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(personajes)
        elif personajes in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(personajes)
        else:
            otros.append(personajes)
    return  magos, cientificos, otros
# Función para modificar la lista de magos
def hacer_grandioso(magos):
    return [f'El gran {mago}' for mago in magos]

# Función para imprimir nombres
def imprimir_nombres(lista_original):
    for nombre in lista_original:
        print(nombre)
# Separar los nombres
magos, cientificos, otros = dividir_nombres(lista_original)

# Imprimir la lista completa antes de ser modificada
print("Lista completa de nombres:")
imprimir_nombres(lista_original)
print()

# Modificar la lista de magos
magos_grandiosos = hacer_grandioso(magos)

# Imprimir los resultados
print("-----------Magos grandiosos:-----------")
imprimir_nombres(magos_grandiosos)
print()

print("-------------Científicos:---------------")
imprimir_nombres(cientificos)
print()

print("--------------Otros:-----------------------")
imprimir_nombres(otros)