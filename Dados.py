def dados(): 
    "Devuelve dos numeros aleatorios, del 1 al 6"
    import random 
    return random.sample([1,2,3,4,5,6], 2)

while True:
    [a, b] = dados()

    print("Los dados obtenidos fueron:", [a, b])
    print("La sumatoria es", a+b)

    respuesta = input("Queres tirar otra vez? (S/N) ").strip()[0].lower()

    if respuesta == "n":
        print("Adios!")
        break
    if respuesta != "s":
        print("Error: No se entendio la respuesta. Adios!")
        break
