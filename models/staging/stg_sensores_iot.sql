with source as (
    select * from {{ source('raw_data', 'raw_sensores_iot') }}
),

renamed as (
    select
        cast(evento_id as string) as id_evento,
        cast(obra_id as string) as id_obra,
        cast(sensor_id as string) as id_sensor,
        cast(timestamp_evento as timestamp) as dtm_evento,
        cast(tipo_evento as string) as tipo_evento,
        cast(status_nivel as string) as status_nivel,
        cast(bateria_sensor_pct as int64) as pct_bateria_sensor
    from source
)

select * from renamed