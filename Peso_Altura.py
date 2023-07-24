# Pedimos al usuario que ingrese su nombre

nombre = input("Por favor, ingresa tu nombre: ")

# Mostramo saludo personalizado

print("Hola, " + nombre + " ¡Bienvenido! Te pediremos una serie de información para calcular tu IMC")

# Pedimos información del peso al usuario en kg

peso_kg = float(input("Por favor " + nombre + " Ingrese su peso en kg: "))

# Pedimos al usuario su estatura en metros

estatura_metros = float(input("Por favor " + nombre + " ahora ingresa tu estatura en metros: "))

# Calculamos el índice de masa corporal (IMC)

imc = peso_kg / (estatura_metros ** 2)

# Mostramos el IMC 

print(nombre + " ,su índice de masa corporal (IMC) es: {:.2f}".format(imc))