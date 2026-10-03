import csv
import random
from datetime import datetime, timedelta

# 1. Gerar raw_obras.csv
obras = [
    {"obra_id": "OBR-001", "nome_obra": "Residencial Serra Azul", "cidade": "Teresópolis", "orcamento": 2500000.00},
    {"obra_id": "OBR-002", "nome_obra": "Edifício Comercial Centro", "cidade": "Rio de Janeiro", "orcamento": 5800000.00},
    {"obra_id": "OBR-003", "nome_obra": "Galpão Logístico Sul", "cidade": "Niterói", "orcamento": 12000000.00},
]

with open("raw_obras.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["obra_id", "nome_obra", "cidade", "orcamento"])
    writer.writeheader()
    writer.writerows(obras)

# 2. Gerar raw_sensores_iot.csv
tipos_evento = ["DETECAO_EPI_OK", "EPI_AUSENTE_CAPACETE", "EPI_AUSENTE_COLETE", "ALERTA_TEMPERATURA"]
status_lista = ["OK", "ALERTA", "CRITICO"]

data_inicio = datetime(2026, 9, 1)
registos_iot = []

for i in range(1, 501):
    obra = random.choice(obras)
    data_evento = data_inicio + timedelta(minutes=random.randint(0, 43200))
    evento = random.choice(tipos_evento)
    
    if evento == "DETECAO_EPI_OK":
        status = "OK"
    elif "EPI_AUSENTE" in evento:
        status = "ALERTA"
    else:
        status = "CRITICO"

    registos_iot.append({
        "evento_id": f"EVT-{i:05d}",
        "obra_id": obra["obra_id"],
        "sensor_id": f"SNS-{random.randint(100, 105)}",
        "timestamp_evento": data_evento.strftime("%Y-%m-%d %H:%M:%S"),
        "tipo_evento": evento,
        "status_nivel": status,
        "bateria_sensor_pct": random.randint(15, 100)
    })

with open("raw_sensores_iot.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "evento_id", "obra_id", "sensor_id", "timestamp_evento", "tipo_evento", "status_nivel", "bateria_sensor_pct"
    ])
    writer.writeheader()
    writer.writerows(registos_iot)

print("Ficheiros 'raw_obras.csv' e 'raw_sensores_iot.csv' gerados com sucesso!")