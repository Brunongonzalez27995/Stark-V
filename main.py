import re
import json
from funciones import *
from data_stark import *

def leer_archivo(nombre_archivo:str) -> str or bool:
    try:
        archivo = open(nombre_archivo, "r", encoding = 'utf-8')
        contenido = archivo.readlines()
        archivo.close()
    except:
        contenido = False
    return contenido

def guardar_archivo(nombre_archivo:str, contenido:str) -> bool:
    try:
        archivo = open(nombre_archivo, "w+", encoding = 'utf-8')
        archivo.write(contenido)
        archivo.close()
        print("Se creó el archivo: {0}".format(nombre_archivo))
        retorno = True
    except:
        print("Error al crear el archivo: {0}".format(nombre_archivo))
        retorno = False
    return retorno

def generar_csv(nombre_archivo:str, lista:list) -> bool:
    if lista == []:
        retorno = False
    else:
        try:
            cabecera = str(",".join(lista[0].keys())) + "\n"
            guardar_archivo(nombre_archivo, cabecera)
            archivo = open(nombre_archivo, "a", encoding = 'utf-8')
            for elemento in lista:
                fila = ",".join(str(valor) for valor in elemento.values()) + "\n"
                archivo.write(fila)
            archivo.close()
            retorno = True
        except:
            print("Error al generar el string.")
            retorno = False
        return retorno

def leer_csv(nombre_archivo:str) -> bool or list: 
    archivo = open(nombre_archivo, "r", encoding = 'utf-8') #Abre el archivo en modo lectura.
    lista_archivo = archivo.readlines() #Genera una lista con el contenido del archivo.
    cabecera = lista_archivo[0] #Obtiene la primera linea que contendrá las claves.
    claves_modificadas = re.sub("\n", "", cabecera) #Modifica los saltos de linea por un espacio vacio.
    claves_lista = claves_modificadas.split(",") #Separa por coma las claves generando una lista de claves.
    lista_final = [] #Creo una lista vacía para añadir los diccionarios.
    
    try:
        for linea in range(1, len(lista_archivo)):
            valor = lista_archivo[linea] #Asigno a valor la linea actual.
            lista_actual = valor.split(",") #Separo la linea por comas.
            contador_clave = -1 #Genero un contador que me ayudará a recorrer la lista de claves.
            diccionario = {} #Genero un diccionario vacío que luego agregaré a la lista final.
            for valor in lista_actual: 
                if contador_clave > len(claves_lista): #Si el contador supera la cantidad de claves...
                    contador_clave = 0 #Se asignará 0 al contador.
                else:
                    contador_clave += 1 #Si no, sumo 1 al contador para conseguir la siguiente clave.
                diccionario[claves_lista[contador_clave]] = valor #Asigno el valor y la clave al diccionario.
                #Siendo claves_lista[contador_clave] la clave y la posición en la lista de claves...
                # y valor el valor actual de la lista de la linea que estoy recorriendo en el primer for.
            lista_final.append(diccionario) #Appendeo el diccionario a la lista final.
            retorno = lista_final

    except:
        print("Error al generar la lista.")
        retorno = False

    archivo.close() #Cierro el archivo.
    return retorno

def generar_json(nombre_archivo:str, lista:list, nombre_lista:str) -> bool:
    if lista == []:
        retorno = False #Si la lista se encuentra vacía devuelve False y muestra un mensaje de error.
        print("La lista se encuentra vacía.")
    else:
        try:
            for elemento in lista: #Sanitizo los datos de la lista.
                sanitizar_dato(elemento, "altura", "flotante")
                sanitizar_dato(elemento, "peso", "flotante")
                sanitizar_dato(elemento, "fuerza", "entero")
            try:
                archivo = open(nombre_archivo, "w+", encoding = 'utf-8') #Abro/creo el archivo en modo escritura.
                #Genero un diccionario que contendrá el tercer parametro y la lista.
                lista_a_guardar = {nombre_lista : lista}
                #Escribo sobre el archivo el diccionario anteriormente creado, utilizando la librería json.
                json.dump(lista_a_guardar, archivo, indent = 4)
                archivo.close() #Cierro el archivo.
                retorno = True #Devuelvo True en caso de generar correctamente el archivo.
                print("Se creó correctamente {0}".format(nombre_archivo)) #Mensaje de archivo creado.
            except:
                print("Error al normalizar los datos.") #Muestro error en caso de alguna exepción.
                retorno = False #Devuelvo False en dicho caso.
        except:
            print("Error al generar archivo .json") #Muestro error en caso de no poder generar el archivo.
            retorno = False #Devuelvo False en dicho caso.

    return retorno #Devuelve True o False según se haya podido crear el archivo json.

