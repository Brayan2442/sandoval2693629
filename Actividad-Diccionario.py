"""diccionario = {
    10: 100,
    20: 300,
    30: 350,
    40: 475,
    50: 525
}

words=[10, 40, 60, 100]

def diccionario1(diccionario):
    print(diccionario)

for word in words:
    if word in diccionario:
        print(word, "->", diccionario[word])
    else:
        print( f"el numero {word} no esta " )"""

diccionario_español_ingles = {"perro": "dog", "gato": "cat"}
diccionario_ingles_español = {"dog": "perro", "cat": "gato"}

def agregar_animal():
    nombre_español = input("Ingrese el nombre del animal en español: ")
    nombre_ingles = input("Ingrese el nombre del animal en inglés: ")

    diccionario_español_ingles[nombre_español] = nombre_ingles
    diccionario_ingles_español[nombre_ingles] = nombre_español

def traducir_español_ingles():
    palabra = input("Ingrese una palabra en español: ")
    if palabra in diccionario_español_ingles:
        traduccion = diccionario_español_ingles[palabra]
        print(f"Traducción al inglés: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def traducir_ingles_español():
    palabra = input("Ingrese una palabra en inglés: ")
    if palabra in diccionario_ingles_español:
        traduccion = diccionario_ingles_español[palabra]
        print(f"Traducción al español: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def mostrar_menu():
    while True:
        print("Menu")
        print("1. Agregar animal")
        print("2. Traducir del español al inglés")
        print("3. Traducir del inglés al español")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_animal()
        elif opcion == "2":
            traducir_español_ingles()
        elif opcion == "3":
            traducir_ingles_español()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente de nuevo.")

mostrar_menu()
















"""diccionario={
                "Rojo": "Red",
                "Verde": "Green",
                "Amarillo": "Yellow",
                "Morado": "Purple",
                "Azul": "Blue",
                "Negro": "Black",
                "Blanco": "White",
                "Cafe": "Coffee",
                "Naranja": "Orange",
                "Rosado": "Pink"

}

    words=['Rojo', 'Verde', 'Azul', 'Dorado']

    for word in words:
        if word in diccionario:
            print(word, "->", diccionario[word])
    else:
        print( f"el color {word} no esta " )"""
