import os
# ---------------------- ALGORITMO ISLA DEL TESORO-----------------------------------------


#-----------------------------------FUNCIONES------------------------------------------

#Función que contiene la lógica del juego 
def juego():
    #Limpia la consola
    os.system("cls")
    #Comienza el juego
    print("Bienvenido a la Isla del Tesoro, tu misión, es buscar el tesoro escondido en algún lugar de esta remota isla. !A la carga¡")
    print("¿Qué camino deseas tomar? \n1. Derecha \n0. Izquierda")
    respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
    print("\n")
    if respuesta :
        print("Depués de caminar unos minutos te has topados con dos caminos y tiene que decidir \npor cuál continuar. ¿Prefieres ir por el laberinto de cuevas o continuar por la selva? \n1. Laberinto de cuevas \n0. Selva")
        respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
        print("\n")
        if respuesta :
            print("Decidiste ir por el laberinto de cuevas, caminaste durante \n7 km y te encontraste un rio subterraneo, despues de nadar unos \nminutos te has topado con una cascada, ¿Qué vas a hacer?: \n1. Saltar la cascada \n0. Bajar escalando por la pared")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta :
                print("Después de 100 m de caída libre has aterrizado en \nun pozo poco profundo causandote la muerte. \nJUEGO TERMINADO")
                volverJugar()
            else :
                print("Después de bajar 100 m escalando por la pared llegaste a \nun pozo poco profundo ubicado a unos pocos metros de la \nsalida de las cuevas. \nAl salir encuentras un camino que te lleva a un claro en \nmedio de la selva. En este lugar mueres al ser atacad@ por \nuna tribu nativa de la isla. \nJUEGO TERMINADO")
                volverJugar()
        else :
            print("Decidiste ir a través de la selva, caminaste durante \n10 km hasta encontrar árboles frutales y decides comer algo, \n¿Qué vas a comer?: \n1. Arándanos silvestres \n0. Moras silvestres")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta :
                print("Los arándanos te han dado energía para continuar caminando hasta \nllegar a un claro en medio de la selva. En este lugar mueres al ser \natacad@ por una tribu nativa de la isla. \nJUEGO TERMINADO")
                volverJugar()
            else :
                print("Mueres al consumir moras silvestre venenosas. \nJUEGO TERMINADO")
                volverJugar()
    else :
        print("Continuas caminando por la selva y te has topado con un río, ¿prefieres nadar o caminar  hasta encontrar otra \nmanera de cruzar? \n1. Nadar \n0. Caminar hasta encontrar un puente")
        respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
        print("\n")
        if respuesta :
            print("Decidiste nadar para cruzar el río, pero a mitad de camino \nfuiste atacad@ por cocodrilos que te han causado la muerte. \nJUEGO TERMINADO")
            volverJugar()
        else :
            print("Decidiste caminar hasta encontrar un puente para cruzar el río. \nAl llegar al otro lado te has topado con tres puertas, una de color \namarillo, otra de color azúl y la última de color rojo. ¿Cuál puerta \neliges para continuar?. \n0. Puerta azúl \n1. Puerta amarilla \n2. Puerta roja")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta == 1 :
                print("Acabas de entrar a un cuarto totalmente amarillo, el cuál contiene \nel siguiente acertijo:")
                print("\tHay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?.")
                respuesta = input("Por favor, escribe tu respuesta: ")
                print("\n")
                if respuesta.lower() == "mi nombre" :
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                    volverJugar()
                else :
                    print("Respuesta incorrecta. \nJUEGO TERMINADO")
                    volverJugar()
            elif respuesta == 0 :
                print("Acabas de entrar a un cuarto totalmente helado, en el cual nieva \nconstantemente y contiene el siguiente acertijo:")
                print("\tAlgunos meses tienen 31 días, otros solo 30.¿Cuantos tienen 28 días?")
                respuesta = input("Por favor, escribe tu respuesta: ")
                print("\n")
                if respuesta.lower() == "todos" :
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                    volverJugar()
                else :
                    print("Respuesta incorrecta. \nJUEGO TERMINADO")
                    volverJugar()
            elif respuesta == 2:
                print("Acabas de ingresar a un cuarto totalmente rojo donde tienes que responder \nel siguiente acertijo:")
                print("\tTarta, pero no es la comida; Mu, pero no el sonido de la vaca; Do, pero no la nota musical ¿Qué es? ")
                respuesta = input("Por favor, escribe tu respuesta: ")
                print("\n")
                if respuesta.lower() == "tartamudo" :
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                    volverJugar()
                else :
                    print("Respuesta incorrecta. \nJUEGO TERMINADO")
                    volverJugar()
            else:
                print("Opción no válida. \nJUEGO TERMINADO")

#Función que permite volver a jugar
def volverJugar():
    print("\n¿Desea jugar de nuevo? \n1.Si \n2.No ")
    jugar = int(input("Por favor, ingresa el número de la opción seleccionada: "))
    if jugar:
        juego()

#------------------------------- EJECUTA EL JUEGO -----------------------------------------------
juego()