# ATALLOS TECLADO
# Comentar/quitar comentario : atajo teclado de comentario = Shift Ctrl 7
# Ctrl + N = nuevo archivo
# Ctrl + L = seleccionar linea
# + atallos teclado:
# ver paleta de comandos:Ctrl+Shift+P, F1.
# Seleccionar todas as ocorrencias da selección actual: Ctrl + Shift + L.
# Seleccionar todas as ocorrencias da palabra actual: Ctrl + F2.
# Mostrar suxestións de edición: Ctrl + Space.
# Terminal : Ctrl + `.
# Mostrar suxestións de edición: Ctrl + Space.
# Abrir de forma rápida un ficheiro: Ctrl + P.
# Crear un novo ficheiro: Ctrl + N.
# Renomear símbolo: F2.
# Ir á definición: F12.

from pydoc import text
from queue import PriorityQueue

import numpy as np

msg = "Hello world!"
print(msg)

print(np.random.randint(1, 9))
print("wonhae" + 2 * "maniiii" + "⋆˚꩜!")


#'
# Crea un programa Python que permita introducir un texto e xerar o seu hash SHA-256. Engade ao teu programa unha funcionalidade para xerar o hash SHA-256 dun arquivo.
# '


texto = "hello world"
hash_texto = hash(texto)  # utiliza internamente el algoritmo SipHash
print(f"Hash do texto {texto}:{hash_texto}")

# modulo python para usar algoritmos criptografia (SHA-256,512,MD5)
import hashlib


def crear_hash_sha256(texto: str) -> str:
    # El texto debe codificarse a bytes
    texto_en_bytes = texto.encode("utf-8")

    # Crear el objeto hash SHA-256
    objeto_hash = hashlib.sha256(texto_en_bytes)

    # Devolver el resumen en formato hexadecimal (64 caracteres)
    return objeto_hash.hexdigest()


# Ejemplo de uso:
mensaje = input()
resultado = crear_hash_sha256(mensaje)
print(f"Texto: {mensaje}")
print(f"Hash SHA-256: {resultado}")

#'
#
#
#
#
# '
