{{
    config(
        materialized='incremental',
        unique_key='day'
    )
}}

select action, dividende, day from (select action, "Dvidende Estimé" as dividende, day, row_number()
over (partition by action, "Dvidende Estimé", day order by date DESC) as rank
from rente_stg) sub where rank = 1 and action is not NULL

{% if is_incremental() %}
    and day >= (select max(day) from {{ this }})
 {% endif %}


