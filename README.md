# 🏗️ Pipeline de Engenharia de Dados: Monitorização IoT e Segurança do Trabalho em Obras

Este projeto consiste num pipeline ELT (*Extract, Load, Transform*) completo focado na monitorização de alertas de segurança e estado de sensores IoT aplicados à Construção Civil.

---

## 🛠️ Arquitetura e Tecnologias

- **Ingestão (Python)**: Geração e carga de dados brutos simulando dispositivos IoT (`raw_sensores_iot`) e cadastro de obras (`raw_obras`).
- **Data Warehouse (Google BigQuery)**: Armazenamento em nuvem na região `US`.
- **Transformação & Testes (dbt Core)**: Modelos organizados em arquitetura de 3 camadas (`staging` e `marts`), com testes de integridade e documentação.
- **Visualização (Looker Studio)**: Dashboard interativo conectado diretamente às tabelas finais de produção no BigQuery.

---

## 📐 Estrutura de Camadas (dbt Models)

1. **`staging`**:
   - `stg_obras`: Limpeza, padronização de tipos de dados e nomes das obras.
   - `stg_sensores_iot`: Tratamento de estampas de tempo (*timestamps*) e classificação dos níveis de bateria e status dos alertas (`OK`, `ALERTA`, `CRITICO`).
2. **`marts`**:
   - `fct_eventos_seguranca_obras`: Tabela fato consolidada que unifica as leituras dos sensores com os metadados das obras para análise analítica de KPIs.

---

## 📊 Dashboard Interativo

Aceda ao relatório no Looker Studio:
🔗 **[Ver Dashboard no Looker Studio](https://datastudio.google.com/reporting/a15552a5-fe2c-4a52-b4b3-4039aec29a96)**

---

## 🚀 Como Executar o Projeto Localmente

1. **Clonar o repositório**:
   ```bash
   git clone [https://github.com/NathanGilmen/dbt-bigquery-iot-construction.git](https://github.com/NathanGilmen/dbt-bigquery-iot-construction.git)
   cd dbt-bigquery-iot-construction
