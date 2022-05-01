select actif, pu from details_stg where date = (select max(date) from details_stg) and pu = 0 and (
actif like 'BGF World%' or actif like 'OR%' or actif like 'AG%') group by date, pu, actif
