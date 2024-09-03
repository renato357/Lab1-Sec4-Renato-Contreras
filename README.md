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
├── README.md            # Este archivo
├── src/                 # Código fuente de las actividades
│   ├── cesar.py         # Implementación del cifrado César
│   ├── pingv4.py        # Código para el envío de pings stealth
│   └── mitm.py          # Código para descifrar los mensajes capturados
├── docs/                # Documentación y reportes
│   └── Informe_Lab1.pdf # Informe detallado del laboratorio
└── data/                # Archivos de datos utilizados
    └── ejemplo.pcapng   # Captura de paquetes para análisis
