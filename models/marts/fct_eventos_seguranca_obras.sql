with sensores as (
    select * from {{ ref('stg_sensores_iot') }}
),

obras as (
    select * from {{ ref('stg_obras') }}
)

select
    s.id_evento,
    s.dtm_evento,
    s.id_sensor,
    s.tipo_evento,
    s.status_nivel,
    s.pct_bateria_sensor,
    o.id_obra,
    o.nome_obra,
    o.cidade,
    o.valor_orcamento
from sensores s
left join obras o
    on s.id_obra = o.id_obra