def leer_json(nombre_archivo:str, nombre_lista:str) -> list or bool:
    try:
        archivo = open(nombre_archivo, "r")
        lista_creada = json.load(archivo)
        retorno = lista_creada[nombre_lista]

    except:
        retorno = False
        print("Error al abrir el archivo.")

    return retorno

def ordenar_por_clave_ascendente(lista:list, clave:str) -> list or bool:
    try:
        for elemento in lista:
            sanitizar_dato(elemento, "altura", "flotante")
            sanitizar_dato(elemento, "peso", "flotante")
            sanitizar_dato(elemento, "fuerza", "entero")

        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if(lista[i][clave] > lista[j][clave]):
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
        retorno = lista
    except:
        retorno = False
        print("Error al ordenar la lista.")

    return retorno

def ordenar_por_clave_descendente(lista:list, clave:str) -> list or bool:
    try:
        for elemento in lista:
            sanitizar_dato(elemento, "altura", "flotante")
            sanitizar_dato(elemento, "peso", "flotante")
            sanitizar_dato(elemento, "fuerza", "entero")

        for i in range(len(lista)-1):
            for j in range(i+1, len(lista)):
                if(lista[i][clave] < lista[j][clave]):
                    auxiliar = lista[i]
                    lista[i] = lista[j]
                    lista[j] = auxiliar
        retorno = lista
    except:
        retorno = False
        print("Error al ordenar la lista.")

    return retorno

def ordenar_por_clave(lista:list):
    retorno = False
    while retorno == False:
        opcion = input("\n1.Ordenar por clave.\n2.Salir al menú.\nIngrese una opción: ")
        if opcion == "1":
            while True:
                opcion_clave = input("Ingrese por qué clave desea ordenar.\n1.Por fuerza.\
                                            \n2.Por peso.\n3.Por altura.\n4.Volver.\nIngrese su opción: ")
                opcion_ordenamiento = input("Ingrese como ordenarlo.\n1.Ascendente.\n2.Descendente.\n3.Volver.\
                                                                            \nIngrese una opción: ")
                if opcion_clave == "1" and opcion_ordenamiento == "1":
                    retorno = ordenar_por_clave_ascendente(lista, "fuerza")
                    break
                elif opcion_clave == "1" and opcion_ordenamiento == "2":
                    retorno = ordenar_por_clave_descendente(lista, "fuerza")
                    break
                elif opcion_clave == "2" and opcion_ordenamiento == "1":
                    retorno = ordenar_por_clave_ascendente(lista, "peso")
                    break
                elif opcion_clave == "2" and opcion_ordenamiento == "2":
                    retorno = ordenar_por_clave_descendente(lista, "peso")
                    break
                elif opcion_clave == "3" and opcion_ordenamiento == "1":
                    retorno = ordenar_por_clave_ascendente(lista, "altura")
                    break
                elif opcion_clave == "3" and opcion_ordenamiento == "2":
                    retorno = ordenar_por_clave_descendente(lista, "altura")
                    break
                elif opcion_clave not in ["1", "2", "3", "4"] or opcion_ordenamiento not in ["1", "2", "3"]:
                    print("Ingrese una opción correcta.")
                elif opcion_clave == "4" or opcion_ordenamiento == "3":
                    break
        elif opcion == "2":
            retorno = False
            break
        else:
            print("Introduzca una opción valida.")

    return retorno

