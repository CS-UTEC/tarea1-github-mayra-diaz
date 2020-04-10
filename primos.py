texto = input("Escriba la palabra/frase que desea verificar si es un palpindromo: ")
texto2 = ""

for i in texto:
    texto2 = i + texto2

if texto == texto2:
    print("Es palíndromo.")

else:
    print("No es palíndromo.")
    
