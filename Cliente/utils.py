import json
import requests


def getNumber(max):
    numeros_bien = True
    opcion = 0
    while numeros_bien:
        try:
            opcion = int(input("Opción: "))
            if opcion >= 0 and opcion < max:
                numeros_bien = False
            else:
                print("Selecciona opcion valida.")
        except ValueError:
            print("Selecciona opcion valida.")
    return opcion


def getToken(user, passs):
    respuesta = []
    datos_user = {
        'usuario': user,
        'password': passs,
    }
    response = requests.post('http://127.0.0.1:5000/login', json=datos_user)
    if response.status_code == 200:
        respuesta = response.json()
        token = respuesta['RESULTADO']
        return token
    else:
        respuesta = response.json()
        print(respuesta['RESULTADO'])
        return False


def getName(token):
    nombre = []
    header = {
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    response = requests.get('http://127.0.0.1:5000/datos', headers=header)
    if response.status_code == 200:
        nombre = response.json()
        return nombre['datos']
    return response


def Logon(user, passs, name):
    datos_user = {
        'usuario': user,
        'password': encriptar(passs),
        'name': name
    }
    response = requests.post('http://127.0.0.1:5000/logon', json=datos_user)
    if response.status_code == 200:
        print("Usuario registrado")
    else:
        print("Fallo al crear Usuario")


def encriptar(plain_text):
    encriptado = ""
    for c in plain_text:
        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + 6) % 26 + ord('A')
            c_new = chr(c_shifted)
            encriptado += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + 6) % 26 + ord('a')
            c_new = chr(c_shifted)
            encriptado += c_new
        elif c.isdigit():
            c_new = (int(c) + 6) % 10
            encriptado += str(c_new)
        else:
            encriptado += c
    return encriptado
