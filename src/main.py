print("Teste")

from machine import Pin
import dht
import time

# Definindo o pino de dado
dht_pin = Pin(12)

# Inicializando o sensor DHT22
sensor = dht.DHT22(dht_pin)

while True:
    try:
        sensor.measure()  # Faz a leitura

        temperatura = sensor.temperature()
        umidade = sensor.humidity()

        print("Temperatura:", temperatura, "°C")
        print("Umidade:", umidade, "%")
        print("-----------------------")

    except OSError as e:
        print("Erro ao ler sensor:", e)

    time.sleep(2)  # Aguarda 2 segundos