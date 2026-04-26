print("Teste")
from machine import Pin
import dht
import time

# Config
PINO_DHT = 12
INTERVALO_LEITURA = 2000  # ms
TEMP_ALERTA = 30

# Hardware
sensor = dht.DHT22(Pin(PINO_DHT))

# Estados
ESTADO_NORMAL = 0
ESTADO_ALERTA = 1
ESTADO_ERRO = 2

estado_atual = ESTADO_NORMAL

# Controle de tempo
ultimo_tempo = 0

# Funções
def ler_sensor():
    """
    Realiza a leitura do DHT22.
    Retorna: (temperatura, umidade, sucesso)
    """
    try:
        sensor.measure()
        return sensor.temperature(), sensor.humidity(), True
    except Exception:
        return None, None, False


def atualizar_estado(temp, leitura_ok):
    """
    Define o estado do sistema com base nos dados.
    """
    if not leitura_ok:
        return ESTADO_ERRO
    elif temp > TEMP_ALERTA:
        return ESTADO_ALERTA
    else:
        return ESTADO_NORMAL


def exibir_dados(temp, hum, estado):
    """
    Exibe os dados no terminal de forma organizada.
    """
    print("\n-----------------------")

    if estado == ESTADO_ERRO:
        print("Erro ao ler sensor")

    else:
        print("Temperatura:", temp, "°C")
        print("Umidade:", hum, "%")

        if estado == ESTADO_ALERTA:
            print("Status: ALERTA (Temperatura alta)")
        else:
            print("Status: NORMAL")


# Loop principal
print("Sistema iniciado")

while True:
    agora = time.ticks_ms()

    if time.ticks_diff(agora, ultimo_tempo) >= INTERVALO_LEITURA:
        ultimo_tempo = agora

        temp, hum, ok = ler_sensor()

        estado_atual = atualizar_estado(temp if temp is not None else 0, ok)

        exibir_dados(temp, hum, estado_atual)