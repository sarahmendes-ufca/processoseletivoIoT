# 📝 Relatório Final 

>👤 **Dados do Candidato**
>- **Nome:** Sarah Mendes Teles 
>- **Github:** sarahmendes-ufca


## 1️⃣ Visão Geral da Solução - Monitoramento de Temperatura e Umidade com ESP32


Este projeto tem como objetivo realizar a leitura de temperatura e umidade utilizando um sensor DHT22 conectado a um ESP32, e
ambiente simulado no Wokwi.

O sistema embarcado coleta os dados do sensor periodicamente e os exibe no terminal serial. Ele simula um sistema básico de 
monitoramento ambiental, que pode ser expandido para aplicações reais como automação residencial ou controle climático.

A interação do usuário ocorre por meio da visualização dos dados no console da simulação.

<img width="600" height="600" alt="image" src="https://drive.google.com/file/d/1hD512HDfouLHNTU8VHv9oujFZuuaM0Lz/view?
usp=sharing" />

---


## 1️⃣ Visão Geral da Solução - Monitoramento de Temperatura e Umidade com ESP32

Este projeto tem como objetivo realizar a leitura de temperatura e umidade utilizando um sensor DHT22 conectado a um ESP32, em ambiente simulado no Wokwi.

O sistema embarcado coleta os dados do sensor periodicamente e os exibe no terminal serial. Ele simula um sistema básico de monitoramento ambiental, que pode ser expandido para aplicações reais como automação residencial ou controle climático.

A interação do usuário ocorre por meio da visualização dos dados no console da simulação.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O sistema segue uma arquitetura simples baseada em loop contínuo.

### 🔁 Fluxo principal (`main.py`)

1. Definição do pino de dados
  - Importa as bibliotecas necessárias:
``` bash 
from machine import Pin
import dht
import time

dht_pin = Pin(12)
```

2. Inicialização do sensor DHT22
  - Aqui o sistema prepara o hardware:
``` bash 
sensor = dht.DHT22(dht_pin)
```

3. Loop infinito:
  - O sistema embarcado roda continuamente através de um loop infinito. Dentro do loop, ocorre a coleta dos dados:
``` bash 
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
```
   - Realiza a leitura do sensor
   - Obtém temperatura e umidade
   - Exibe os valores no terminal
   - Aguarda um intervalo antes da próxima leitura

### 📁 Estrutura de diretórios do projeto

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

### ⏱️ Estrutura de execução

- Loop infinito (`while True`)
- Temporização com `sleep(2)`
- Tratamento de erro com `try/except`

### 🔗 Interação entre componentes

* O ESP32 envia sinal de leitura ao DHT22
* O DHT22 responde com os dados de temperatura e umidade
* O ESP32 processa e imprime os valores

---

## 3️⃣ Componentes Utilizados na Simulação

* **ESP32**

  * Microcontrolador responsável pela execução do código e controle do sistema

* **DHT22 (sensor de temperatura e umidade)**

  * Responsável por medir temperatura (°C) e umidade relativa (%)

* **Resistor de 10kΩ (pull-up)**

  * Necessário entre VCC e DATA para estabilizar o sinal do sensor

* **Jumpers (fios)**

  * Conectam os componentes

### 📌 Conexões principais:

* VCC → 3.3V do ESP32
* GND → GND do ESP32
* DATA → GPIO (ex: GPIO 15)

---

## 4️⃣ Decisões Técnicas Relevantes

* **Uso da biblioteca `dht`**

  * Facilita a comunicação com o sensor sem precisar implementar o protocolo manualmente

* **Estrutura simples com loop infinito**

  * Adequada para sistemas embarcados que executam continuamente

* **Tratamento de exceções (`try/except`)**

  * Evita que o programa trave caso haja falha na leitura do sensor

* **Intervalo de leitura (2 segundos)**

  * Necessário devido à limitação do DHT22, que não suporta leituras muito frequentes

---

## 5️⃣ Resultados Obtidos

O sistema conseguiu:

- Ler corretamente os valores de temperatura e umidade
- Exibir os dados no terminal da simulação
- Manter execução contínua sem travamentos

### ✅ Requisitos atendidos:

- Comunicação com sensor DHT22
- Processamento de dados no ESP32
- Exibição dos resultados

Na simulação do Wokwi, os valores são atualizados periodicamente e refletem o comportamento esperado do sensor.

---

## 6️⃣ Comentários Adicionais

### ⚠️ Dificuldades encontradas

- Erros iniciais de leitura do sensor

### 🚧 Limitações

- Sistema apenas exibe dados (não armazena nem envia)
- Sem interface gráfica ou comunicação externa

### 🚀 Melhorias futuras

- Envio dos dados via Wi-Fi (MQTT ou HTTP)
- Integração com dashboard (ex: Node-RED)
- Uso de display LCD/OLED

### 📚 Aprendizados

- Integração de sensores com microcontroladores
- Importância de detalhes elétricos (pull-up)
- Estrutura básica de sistemas embarcados em MicroPython

---
