
# -*- coding: utf-8 -*-
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#con pos+3 ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c',]
#con pos+5 ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e',]

# omitimos los espacios y aplicamos el lowe case
def omitSpace(mensaje):
    newWord = ''
    for letter in mensaje:
        if(letter!=' '):
            newWord += letter
    return newWord.lower()

# encriptamos los mensajes
def Encryp(menssaje, movePosition):
    global alphabet
    messageEncrypt = ''
    lenAlphabet = len(alphabet)
    for letter in omitSpace(menssaje):
        position = alphabet.index(letter)
        aux = lenAlphabet - position
        if(aux > movePosition):
            messageEncrypt += alphabet[position+movePosition]
        else:
            newPos = movePosition - aux
            messageEncrypt += alphabet[newPos]

    print('mensaje: '+menssaje,'mensaje encryptado: '+messageEncrypt)
