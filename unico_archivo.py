#En este archivo cada equipo creará las funciones necesarias para resolver lo que le corresponde, 
#el main del programa es el mismo para todos, cada equipo debe crear un función principal la cual es 
#llamada por la función main que es la que tiene el menú


if __name__== "__main__":
  while True:
    print("""
    Menú:
    1. Ejercicio 1.
    2. Ejercicio 2.
    3. Ejercicio 3.
    4. Ejercicio 4.
    """)
    
    # print(comentario)
    # ckurbneiruvneirugn
    opcion = input("Elige una opción: ")    
    lista_str = input("ingrese numeros separados por comas: ")
    numeros_lista = [int(numero) for numero in lista_str.replace(" ", "").split(",")]
    def formas_subir_escaleran(n):
        if n <= 1:
            return 1
        else:
            return formas_subir_escaleran(n - 1) + formas_subir_escaleran(n - 2)
    #!----------------------------------------------------------------
    def obtener_numeros_negativos(lista):
        numeros_lista = []
        for numero in lista:
            if numero < 0:
                numeros_lista.append(numero)
        return numeros_lista
    #!----------------------------------------------------------------
    def numeros_positivos(numeros_lista):
        positivos = []
        for numero in numeros_lista:
            if numero > 0:
                positivos.append(numero)
        return positivos
    #!----------------------------------------------------------------
    if opcion == "1":
        ejercicio1 = formas_subir_escaleran(4)
    elif opcion == "2":
        negativos = obtener_numeros_negativos(numeros_lista)
        ejercicio2= print(negativos)
    elif opcion == "3":
        ejercicio3 = print(numeros_positivos(numeros_lista))
    elif opcion == "4":
        escalones = ejercicio1+ejercicio2+ejercicio3
        print (formas_subir_escaleran(escalones))
## identificacion del archivo en la rama master