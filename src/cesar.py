import sys

def cifrado_cesar(texto, corrimiento):
    resultado = ""

    for char in texto:
        if char.isalpha():
            desplazamiento = ord(char) + corrimiento

            if char.isupper():
                resultado += chr((desplazamiento - 65) % 26 + 65)
            else:
                resultado += chr((desplazamiento - 97) % 26 + 97)
        else:
            resultado += char

    return resultado

if __name__ == "__main__":
    # Asegúrate de que se proporcionen suficientes argumentos
    if len(sys.argv) != 3:
        print("Uso: sudo python3 cesar.py 'Texto a cifrar' (numero de corrimiento)")
        sys.exit(1)

    # Obtener el texto y el corrimiento desde los argumentos
    texto = sys.argv[1]
    corrimiento = int(sys.argv[2])

    # Cifrar el texto (criptografia y seguridad en redes)
    texto_cifrado = cifrado_cesar(texto, corrimiento)
    print(f"Texto cifrado: {texto_cifrado}")

#sudo python3 cesar.py "criptografia y seguridad en redes" 9
