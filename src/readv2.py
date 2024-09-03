import sys
from scapy.all import rdpcap, ICMP

# Función para descifrar usando cifrado César
def cesar_descifrar(texto, corrimiento):
    descifrado = ""
    for char in texto:
        if char.isalpha():  # Solo aplica el corrimiento a letras
            desplazamiento = ord(char) - corrimiento
            if char.isupper():
                descifrado += chr((desplazamiento - 65) % 26 + 65)
            else:
                descifrado += chr((desplazamiento - 97) % 26 + 97)
        else:
            descifrado += char
    return descifrado

# Función para contar letras comunes en español
def contar_letras_comunes(texto):
    letras_comunes = "eaosrnidlc"  # Las letras más comunes en español
    return sum(texto.count(letra) for letra in letras_comunes)

# Función principal para leer paquetes ICMP y descifrar
def leer_paquetes_y_descifrar(archivo_pcap):
    # Leer los paquetes desde el archivo pcap
    try:
        packets = rdpcap(archivo_pcap)
    except FileNotFoundError:
        print(f"Archivo {archivo_pcap} no encontrado.")
        sys.exit(1)

    # Extraer los primeros 8 bytes del campo de datos ICMP de cada paquete
    icmp_data = []
    for packet in packets:
        if ICMP in packet and packet[ICMP].type == 8:  # Tipo 8 es Echo request
            payload = bytes(packet[ICMP].payload)
            first_8_bytes = payload[:8]  # Obtener los primeros 8 bytes del payload
            icmp_data.append(first_8_bytes)

    # Unir todos los bytes de los paquetes en un solo string de caracteres
    icmp_string = ''.join([bytes.decode(d, errors='ignore') for d in icmp_data])
    print(f"Datos ICMP extraídos: {icmp_string}")

    mejor_candidato = None
    mayor_conteo_letras = 0

    # Probar todas las combinaciones posibles de corrimientos (0-25)
    resultados = []
    for corrimiento in range(26):
        descifrado = cesar_descifrar(icmp_string, corrimiento)
        conteo_letras = contar_letras_comunes(descifrado)

        resultados.append((corrimiento, descifrado))

        # Seleccionar el descifrado con más letras comunes
        if conteo_letras > mayor_conteo_letras:
            mayor_conteo_letras = conteo_letras
            mejor_candidato = (corrimiento, descifrado)

    # Imprimir todas las combinaciones y resaltar el mejor candidato en verde
    for corrimiento, descifrado in resultados:
        if corrimiento == mejor_candidato[0]:
            print(f"\033[92mCorrimiento {corrimiento}: {descifrado}\033[0m")
        else:
            print(f"Corrimiento {corrimiento}: {descifrado}")

if __name__ == "__main__":
    # Verificar si el archivo pcap fue pasado como argumento
    if len(sys.argv) != 2:
        print("Uso: sudo python3 readv2.py <archivo_pcapng>")
        sys.exit(1)

    archivo_pcap = sys.argv[1]
    leer_paquetes_y_descifrar(archivo_pcap)
