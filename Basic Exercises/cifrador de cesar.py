letras = 'abcdefghijklmnopqrstuvwxyz'
numero_letras = len(letras)


def encriptar(textoN, key): # la funcion toma de variables el texto a encriptar y la clave de cifrado
    textocifrado = '' #almacena la cadena del resultado de cifrado
    for letras in textoN: #itera sobre cada letra del original
        letras = letras.lower()
        if not letras == ' ':  #encripta si no es un caracter vacio
            index = letras.find(letras) #se utiliza el metodo find para encontrar el indice en la cadena
            if index == -1: #si find no entra en la cadena vuelve a empezar de 0
                textocifrado += letras
            else:
                nuevo_indice = index + key
                if nuevo_indice >= numero_letras: #si el nuevo indice es mayor o igual 26 se resta 26 para que este dentro de la cadena
                    nuevo_indice -= numero_letras
                textocifrado += letras[nuevo_indice] #el caracter encriptado al nuevo indice se agrega al texto cifrado
    return textocifrado #una vez que se itero en todas las letras del textoN retorna el texto cifrado como resultado

"""def desencriptar(textocifrado, key): 
    textoN = '' 
    for letras in textocifrado: 
        letras = letras.lower()
        if not letras == ' ':  
            index = letras.find(letras) 
            if index == -1: 
                textocifrado += letras
            else:
                nuevo_indice = index - key
                if nuevo_indice < 0: 
                    nuevo_indice += numero_letras
                textoN += letras[nuevo_indice] 
    return textoN """
            
        

input_usuario = input("Presiona 'e' para encriptar o 'e' para desencriptar")
if input_usuario == 'e':
    key = int(input("Ingresa la llave (1 hasta 26):"))
    text = input("Ingresa el texto para encriptar:" )
    textocifrado = encriptar(text, key)
    print(f'Texto cifrado: {textocifrado}')
