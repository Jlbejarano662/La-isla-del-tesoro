import os

#Limpia la consola
os.system("cls")

#Algoritmo de la "Isla del Tesoro"
#Para los inputs con selección múltiple, ingresar el número de la opción seleccionada
print("Bienvenido a la Isla del Tesoro, tu misión, si decides aceptarla, es")
print("buscar el tesoro escondido en algún lugar de esta remota isla.")
print("¿Listo para jugar?")
print("1. Sí ")
print("0. No")
respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
print("\n")
if respuesta :
    print("¿Qué camino deseas tomar?")  
    print("1. Derecha")  
    print("0. Izquierda")
    respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
    print("\n")
    if respuesta :
        print("¿Prefieres ir por el laberinto de cuevas o continuar por la selva?")  
        print("1. Laberinto de cuevas")  
        print("0. Selva")
        respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
        print("\n")
        if respuesta :
            print("Decidiste ir por el laberinto de cuevas, caminaste durante") 
            print("7 km y te encontraste un rio subterraneo, despues de nadar unos") 
            print("minutos te has topado con una cascada, ¿Qué vas a hacer?:") 
            print("1. Saltar la cascada") 
            print("0. Bajar escalando por la pared")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta :
                print("Después de 100 m de caída libre has aterrizado en") 
                print("un pozo poco profundo causandote la muerte.") 
                print("JUEGO TERMINADO")
            else :
                print("Después de bajar 100 m escalando por la pared llegaste a") 
                print("un pozo poco profundo ubicado a unos pocos metros de la") 
                print("salida de las cuevas.") 
                print("Al salir encuentras un camino que te lleva a un claro en") 
                print("medio de la selva. En este lugar mueres al ser atacad@ por") 
                print("una tribu nativa de la isla.")    
                print("JUEGO TERMINADO")
        else :
            print("Decidiste ir a través de la selva, caminaste durante") 
            print("10 km hasta encontrar árboles frutales y decides comer algo,") 
            print("¿Qué vas a comer?:") 
            print("1. Arándanos silvestres") 
            print("0. Moras silvestres")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta :
                print("Los arándanos te han dado energía para continuar caminando hasta") 
                print("llegar a un claro en medio de la selva. En este lugar mueres al ser") 
                print("atacad@ por una tribu nativa de la isla.")    
                print("JUEGO TERMINADO")
            else :
                print("Mueres al consumir moras silvestre venenosas.") 
                print("JUEGO TERMINADO")
    else :
        print("Te has topado con un río, ¿prefieres nadar o caminar  hasta encontrar otra") 
        print("manera de cruzar?") 
        print("1. Nadar") 
        print("0. Caminar hasta encontrar un puente")
        respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
        print("\n")
        if respuesta :
            print("Decidiste nadar para cruzar el río, pero a mitad de camino") 
            print("fuiste atacad@ por cocodrilos que te han causado la muerte.") 
            print("JUEGO TERMINADO")
        else :
            print("Decidiste caminar hasta encontrar un puente para cruzar el río.") 
            print("Al llegar al otro lado te has topado con tres puertas, una de color") 
            print("amarillo, otra de color azúl y la última de color rojo. ¿Cuál puerta") 
            print("eliges para continuar?.") 
            print("0. Puerta azúl")
            print("1. Puerta amarilla") 
            print("2. Puerta roja")
            respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
            print("\n")
            if respuesta == 1 :
                print("Acabas de entrar a un cuarto totalmente amarillo, el cuál contiene") 
                print("el siguiente acertijo:") 
                print("Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú.")  
                print("¿Qué es?.")
                respuesta = input("Por favor, escribe tu respuesta: ")
                print("\n")
                if respuesta.lower() == "mi nombre" :
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                else :
                    print("JUEGO TERMINADO")
            elif respuesta == 0 :
                print("Acabas de entrar a un cuarto totalmente helado, en el cual nieva") 
                print("constantemente y solo contiene unos poco materiales parhacer una fogata.") 
                print("¿Lograste encender la fogata y sobrevivir hasta el día siguiente?") 
                print("1. Sí")
                print("0. No")
                respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
                print("\n")
                if respuesta:
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                else :
                    print("Al no poder encender una fogata mueres por congelamiento") 
                    print("JUEGO TERMINADO")
            elif respuesta == 2:
                print("Acabas de ingresar a un cuarto totalmente rojo donde tiene que") 
                print("jugar \"El Piso es Lava\" contra una computadora.") 
                print("¿Logras vencer a la computadora?") 
                print("1. Sí") 
                print("0. No")
                respuesta = int(input("Por favor, ingresa el número de la opción seleccionada: "))
                print("\n")
                if respuesta :
                    print("¡FELICIDADES, ACABAS DE GANAR!")
                else :
                    print("Mueres al caer en lava ardiente.") 
                    print("JUEGO TERMINADO")
else: 
    print("JUEGO TERMINADO")
