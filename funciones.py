import re

def stark_normalizar_datos(lista:list):#FALTA COMENTAR
    if lista != [] and type(lista) == list: #Si no está vacía y lo que pasamos por parametro es una lista entonces...
        for elemento in lista: #Recorro la lista.
            sanitizar_altura = sanitizar_dato(elemento, "altura", "float")#Normalizo todos los datos con las funciones anteriores.
            sanitizar_peso = sanitizar_dato(elemento, "peso", "entero")
            sanitizar_color_ojos = sanitizar_dato(elemento, "color_ojos", "string")
            sanitizar_color_pelo = sanitizar_dato(elemento, "color_pelo", "string")
            sanitizar_fuerza = sanitizar_dato(elemento, "fuerza", "entero")
            sanitizar_inteligencia = sanitizar_dato(elemento, "inteligencia", "string")
        print("Datos normalizados")
    else:
        print("Lista se encuentra vacía.")#Si no se cumple la primera condición, imprime un mensaje de error.

def sanitizar_entero(numero_a_sanitizar:str or int or float) -> int:
    if type(numero_a_sanitizar) != str:
        retorno = numero_a_sanitizar
    else:
        dato_a_analizar = numero_a_sanitizar.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
        dato_a_analizar = numero_a_sanitizar
        buscar_numero = re.search(r"[0-9]+", dato_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
        buscar_digitos = re.search(r"[a-zA-Z]+", dato_a_analizar) #Utiliza expresiones regulares para buscar letras mayusculas o minusculas.
        buscar_caracteres = re.search(r"[\W]+", dato_a_analizar) #Utiliza expresiones regulares para encontrar caracteres especiales.

        if buscar_numero: #Si se encontró uno o más dígitos numericos...
            es_negativo = re.search(r"^-", dato_a_analizar) #Busca "-" al principio de la cadena.
            if es_negativo:
                retorno = -2 #Si se encuentra un "-" al principio de la cadena, devolverá -2 indicando que es un número negativo.
            else: #Si no es negativo intentará castear el STR a INT.
                try:
                    retorno = int(dato_a_analizar) #Castea a INT el STR pasado por parametro.
                except:
                    retorno = -3 #En caso de no ser posible por alguna razón devuelve -3.
        elif buscar_numero == None: #Si no encontró números en la cadena...
            if buscar_caracteres or buscar_digitos:  #Si tiene caracteres especiales o letras minusculas o mayúsculas...
                retorno = -1 #Asigna -1 al retorno, indicando que encontró caracteres/letras en la cadena.
            else:
                retorno = -3 #Asigna -3 al retorno en caso de otros posibles errores.

    return retorno #Devuelve el retorno que podrá ser -1 en caso de caracteres no numericos. -2 en caso de numeros negativos. 
    # -3 En otros casos, en caso de que el STR sea un número positivo, entonces lo casteara a entero y lo asignará a retorno.

def sanitizar_flotante(numero_a_sanitizar:str) -> float or int:
    if type(numero_a_sanitizar) != str:
        retorno = numero_a_sanitizar
    else:
        dato_a_analizar = numero_a_sanitizar.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
        buscar_numero_flotante = re.search(r"[0-9]+\.[0-9]+", dato_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
        buscar_digitos = re.search(r"[a-zA-Z]+", dato_a_analizar) #Utiliza expresiones regulares para buscar letras mayusculas o minusculas.
        buscar_caracteres = re.search(r"[\W]+", dato_a_analizar) #Utiliza expresiones regulares para encontrar caracteres especiales.

        if buscar_numero_flotante: #Si se encontró uno o más números seguido de un "." y otro número o más numeros...
            es_negativo = re.search(r"^-", dato_a_analizar) #Busca "-" al principio de la cadena.
            if es_negativo:
                retorno = -2 #Si se encuentra un "-" al principio de la cadena, devolverá -2 indicando que es un número negativo.
            else: #Si no es negativo intentará castear el STR a INT.
                try:
                    retorno = float(dato_a_analizar) #Castea a FLOAT el STR pasado por parametro.
                except:
                    retorno = -3 #En caso de no ser posible por alguna razón devuelve -3.
        elif buscar_numero_flotante == None: #Si no encontró flotantes en la cadena...
            if buscar_caracteres or buscar_digitos:  #Si tiene caracteres especiales o letras minusculas o mayúsculas...
                retorno = -1 #Asigna -1 al retorno, indicando que encontró caracteres/letras en la cadena.
            else:
                retorno = -3 #Asigna -3 al retorno en caso de otros posibles errores.

    return retorno #Devuelve el retorno que podrá ser -1 en caso de caracteres no numericos. -2 en caso de numeros negativos. 
    # -3 En otros casos, en caso de que el STR sea un número positivo flotante, entonces lo casteara a float y lo asignará a retorno.

def sanitizar_string(cadena:str) -> str:
    cadena_a_analizar = cadena.strip() #Quita los espacios vacíos en la cadena pasada por parametro.
    buscar_numero = re.search(r"[0-9]+", cadena_a_analizar) #Utiliza expresiones regulares para buscar uno o más digitos numericos.
    if buscar_numero: #Si hay números en la cadena entonces...
        retorno = "N/A" #Se asignará N/A a la variable retorno.
    else: 
        cadena_modificada = re.sub("/", " ", cadena_a_analizar).lower() #En caso de que no haya números en la cadena, se reemplazaran...
        retorno = cadena_modificada #... "/" si se encuentran en la cadena por un espacio vacío, y luego la cadena será pasada a minúsculas...
        # ... finalmente, se asignará la cadena modificada a la variable retorno.
    return retorno # Devolverá retorno que será "N/A" en caso de una cadena con números o la cadena sanitizada.

def sanitizar_dato(diccionario:dict, clave:str, tipo_dato:str) -> bool:
    if tipo_dato in ("entero", "int", "flotante", "float", "cadena", "string"):#Verifico si el dato que pasé coincide con los especificados.
        clave_a_sanitizar = clave.lower()#Paso a minúsculas la clave buscada para evitar posibles errores.
        tipo_dato_sanitizado = tipo_dato.lower()#Paso a minúsculas el tipo de dato buscado para evitar posibles errores.

        if clave_a_sanitizar in diccionario:#Si la clave que estoy buscando se encuentra en el diccionario entonces...
            clave_solicitada = diccionario[clave_a_sanitizar]#Asigno a clave_solicitada el valor que se encuentra dentro de la clave.
            if tipo_dato == "entero" or tipo_dato == "int":#Si el tipo de dato es entero o int...
                diccionario[clave_a_sanitizar] = sanitizar_entero(clave_solicitada)#Sanitizo el dato a int.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
            elif tipo_dato == "flotante" or tipo_dato == "float":#Si el tipo de dato es flotante...
                diccionario[clave_a_sanitizar] = sanitizar_flotante(clave_solicitada)#Sanitizo el dato a float.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
            elif tipo_dato == "cadena" or tipo_dato == "string":#Si el tipo de dato es un String...
                diccionario[clave_a_sanitizar] = sanitizar_string(clave_solicitada)#Sanitizo el dato a STR.
                retorno = True#Devuelvo True en caso de que se haya sanitizado algún dato.
        elif clave_a_sanitizar not in diccionario:#Si la clave no se encuentra en el diccionario.
            print("La clave especificada no existe en el héroe")#Printeo mensaje de error.
            retorno = False#Devuelvo false en caso de no poder sanitizar datos.
    else:
        print("Tipo de dato no reconocido.")#Si "tipo_dato" no se encuentra entre los especificados, entonces mostrará mensaje de error...
        retorno = False#Y devolverá false.

    return retorno#Devuelve retorno que podrá ser un True o False según se haya sanitizado algún dato.