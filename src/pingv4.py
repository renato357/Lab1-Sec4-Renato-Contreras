import sys
from scapy.all import *
import random
import time

def send_stealth_ping(text, ip_destino="8.8.8.8"):  # IP por defecto es localhost
    # Configuraciones iniciales
    base_identifier = random.randint(0, 65535)  # Identifier del ICMP constante
    base_ip_id = random.randint(0, 65535)  # Identificación IP inicial aleatoria
    base_seq = 1  # Número de secuencia inicial

    # Usar un timestamp constante (intento de hacerlo)
    timestamp_constante = int(time.time()) & 0xFFFFFFFF  # Timestamp en segundos desde epoch

    # Envío de caracteres del texto uno por uno
    for i, char in enumerate(text):
        # Codificar el carácter a enviar
        char_encoded = char.encode('utf-8')

        # Crear payload con los primeros 8 bytes constantes seguido del carácter
        primeros_8_bytes = char_encoded + b'\x00' * (8 - len(char_encoded))
        
        # Continuar con la secuencia de bytes desde 0x10 hasta 0x37
        incremental_bytes = bytes(range(0x10, 0x38))  # Genera los bytes 10, 11, ..., 36, 37
        
        # Construir el payload completo
        payload = primeros_8_bytes + incremental_bytes

        # Construir paquete ICMP con las configuraciones deseadas
        packet = (IP(dst=ip_destino, id=base_ip_id + i) /
                  ICMP(type=8, id=base_identifier, seq=base_seq, ts_ori=timestamp_constante) /
                  payload)

        # Mostrar los parámetros que se están enviando
        print(f"Enviando carácter '{char}' en el paquete {i+1}")
        print(f"IP ID: {packet[IP].id}, ICMP Identifier: {packet[ICMP].id}, Seq: {packet[ICMP].seq}, Timestamp: {packet[ICMP].ts_ori}, Data: {payload.hex()}")

        # Enviar el paquete ICMP
        send(packet)
        time.sleep(0.1)  # Ajusta el sleep a 0.1 segundos

        # Incrementar valores para el próximo paquete
        base_seq += 1  # Incrementa el número de secuencia para el próximo paquete

if __name__ == "__main__":
    # Obtener la frase de los argumentos de la línea de comandos
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"<frase>\"")
        sys.exit(1)

    frase = sys.argv[1]
    send_stealth_ping(frase)
