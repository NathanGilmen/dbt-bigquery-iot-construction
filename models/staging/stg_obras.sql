with source as (
    select * from {{ source('raw_data', 'raw_obras') }}
),

renamed as (
    select
        cast(obra_id as string) as id_obra,
        cast(nome_obra as string) as nome_obra,
        cast(cidade as string) as cidade,
        cast(orcamento as numeric) as valor_orcamento
    from source
)

select * from renamed