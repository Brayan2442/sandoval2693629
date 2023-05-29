
Colores={
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
    if word in Colores:
        print(word, "->", Colores[word])
    else:
        print( f"el color {word} no esta " )


