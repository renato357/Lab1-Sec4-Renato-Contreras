# Proyecto de Criptografía - Laboratorio 1

Este repositorio contiene el código y los informes correspondientes al Laboratorio 1 del curso de Criptografía. El objetivo del laboratorio es auditar la capacidad de un sistema para detectar filtraciones de información a través del análisis de tráfico de red.

## Descripción General

En este proyecto, se desarrollan varias actividades que incluyen la creación de un software que genera tráfico similar al programa `ping`, pero con la inclusión de información confidencial. Se busca que este tráfico pase desapercibido ante un sistema de Deep Packet Inspection (DPI).

### Actividades

1. **Algoritmo de cifrado:** Implementación de un cifrado César en Python.
2. **Modo stealth:** Envío de caracteres cifrados a través de paquetes ICMP sin levantar sospechas.
3. **MitM (Man in the Middle):** Recuperación del mensaje transmitido aplicando un ataque de fuerza bruta al cifrado.

## Estructura del Repositorio

```bash
├── README.md                             # Este archivo
├── img/                                  # Carpeta con todas las imágenes
├── src/                                  # Código fuente de las actividades
│   ├── cesar.py                          # Implementación del cifrado César
│   ├── pingv4.py                         # Código para el envío de pings stealth
│   ├── readv2.py                         # Código para descifrar los mensajes capturados
│   └── cesar.pcapng                      # Archivos de datos utilizados
└── docs/                                 # Documentación y reportes
    └── Lab01_Cripto_Renato_Contreras.pdf # Informe detallado del laboratorio
```
## Contacto

Para consultas o más información, por favor contacta a:

**Renato Óscar Benjamín Contreras Carvajal**  
Correo: [renato.contreras@mail.udp.cl](mailto:renato.contreras@mail.udp.cl)
