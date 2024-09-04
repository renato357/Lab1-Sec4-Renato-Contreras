from scapy.all import *
import random
import time

def send_stealth_ping(text, ip_destino="8.8.8.8"):
    base_identifier = random.randint(0, 65535)  # Identifier del ICMP constante
    base_ip_id = random.randint(0, 65535)  # Identificación IP inicial aleatoria
    base_seq = 1  # Número de secuencia inicial

    # Timestamp constante
    timestamp_constante = int(time.time() * 1000) & 0xFFFFFFFF  # Timestamp en milisegundos desde epoch

    for i, char in enumerate(text):
        char_encoded = char.encode('utf-8')

        # Crear los primeros 8 bytes estáticos
        primeros_8_bytes = b'\x01\x02\x03\x04\x05\x06\x07\x08'  # 8 bytes estáticos

        # Continuar con el carácter enviado
        char_byte = char_encoded if len(char_encoded) == 1 else char_encoded[:1]  # Asegura que sea 1 byte
        
        # Continuar con la secuencia de bytes desde 0x10 hasta 0x37
        incremental_bytes = bytes(range(0x10, 0x38))  # Genera los bytes 0x10, ..., 0x37

        # Construir el payload completo
        payload = primeros_8_bytes + char_byte + incremental_bytes

        # Construir paquete ICMP tipo 13 (Timestamp Request)
        packet = (IP(dst=ip_destino, id=base_ip_id + i) /
                  ICMP(type=13, id=base_identifier, seq=base_seq, ts_ori=timestamp_constante, ts_rx=0, ts_tx=0) /
                  payload)

        # Mostrar los parámetros que se están enviando
        print(f"Enviando carácter '{char}' en el paquete {i+1}")
        print(f"IP ID: {packet[IP].id}, ICMP Identifier: {packet[ICMP].id}, Seq: {packet[ICMP].seq}, Timestamp: {packet[ICMP].ts_ori}, Data: {payload.hex()}")

        # Enviar el paquete ICMP
        send(packet)
        time.sleep(0.1)

        base_seq += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"<frase>\"")
        sys.exit(1)

    frase = sys.argv[1]
    send_stealth_ping(frase)
