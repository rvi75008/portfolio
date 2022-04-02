{{
    config(
        materialized='incremental',
        unique_key='day'
    )
}}

select actif, valo, day from (select actif as actif, valorisation as valo, day, row_number()
over (partition by actif, day order by date DESC) as rank
from details_stg) sub where rank = 1

{% if is_incremental() %}
    and day >= (select max(day) from {{ this }})
 {% endif %}


