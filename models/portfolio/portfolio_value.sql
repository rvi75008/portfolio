select sum(valo) as valeur_totale, day from {{ ref('details') }} group by day