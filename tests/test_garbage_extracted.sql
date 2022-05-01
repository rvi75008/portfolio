with value_yesterday as (select valeur_totale from {{ ref('portfolio_value') }} where day = SUBSTR(CAST(  {{ dbt_date.yesterday() }} as varchar ), 3)),
latest_values_today as (
select sum(valorisation) as valo from details_stg where date = (select max(date) from details_stg) group by date
)
select evol from (select  t.valo/y.valeur_totale * 100 as evol from value_yesterday y full outer join latest_values_today t on 1 = 1) sub
where evol < 98 or evol > 102
