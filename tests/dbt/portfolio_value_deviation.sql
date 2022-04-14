with value_yesterday as (select valeur_totale from {{ ref('portfolio_value') }} where day = CAST(  {{ dbt_date.yesterday() }} as varchar )),
value_today as (select valeur_totale from {{ ref('portfolio_value') }} where day = CAST(  {{ dbt_date.today() }} as varchar ))
select evol from (select  t.valeur_totale/y.valeur_totale * 100 as evol from value_yesterday y full outer join value_today t on 1 = 1) sub
where evol < 90 or evol > 100