def stark_5_menu(lista:list):
    normalizados = False
    while normalizados == False:
        opcion = input("1.Normalizar datos.\n2.Salir de S.T.A.R.K V\nIngrese una opción: ")
        if opcion == "1":
            try: 
                for elemento in lista:
                    sanitizar_dato(elemento, "altura", "flotante")
                    sanitizar_dato(elemento, "peso", "flotante")
                    sanitizar_dato(elemento, "fuerza", "entero")

                normalizados = True
                print("Datos normalizados con éxito.")
            except:
                print("Error al normalizar los datos.")
        elif opcion == "2":
            print("Saliendo de S.T.A.R.K V")
            break
        else:
            print("Ingrese una opción valida.")
    while True:
        opcion = input("1.Generar CSV\n2.Listar heroes del archivo CSV ordenados por altura ASC.\
                       \n3.Generar JSON.\n4.Listar heroes del archivo JSON ordenados por peso DESC.\
                       \n5.Ordenar Lista por fuerza.\n6.Salir\nIngrese una opción: ")
        if opcion == "1":
            nombre_csv = input("Ingrese el nombre del archivo que quiere generar: ")
            lista_csv = generar_csv(nombre_csv, lista)
        if opcion == "2":
                nombre_csv = input("Ingrese el nombre del archivo que quiere ordenar: ")
                lista_archivo = leer_csv(nombre_csv)
                lista_ordenada_altura_ascendente = ordenar_por_clave_ascendente(lista_archivo, "altura")
                try:
                    for elemento in lista_ordenada_altura_ascendente:
                        try:
                            print(f"Nombre del héroe: {elemento['nombre']}")
                            print(f"Altura del héroe: {elemento['altura']}")
                        except:
                            print("Problema con los datos del heroe.")
                except:
                    print("Error: Nombre del archivo incorrecto.")
        elif opcion == "3":
            nombre_archivo_json = input("Ingrese el nombre del archivo que quiere generar: ")
            nombre_lista_json = input("Ingrese el nombre de la lista que quiere generar: ")
            generar_json(nombre_archivo_json, lista, nombre_lista_json)
        elif opcion == "4":
            nombre_archivo_json = input("Ingrese el nombre del archivo que quiere ordenar: ")
            nombre_lista_json = input("Ingrese el nombre de la lista que quiere ordenar: ")
            lista_json = leer_json(nombre_archivo_json, nombre_lista_json)
            if lista_json:
                lista_ordenada = ordenar_por_clave_descendente(lista_json, "peso")
                try:
                    for elemento in lista_ordenada:
                        print("Nombre del héroe: {}".format(elemento["nombre"]))
                        print("Peso del héroe: {}".format(elemento["peso"]))
                except:
                    print("Problema con los datos del héroe.")
            else:
                print("Error: Nombre del archivo incorrecto.")
        elif opcion == "5":
            opcion = input("1.Ascendente.\n2.Descendente.\nIngrese cómo quiere ordenar la lista por fuerza: ")
            if opcion == "1":
                lista_ordenada = ordenar_por_clave_ascendente(lista, "fuerza")
                for elemento in lista_ordenada:
                    print("Nombre del héroe: {}".format(elemento["nombre"]))
                    print("Fuerza del héroe: {}".format(elemento["fuerza"]))
            elif opcion == "2":
                lista_ordenada = ordenar_por_clave_descendente(lista, "fuerza")
                for elemento in lista_ordenada:
                    print("Nombre del héroe: {}".format(elemento["nombre"]))
                    print("Fuerza del héroe: {}".format(elemento["fuerza"]))
            else:
                print("Ingrese una opción correcta.")
        elif opcion == "6":
            print("Saliendo de S.T.A.R.K V")
            break

stark_5_menu(lista_personajes)