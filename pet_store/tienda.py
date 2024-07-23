# tienda.py
# Archivo de entrada para la aplicación. Contiene la lógica principal e inicialización.

def main():
    """
    Función principal para iniciar la aplicación de la tienda de mascotas.
    """
    print("***********************************")
    print("*********  BIENVENIDO A  **********")
    print("****  LA TIENDA DE MASCOTAS *******")
    print("***********************************")

    # Variables iniciales para el inventario de mascotas
    num_perros = 10
    num_gatos = 8
    num_pajaros = 25
    num_pez = 50

    # Calcular el total de animales en la tienda
    animales_totales = num_perros + num_gatos + num_pajaros + num_pez

    # Solicitar el nombre y apellido del usuario
    nombre = input("Ingrese su nombre: ")
    print("-----------------------------------")
    apellido = input("Ingrese su apellido: ")

    # Solicitar el género del usuario y validar la entrada
    while True:
        print("-----------------------------------")
        print("\nPor favor ingrese su género:")
        print("\n(F) para Femenino.\n(M) para Masculino.\n")
        print("-----------------------------------")
        genero = input(":").strip().capitalize()
        if genero in ["F", "M"]:
            break
        else:
            print("-----------------------------------")
            print("Entrada no válida, por favor, ingrese:")
            print("(F) para Femenino.\n(M) para Masculino.\n(XX = F) o (XY = M)\n")
            print("-----------------------------------")
            print("        Vuelva a intentarlo        ")

    # Ajustar el saludo según el género
    if genero == "F":
        genero = "Sra."
    else:
        genero = "Sr."
    
    nombre_completo = nombre + " " + apellido  # Concatenar nombre y apellido

    # Mostrar saludo personalizado
    print("-----------------------------------\n")
    print("************************************************")
    print("*                                              *")
    print("*         Saludos, " + genero, nombre_completo + "!          *")
    print("*                                              *")

    while True:
        # Mostrar el menú principal
        print("************************************************")
        print("*                    MENU:                     *")
        print("************************************************")
        print("*                                              *")
        print("* 1: Conocer cuantos animales hay en la tienda *")
        print("*                                              *")
        print("* 2: Comprar un animal                         *")
        print("*                                              *")
        print("* 3: Salir                                     *")
        print("*                                              *")
        print("************************************************")
        print("*           Ingresa una opcion:                *")
        print("================================================")

        # Solicitar la opción del usuario
        respuesta = int(input(":"))
        print("================================================")
        
        if respuesta == 1:
            # Mostrar información sobre los animales en la tienda
            print("\nInformacion de animales en la tienda:")
            print("\nPerros:", num_perros, "\nGatos:", num_gatos, "\nPajaros:", num_pajaros, "\nPeces:", num_pez)
            print("\nEn total tenemos:", animales_totales, "animales\n")
        elif respuesta == 2:
            # Solicitar la especie y cantidad de animales a comprar
            animal = 0
            print("\n¿Que animal deseas comprar, ingrese la cantidad.\n")
            print("1.Perros?""\n2.Gatos?""\n3.Pajaros?""\n4.Pez?""\n5.Desea comprar otro animal?\n")
            print("\nIngresa el numero que identifica el tipo de animal que deseas comprar:")
            print(":")
            animal = int(input())

            if animal == 1:
                animal = "perro"
                print("\nContamos con ", num_perros, animal)
                print("\nIngresa la cantidad que deseas comprar en numeros:")
                print(":")
                cantidad = int(input())
                if cantidad > num_perros:
                    animal = "perros"
                    print("\nDisculpe solo contamos con ", num_perros, animal)
                    print("************************************************")
                    print("\nIngresa la cantidad que deseas comprar nuevamente:")
                    print(":")
                    cantidad = int(input())
                    if cantidad <= num_perros:
                        print("\nExelente!, has comprado ", cantidad, animal)
                    else:
                        print("Disculpe trate mas tarde!")
                elif cantidad <= num_perros:
                    print("\nExelente!, has comprado ", cantidad, animal)
            elif animal == 2:
                animal = "gato"
                print("\nContamos con ", num_gatos, animal)
                print("\nIngresa la cantidad que deseas comprar en numeros:")
                print(":")
                cantidad = int(input())
                if cantidad > num_gatos:
                    animal = "gatos"
                    print("\nDisculpe solo contamos con ", num_gatos, animal)
                    print("************************************************")
                    print("\nIngresa la cantidad que deseas comprar nuevamente:")
                    print(":")
                    cantidad = int(input())
                    if cantidad <= num_gatos:
                        print("\nExelente!, has comprado ", cantidad, animal)
                    else:
                        print("Disculpe trate mas tarde!")
                elif cantidad <= num_gatos:
                    print("\nExelente!, has comprado ", cantidad, animal)
            elif animal == 3:
                animal = "pajaro"
                print("\nContamos con ", num_pajaros, animal)
                print("\nIngresa la cantidad que deseas comprar en numeros:")
                print(":")
                cantidad = int(input())
                if cantidad > num_pajaros:
                    animal = "pajaros"
                    print("\nDisculpe solo contamos con ", num_pajaros, animal)
                    print("************************************************")
                    print("\nIngresa la cantidad que deseas comprar nuevamente:")
                    print(":")
                    cantidad = int(input())
                    if cantidad <= num_pajaros:
                        print("\nExelente!, has comprado ", cantidad, animal)
                    else:
                        print("Disculpe trate mas tarde!")
                elif cantidad <= num_pajaros:
                    print("\nExelente!, has comprado ", cantidad, animal)
            elif animal == 4:
                animal = "pez"
                print("\nContamos con ", num_pez, animal)
                print("\nIngresa la cantidad que deseas comprar en numeros:")
                print(":")
                cantidad = int(input())
                if cantidad > num_pez:
                    animal = "peces"
                    print("\nDisculpe solo contamos con ", num_pez, animal)
                    print("************************************************")
                    print("\nIngresa la cantidad que deseas comprar nuevamente:")
                    print(":")
                    cantidad = int(input())
                    if cantidad <= num_pez:
                        print("\nExelente!, has comprado ", cantidad, animal)
                    else:
                        print("Disculpe trate mas tarde!")
                elif cantidad <= num_pez:
                    print("\nExelente!, has comprado ", cantidad, animal)
            elif animal == 5:
                print("\nPor favor ingrese qué animal le gustaría comprar: ")
                print("************************************************")
                print(":")
                solicitud_animal = input()
                print("************************************************")
                print("Al momento no contamos con:", "(", solicitud_animal ,")", "\nDe ser posible la adquisición de su pedido le estaremos contactando!")
                print("************************************************")
                print("Favor de ingresar su número de teléfono y le llamaremos a la brevedad posible!")
                print("Solo ingrese dígitos, gracias!")
                print("************************************************")
                print(":")
                telefono_cliente = input()
                print("************************************************")
                print("Confirmación de solicitud para:\n", genero, nombre_completo, "\nHa solicitado un/una:", solicitud_animal, "\nNos comunicaremos al:", telefono_cliente, "a la brevedad posible.")
                print("Gracias por visitarnos vuelva pronto", genero, nombre_completo, "!")
            else:
                print("\nTu respuesta no es correcta")
        else:
            print("\nGracias por visitarnos,", genero + apellido, "!!!""\nNos alegra mucho su compra de", "(", cantidad, ")", animal, "!!!" "\nVuelve pronto!")
            break

if __name__ == "__main__":
    main()
