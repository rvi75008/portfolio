CREATE SCHEMA dev AUTHORIZATION dbtdev;
ALTER ROLE dbtdev set search_path = 'dev';
GRANT ALL PRIVILEGES ON SCHEMA dev to dbtdev;


BEGIN;
SET client_encoding = 'LATIN1';
SET search_path TO 'dev';
CREATE TABLE details_stg (actif text, valorisation double precision, date text, day text);
CREATE TABLE rente_stg (action text, dividende double precision, date text, day text);

COPY details_stg (actif, valorisation, date, day) FROM stdin;
OR - 10F	3500	2022-03-31 19:51:41.883599	22-03-31
AG - 5F	32.5	2022-03-31 19:51:41.883599	22-03-31
AG - Phil	167.3	2022-03-31 19:51:41.883599	22-03-31
BGF World Gold	11319.69	2022-03-31 19:51:41.883599	22-03-31
OR - 20F	2028	2022-03-31 19:51:41.883599	22-03-31
Sanofi	12951.4	2022-03-31 19:51:41.883599	22-03-31
OR - 10$	865	2022-03-31 19:51:41.883599	22-03-31
AG - 50F	469.2	2022-03-31 19:51:41.883599	22-03-31
Entrepreteurs	995.39	2022-03-31 19:51:41.883599	22-03-31
ABC Arbitrage	13567.18	2022-03-31 19:51:41.883599	22-03-31
AG - 1F	135	2022-03-31 19:51:41.883599	22-03-31
IShares China Bonds	54525.21	2022-03-31 19:51:41.883599	22-03-31
CC - DBS	411.35	2022-03-31 19:51:41.883599	22-03-31
Cash PEA	38.56	2022-03-31 19:51:41.883599	22-03-31
Prêt Lombard	-30500	2022-03-31 19:51:41.883599	22-03-31
Fond Monétaire	-3.48	2022-03-31 19:51:41.883599	22-03-31
CCC - Hello Bank	532.83	2022-03-31 19:51:41.883599	22-03-31
Danone	10856.51	2022-03-31 19:51:41.883599	22-03-31
BGF World Energy	26420.81	2022-03-31 19:51:41.883599	22-03-31
October	390.71	2022-03-31 19:51:41.883599	22-03-31
IDI	1798	2022-03-31 19:51:41.883599	22-03-31
Moury Construct	11072	2022-03-31 19:51:41.883599	22-03-31
Gazprom	506.13	2022-03-31 19:51:41.883599	22-03-31
BGF World Mining	16164.4	2022-03-31 19:51:41.883599	22-03-31
Publicis	10665.18	2022-03-31 19:51:41.883599	22-03-31
Nikko AM ASEAN	3408.12	2022-03-31 19:51:41.883599	22-03-31
Holland Colours	3130	2022-03-31 19:51:41.883599	22-03-31
OR - 50 Peso	6270	2022-03-31 19:51:41.883599	22-03-31
AXA	12328.48	2022-03-31 19:51:41.883599	22-03-31
Flow Traders	10563.9	2022-03-31 19:51:41.883599	22-03-31
BNB	2250.1	2022-03-31 19:51:41.883599	22-03-31
Scor	13631.73	2022-03-31 19:51:41.883599	22-03-31
CBO Territoria	13011.15	2022-03-31 19:51:41.883599	22-03-31
Van de Velde	9752.4	2022-03-31 19:51:41.883599	22-03-31
CT Bourso Cash	0	2022-03-31 19:51:41.883599	22-03-31
Cash PEA-PME	36.67	2022-03-31 19:51:41.883599	22-03-31
BUSD	0.3	2022-03-31 19:51:41.883599	22-03-31
USDT	0.23	2022-03-31 19:51:41.883599	22-03-31
CC - Boursorama	95.58	2022-03-31 19:51:41.883599	22-03-31
Revolut	850.53	2022-03-31 19:51:41.883599	22-03-31
US 20+ years	30029.69	2022-03-31 19:51:41.883599	22-03-31
OR - 10F	3500	2022-03-31 19:51:48.534290	22-03-31
AG - 5F	32.5	2022-03-31 19:51:48.534290	22-03-31
AG - Phil	167.3	2022-03-31 19:51:48.534290	22-03-31
BGF World Gold	11319.69	2022-03-31 19:51:48.534290	22-03-31
OR - 20F	2028	2022-03-31 19:51:48.534290	22-03-31
Sanofi	12951.4	2022-03-31 19:51:48.534290	22-03-31
OR - 10$	865	2022-03-31 19:51:48.534290	22-03-31
AG - 50F	469.2	2022-03-31 19:51:48.534290	22-03-31
Entrepreteurs	995.39	2022-03-31 19:51:48.534290	22-03-31
ABC Arbitrage	13567.18	2022-03-31 19:51:48.534290	22-03-31
AG - 1F	135	2022-03-31 19:51:48.534290	22-03-31
IShares China Bonds	54525.21	2022-03-31 19:51:48.534290	22-03-31
CC - DBS	411.35	2022-03-31 19:51:48.534290	22-03-31
Cash PEA	38.56	2022-03-31 19:51:48.534290	22-03-31
Prêt Lombard	-30500	2022-03-31 19:51:48.534290	22-03-31
Fond Monétaire	-3.48	2022-03-31 19:51:48.534290	22-03-31
CCC - Hello Bank	532.83	2022-03-31 19:51:48.534290	22-03-31
Danone	10856.51	2022-03-31 19:51:48.534290	22-03-31
BGF World Energy	26420.81	2022-03-31 19:51:48.534290	22-03-31
October	390.71	2022-03-31 19:51:48.534290	22-03-31
IDI	1798	2022-03-31 19:51:48.534290	22-03-31
Moury Construct	11072	2022-03-31 19:51:48.534290	22-03-31
Gazprom	506.13	2022-03-31 19:51:48.534290	22-03-31
BGF World Mining	16164.4	2022-03-31 19:51:48.534290	22-03-31
Publicis	10665.18	2022-03-31 19:51:48.534290	22-03-31
Nikko AM ASEAN	3408.12	2022-03-31 19:51:48.534290	22-03-31
Holland Colours	3130	2022-03-31 19:51:48.534290	22-03-31
OR - 50 Peso	6270	2022-03-31 19:51:48.534290	22-03-31
AXA	12328.48	2022-03-31 19:51:48.534290	22-03-31
Flow Traders	10563.9	2022-03-31 19:51:48.534290	22-03-31
BNB	2250.1	2022-03-31 19:51:48.534290	22-03-31
Scor	13631.73	2022-03-31 19:51:48.534290	22-03-31
CBO Territoria	13011.15	2022-03-31 19:51:48.534290	22-03-31
Van de Velde	9752.4	2022-03-31 19:51:48.534290	22-03-31
CT Bourso Cash	0	2022-03-31 19:51:48.534290	22-03-31
Cash PEA-PME	36.67	2022-03-31 19:51:48.534290	22-03-31
BUSD	0.3	2022-03-31 19:51:48.534290	22-03-31
USDT	0.23	2022-03-31 19:51:48.534290	22-03-31
CC - Boursorama	95.58	2022-03-31 19:51:48.534290	22-03-31
Revolut	850.53	2022-03-31 19:51:48.534290	22-03-31
US 20+ years	30029.69	2022-03-31 19:51:48.534290	22-03-31
OR - 10F	3500	2022-03-31 20:01:04.994911	22-03-31
AG - 5F	32.5	2022-03-31 20:01:04.994911	22-03-31
AG - Phil	167.3	2022-03-31 20:01:04.994911	22-03-31
BGF World Gold	11319.32	2022-03-31 20:01:04.994911	22-03-31
OR - 20F	2028	2022-03-31 20:01:04.994911	22-03-31
Sanofi	12951.4	2022-03-31 20:01:04.994911	22-03-31
OR - 10$	865	2022-03-31 20:01:04.994911	22-03-31
AG - 50F	469.2	2022-03-31 20:01:04.994911	22-03-31
Entrepreteurs	995.39	2022-03-31 20:01:04.994911	22-03-31
ABC Arbitrage	13567.18	2022-03-31 20:01:04.994911	22-03-31
AG - 1F	135	2022-03-31 20:01:04.994911	22-03-31
IShares China Bonds	54539.08	2022-03-31 20:01:04.994911	22-03-31
CC - DBS	411.33	2022-03-31 20:01:04.994911	22-03-31
Cash PEA	38.56	2022-03-31 20:01:04.994911	22-03-31
Prêt Lombard	-30500	2022-03-31 20:01:04.994911	22-03-31
Fond Monétaire	-3.48	2022-03-31 20:01:04.994911	22-03-31
CCC - Hello Bank	532.83	2022-03-31 20:01:04.994911	22-03-31
Danone	10856.51	2022-03-31 20:01:04.994911	22-03-31
BGF World Energy	26419.93	2022-03-31 20:01:04.994911	22-03-31
October	390.71	2022-03-31 20:01:04.994911	22-03-31
IDI	1798	2022-03-31 20:01:04.994911	22-03-31
Moury Construct	11072	2022-03-31 20:01:04.994911	22-03-31
Gazprom	506.26	2022-03-31 20:01:04.994911	22-03-31
BGF World Mining	16163.86	2022-03-31 20:01:04.994911	22-03-31
Publicis	10665.18	2022-03-31 20:01:04.994911	22-03-31
Nikko AM ASEAN	3408.01	2022-03-31 20:01:04.994911	22-03-31
Holland Colours	3130	2022-03-31 20:01:04.994911	22-03-31
OR - 50 Peso	6270	2022-03-31 20:01:04.994911	22-03-31
AXA	12328.48	2022-03-31 20:01:04.994911	22-03-31
Flow Traders	10563.9	2022-03-31 20:01:04.994911	22-03-31
BNB	2251.39	2022-03-31 20:01:04.994911	22-03-31
Scor	13631.73	2022-03-31 20:01:04.994911	22-03-31
CBO Territoria	13011.15	2022-03-31 20:01:04.994911	22-03-31
Van de Velde	9752.4	2022-03-31 20:01:04.994911	22-03-31
CT Bourso Cash	0	2022-03-31 20:01:04.994911	22-03-31
Cash PEA-PME	36.67	2022-03-31 20:01:04.994911	22-03-31
BUSD	0.3	2022-03-31 20:01:04.994911	22-03-31
USDT	0.23	2022-03-31 20:01:04.994911	22-03-31
CC - Boursorama	95.58	2022-03-31 20:01:04.994911	22-03-31
Revolut	850.75	2022-03-31 20:01:04.994911	22-03-31
US 20+ years	30037.34	2022-03-31 20:01:04.994911	22-03-31
OR - 10F	3500	2022-04-01 18:02:52.343528	22-04-01
AG - 5F	32.5	2022-04-01 18:02:52.343528	22-04-01
AG - Phil	165.9	2022-04-01 18:02:52.343528	22-04-01
BGF World Gold	11314.39	2022-04-01 18:02:52.343528	22-04-01
OR - 20F	2028	2022-04-01 18:02:52.343528	22-04-01
Sanofi	13179.6	2022-04-01 18:02:52.343528	22-04-01
OR - 10$	865	2022-04-01 18:02:52.343528	22-04-01
AG - 50F	466.9	2022-04-01 18:02:52.343528	22-04-01
Entrepreteurs	995.39	2022-04-01 18:02:52.343528	22-04-01
ABC Arbitrage	13548.92	2022-04-01 18:02:52.343528	22-04-01
AG - 1F	135	2022-04-01 18:02:52.343528	22-04-01
IShares China Bonds	54744.43	2022-04-01 18:02:52.343528	22-04-01
CC - DBS	411.74	2022-04-01 18:02:52.343528	22-04-01
Cash PEA	14.99	2022-04-01 18:02:52.343528	22-04-01
Prêt Lombard	-30500	2022-04-01 18:02:52.343528	22-04-01
Fond Monétaire	-3.48	2022-04-01 18:02:52.343528	22-04-01
CCC - Hello Bank	271.81	2022-04-01 18:02:52.343528	22-04-01
Danone	10908.59	2022-04-01 18:02:52.343528	22-04-01
BGF World Energy	26490.44	2022-04-01 18:02:52.343528	22-04-01
October	390.71	2022-04-01 18:02:52.343528	22-04-01
IDI	1822.8	2022-04-01 18:02:52.343528	22-04-01
Moury Construct	10816	2022-04-01 18:02:52.343528	22-04-01
Gazprom	507.29	2022-04-01 18:02:52.343528	22-04-01
BGF World Mining	16367.26	2022-04-01 18:02:52.343528	22-04-01
Publicis	10630.44	2022-04-01 18:02:52.343528	22-04-01
Nikko AM ASEAN	3418.5	2022-04-01 18:02:52.343528	22-04-01
Holland Colours	3200	2022-04-01 18:02:52.343528	22-04-01
OR - 50 Peso	6270	2022-04-01 18:02:52.343528	22-04-01
AXA	12421.28	2022-04-01 18:02:52.343528	22-04-01
Flow Traders	10881.3	2022-04-01 18:02:52.343528	22-04-01
BNB	2343.51	2022-04-01 18:02:52.343528	22-04-01
Scor	13561.68	2022-04-01 18:02:52.343528	22-04-01
CBO Territoria	13011.15	2022-04-01 18:02:52.343528	22-04-01
Van de Velde	9588.6	2022-04-01 18:02:52.343528	22-04-01
CT Bourso Cash	0	2022-04-01 18:02:52.343528	22-04-01
Cash PEA-PME	36.67	2022-04-01 18:02:52.343528	22-04-01
BUSD	0.3	2022-04-01 18:02:52.343528	22-04-01
USDT	0.23	2022-04-01 18:02:52.343528	22-04-01
CC - Boursorama	1216.72	2022-04-01 18:02:52.343528	22-04-01
Revolut	1824.93	2022-04-01 18:02:52.343528	22-04-01
US 20+ years	29999.14	2022-04-01 18:02:52.343528	22-04-01
Rubis	324.36	2022-04-01 18:02:52.343528	22-04-01
OR - 10F	3500	2022-04-01 18:03:02.333510	22-04-01
AG - 5F	32.5	2022-04-01 18:03:02.333510	22-04-01
AG - Phil	165.9	2022-04-01 18:03:02.333510	22-04-01
BGF World Gold	11314.39	2022-04-01 18:03:02.333510	22-04-01
OR - 20F	2028	2022-04-01 18:03:02.333510	22-04-01
Sanofi	13179.6	2022-04-01 18:03:02.333510	22-04-01
OR - 10$	865	2022-04-01 18:03:02.333510	22-04-01
AG - 50F	466.9	2022-04-01 18:03:02.333510	22-04-01
Entrepreteurs	995.39	2022-04-01 18:03:02.333510	22-04-01
ABC Arbitrage	13548.92	2022-04-01 18:03:02.333510	22-04-01
AG - 1F	135	2022-04-01 18:03:02.333510	22-04-01
IShares China Bonds	54744.43	2022-04-01 18:03:02.333510	22-04-01
CC - DBS	411.74	2022-04-01 18:03:02.333510	22-04-01
Cash PEA	14.99	2022-04-01 18:03:02.333510	22-04-01
Prêt Lombard	-30500	2022-04-01 18:03:02.333510	22-04-01
Fond Monétaire	-3.48	2022-04-01 18:03:02.333510	22-04-01
CCC - Hello Bank	271.81	2022-04-01 18:03:02.333510	22-04-01
Danone	10908.59	2022-04-01 18:03:02.333510	22-04-01
BGF World Energy	26490.44	2022-04-01 18:03:02.333510	22-04-01
October	390.71	2022-04-01 18:03:02.333510	22-04-01
IDI	1822.8	2022-04-01 18:03:02.333510	22-04-01
Moury Construct	10816	2022-04-01 18:03:02.333510	22-04-01
Gazprom	507.29	2022-04-01 18:03:02.333510	22-04-01
BGF World Mining	16367.26	2022-04-01 18:03:02.333510	22-04-01
Publicis	10630.44	2022-04-01 18:03:02.333510	22-04-01
Nikko AM ASEAN	3418.5	2022-04-01 18:03:02.333510	22-04-01
Holland Colours	3200	2022-04-01 18:03:02.333510	22-04-01
OR - 50 Peso	6270	2022-04-01 18:03:02.333510	22-04-01
AXA	12421.28	2022-04-01 18:03:02.333510	22-04-01
Flow Traders	10881.3	2022-04-01 18:03:02.333510	22-04-01
BNB	2343.51	2022-04-01 18:03:02.333510	22-04-01
Scor	13561.68	2022-04-01 18:03:02.333510	22-04-01
CBO Territoria	13011.15	2022-04-01 18:03:02.333510	22-04-01
Van de Velde	9588.6	2022-04-01 18:03:02.333510	22-04-01
CT Bourso Cash	0	2022-04-01 18:03:02.333510	22-04-01
Cash PEA-PME	36.67	2022-04-01 18:03:02.333510	22-04-01
BUSD	0.3	2022-04-01 18:03:02.333510	22-04-01
USDT	0.23	2022-04-01 18:03:02.333510	22-04-01
CC - Boursorama	1216.72	2022-04-01 18:03:02.333510	22-04-01
Revolut	1824.93	2022-04-01 18:03:02.333510	22-04-01
US 20+ years	29999.14	2022-04-01 18:03:02.333510	22-04-01
Rubis	324.36	2022-04-01 18:03:02.333510	22-04-01
OR - 10F	3500	2022-04-01 18:17:55.575811	22-04-01
AG - 5F	32.5	2022-04-01 18:17:55.575811	22-04-01
AG - Phil	166.6	2022-04-01 18:17:55.575811	22-04-01
BGF World Gold	11312.92	2022-04-01 18:17:55.575811	22-04-01
OR - 20F	2028	2022-04-01 18:17:55.575811	22-04-01
Sanofi	13179.6	2022-04-01 18:17:55.575811	22-04-01
OR - 10$	865	2022-04-01 18:17:55.575811	22-04-01
AG - 50F	466.9	2022-04-01 18:17:55.575811	22-04-01
Entrepreteurs	995.39	2022-04-01 18:17:55.575811	22-04-01
ABC Arbitrage	13548.92	2022-04-01 18:17:55.575811	22-04-01
AG - 1F	135	2022-04-01 18:17:55.575811	22-04-01
IShares China Bonds	54735.97	2022-04-01 18:17:55.575811	22-04-01
CC - DBS	411.69	2022-04-01 18:17:55.575811	22-04-01
Cash PEA	14.99	2022-04-01 18:17:55.575811	22-04-01
Prêt Lombard	-30500	2022-04-01 18:17:55.575811	22-04-01
Fond Monétaire	-3.48	2022-04-01 18:17:55.575811	22-04-01
CCC - Hello Bank	271.81	2022-04-01 18:17:55.575811	22-04-01
Danone	10908.59	2022-04-01 18:17:55.575811	22-04-01
BGF World Energy	26486.98	2022-04-01 18:17:55.575811	22-04-01
October	390.71	2022-04-01 18:17:55.575811	22-04-01
IDI	1822.8	2022-04-01 18:17:55.575811	22-04-01
Moury Construct	10816	2022-04-01 18:17:55.575811	22-04-01
Gazprom	507.21	2022-04-01 18:17:55.575811	22-04-01
BGF World Mining	16365.13	2022-04-01 18:17:55.575811	22-04-01
Publicis	10630.44	2022-04-01 18:17:55.575811	22-04-01
Nikko AM ASEAN	3418.05	2022-04-01 18:17:55.575811	22-04-01
Holland Colours	3200	2022-04-01 18:17:55.575811	22-04-01
OR - 50 Peso	6270	2022-04-01 18:17:55.575811	22-04-01
AXA	12421.28	2022-04-01 18:17:55.575811	22-04-01
Flow Traders	10881.3	2022-04-01 18:17:55.575811	22-04-01
BNB	2339.75	2022-04-01 18:17:55.575811	22-04-01
Scor	13561.68	2022-04-01 18:17:55.575811	22-04-01
CBO Territoria	13011.15	2022-04-01 18:17:55.575811	22-04-01
Van de Velde	9588.6	2022-04-01 18:17:55.575811	22-04-01
CT Bourso Cash	0	2022-04-01 18:17:55.575811	22-04-01
Cash PEA-PME	36.67	2022-04-01 18:17:55.575811	22-04-01
BUSD	0.3	2022-04-01 18:17:55.575811	22-04-01
USDT	0.23	2022-04-01 18:17:55.575811	22-04-01
CC - Boursorama	1216.72	2022-04-01 18:17:55.575811	22-04-01
Revolut	1824.65	2022-04-01 18:17:55.575811	22-04-01
US 20+ years	29994.5	2022-04-01 18:17:55.575811	22-04-01
Rubis	324.36	2022-04-01 18:17:55.575811	22-04-01
OR - 10F	3500	2022-04-01 18:17:59.175707	22-04-01
AG - 5F	32.5	2022-04-01 18:17:59.175707	22-04-01
AG - Phil	166.6	2022-04-01 18:17:59.175707	22-04-01
BGF World Gold	11312.92	2022-04-01 18:17:59.175707	22-04-01
OR - 20F	2028	2022-04-01 18:17:59.175707	22-04-01
Sanofi	13179.6	2022-04-01 18:17:59.175707	22-04-01
OR - 10$	865	2022-04-01 18:17:59.175707	22-04-01
AG - 50F	466.9	2022-04-01 18:17:59.175707	22-04-01
Entrepreteurs	995.39	2022-04-01 18:17:59.175707	22-04-01
ABC Arbitrage	13548.92	2022-04-01 18:17:59.175707	22-04-01
AG - 1F	135	2022-04-01 18:17:59.175707	22-04-01
IShares China Bonds	54735.97	2022-04-01 18:17:59.175707	22-04-01
CC - DBS	411.69	2022-04-01 18:17:59.175707	22-04-01
Cash PEA	14.99	2022-04-01 18:17:59.175707	22-04-01
Prêt Lombard	-30500	2022-04-01 18:17:59.175707	22-04-01
Fond Monétaire	-3.48	2022-04-01 18:17:59.175707	22-04-01
CCC - Hello Bank	271.81	2022-04-01 18:17:59.175707	22-04-01
Danone	10908.59	2022-04-01 18:17:59.175707	22-04-01
BGF World Energy	26486.98	2022-04-01 18:17:59.175707	22-04-01
October	390.71	2022-04-01 18:17:59.175707	22-04-01
IDI	1822.8	2022-04-01 18:17:59.175707	22-04-01
Moury Construct	10816	2022-04-01 18:17:59.175707	22-04-01
Gazprom	507.21	2022-04-01 18:17:59.175707	22-04-01
BGF World Mining	16365.13	2022-04-01 18:17:59.175707	22-04-01
Publicis	10630.44	2022-04-01 18:17:59.175707	22-04-01
Nikko AM ASEAN	3418.05	2022-04-01 18:17:59.175707	22-04-01
Holland Colours	3200	2022-04-01 18:17:59.175707	22-04-01
OR - 50 Peso	6270	2022-04-01 18:17:59.175707	22-04-01
AXA	12421.28	2022-04-01 18:17:59.175707	22-04-01
Flow Traders	10881.3	2022-04-01 18:17:59.175707	22-04-01
BNB	2339.75	2022-04-01 18:17:59.175707	22-04-01
Scor	13561.68	2022-04-01 18:17:59.175707	22-04-01
CBO Territoria	13011.15	2022-04-01 18:17:59.175707	22-04-01
Van de Velde	9588.6	2022-04-01 18:17:59.175707	22-04-01
CT Bourso Cash	0	2022-04-01 18:17:59.175707	22-04-01
Cash PEA-PME	36.67	2022-04-01 18:17:59.175707	22-04-01
BUSD	0.3	2022-04-01 18:17:59.175707	22-04-01
USDT	0.23	2022-04-01 18:17:59.175707	22-04-01
CC - Boursorama	1216.72	2022-04-01 18:17:59.175707	22-04-01
Revolut	1824.65	2022-04-01 18:17:59.175707	22-04-01
US 20+ years	29994.5	2022-04-01 18:17:59.175707	22-04-01
Rubis	324.36	2022-04-01 18:17:59.175707	22-04-01
OR - 10F	3500	2022-04-01 18:20:37.232650	22-04-01
AG - 5F	32.5	2022-04-01 18:20:37.232650	22-04-01
AG - Phil	166.6	2022-04-01 18:20:37.232650	22-04-01
BGF World Gold	11312.35	2022-04-01 18:20:37.232650	22-04-01
OR - 20F	2028	2022-04-01 18:20:37.232650	22-04-01
Sanofi	13179.6	2022-04-01 18:20:37.232650	22-04-01
OR - 10$	865	2022-04-01 18:20:37.232650	22-04-01
AG - 50F	466.9	2022-04-01 18:20:37.232650	22-04-01
Entrepreteurs	995.39	2022-04-01 18:20:37.232650	22-04-01
ABC Arbitrage	13548.92	2022-04-01 18:20:37.232650	22-04-01
AG - 1F	135	2022-04-01 18:20:37.232650	22-04-01
IShares China Bonds	54735.97	2022-04-01 18:20:37.232650	22-04-01
CC - DBS	411.67	2022-04-01 18:20:37.232650	22-04-01
Cash PEA	14.99	2022-04-01 18:20:37.232650	22-04-01
Prêt Lombard	-30500	2022-04-01 18:20:37.232650	22-04-01
Fond Monétaire	-3.48	2022-04-01 18:20:37.232650	22-04-01
CCC - Hello Bank	271.81	2022-04-01 18:20:37.232650	22-04-01
Danone	10908.59	2022-04-01 18:20:37.232650	22-04-01
BGF World Energy	26485.66	2022-04-01 18:20:37.232650	22-04-01
October	390.71	2022-04-01 18:20:37.232650	22-04-01
IDI	1822.8	2022-04-01 18:20:37.232650	22-04-01
Moury Construct	10816	2022-04-01 18:20:37.232650	22-04-01
Gazprom	507.21	2022-04-01 18:20:37.232650	22-04-01
BGF World Mining	16364.31	2022-04-01 18:20:37.232650	22-04-01
Publicis	10630.44	2022-04-01 18:20:37.232650	22-04-01
Nikko AM ASEAN	3417.88	2022-04-01 18:20:37.232650	22-04-01
Holland Colours	3200	2022-04-01 18:20:37.232650	22-04-01
OR - 50 Peso	6270	2022-04-01 18:20:37.232650	22-04-01
AXA	12421.28	2022-04-01 18:20:37.232650	22-04-01
Flow Traders	10881.3	2022-04-01 18:20:37.232650	22-04-01
BNB	2339.9	2022-04-01 18:20:37.232650	22-04-01
Scor	13561.68	2022-04-01 18:20:37.232650	22-04-01
CBO Territoria	13011.15	2022-04-01 18:20:37.232650	22-04-01
Van de Velde	9588.6	2022-04-01 18:20:37.232650	22-04-01
CT Bourso Cash	0	2022-04-01 18:20:37.232650	22-04-01
Cash PEA-PME	36.67	2022-04-01 18:20:37.232650	22-04-01
BUSD	0.3	2022-04-01 18:20:37.232650	22-04-01
USDT	0.23	2022-04-01 18:20:37.232650	22-04-01
CC - Boursorama	1216.72	2022-04-01 18:20:37.232650	22-04-01
Revolut	1824.65	2022-04-01 18:20:37.232650	22-04-01
US 20+ years	29994.5	2022-04-01 18:20:37.232650	22-04-01
Rubis	324.36	2022-04-01 18:20:37.232650	22-04-01
\.

COPY rente_stg (action, dividende, date, day) FROM stdin;
Sanofi	3.33	2022-03-31 19:51:41.883623	22-03-31
AXA	1.54	2022-03-31 19:51:41.883623	22-03-31
ABC Arbitrage	0.4	2022-03-31 19:51:41.883623	22-03-31
Publicis	2.4	2022-03-31 19:51:41.883623	22-03-31
Danone	1.94	2022-03-31 19:51:41.883623	22-03-31
Flow Traders	1.1475	2022-03-31 19:51:41.883623	22-03-31
Moury Construct	5.88	2022-03-31 19:51:41.883623	22-03-31
Holland Colours	5.1425	2022-03-31 19:51:41.883623	22-03-31
Scor	1.8	2022-03-31 19:51:41.883623	22-03-31
CBO Territoria	0.24	2022-03-31 19:51:41.883623	22-03-31
Van de Velde	1.4	2022-03-31 19:51:41.883623	22-03-31
IDI	3.4	2022-03-31 19:51:41.883623	22-03-31
Sanofi	3.33	2022-03-31 19:51:48.534309	22-03-31
AXA	1.54	2022-03-31 19:51:48.534309	22-03-31
ABC Arbitrage	0.4	2022-03-31 19:51:48.534309	22-03-31
Publicis	2.4	2022-03-31 19:51:48.534309	22-03-31
Danone	1.94	2022-03-31 19:51:48.534309	22-03-31
Flow Traders	1.1475	2022-03-31 19:51:48.534309	22-03-31
Moury Construct	5.88	2022-03-31 19:51:48.534309	22-03-31
Holland Colours	5.1425	2022-03-31 19:51:48.534309	22-03-31
Scor	1.8	2022-03-31 19:51:48.534309	22-03-31
CBO Territoria	0.24	2022-03-31 19:51:48.534309	22-03-31
Van de Velde	1.4	2022-03-31 19:51:48.534309	22-03-31
IDI	3.4	2022-03-31 19:51:48.534309	22-03-31
Sanofi	3.33	2022-03-31 20:01:04.994937	22-03-31
AXA	1.54	2022-03-31 20:01:04.994937	22-03-31
ABC Arbitrage	0.4	2022-03-31 20:01:04.994937	22-03-31
Publicis	2.4	2022-03-31 20:01:04.994937	22-03-31
Danone	1.94	2022-03-31 20:01:04.994937	22-03-31
Flow Traders	1.1475	2022-03-31 20:01:04.994937	22-03-31
Moury Construct	5.88	2022-03-31 20:01:04.994937	22-03-31
Holland Colours	5.1425	2022-03-31 20:01:04.994937	22-03-31
Scor	1.8	2022-03-31 20:01:04.994937	22-03-31
CBO Territoria	0.24	2022-03-31 20:01:04.994937	22-03-31
Van de Velde	1.4	2022-03-31 20:01:04.994937	22-03-31
IDI	3.4	2022-03-31 20:01:04.994937	22-03-31
Sanofi	3.33	2022-04-01 18:02:52.343545	22-04-01
AXA	1.54	2022-04-01 18:02:52.343545	22-04-01
ABC Arbitrage	0.4	2022-04-01 18:02:52.343545	22-04-01
Publicis	2.4	2022-04-01 18:02:52.343545	22-04-01
Danone	1.94	2022-04-01 18:02:52.343545	22-04-01
Flow Traders	1.1475	2022-04-01 18:02:52.343545	22-04-01
Moury Construct	5.88	2022-04-01 18:02:52.343545	22-04-01
Holland Colours	5.1425	2022-04-01 18:02:52.343545	22-04-01
Scor	1.8	2022-04-01 18:02:52.343545	22-04-01
CBO Territoria	0.24	2022-04-01 18:02:52.343545	22-04-01
Van de Velde	1.4	2022-04-01 18:02:52.343545	22-04-01
IDI	3.4	2022-04-01 18:02:52.343545	22-04-01
Rubis	1.8	2022-04-01 18:02:52.343545	22-04-01
Sanofi	3.33	2022-04-01 18:03:02.333535	22-04-01
AXA	1.54	2022-04-01 18:03:02.333535	22-04-01
ABC Arbitrage	0.4	2022-04-01 18:03:02.333535	22-04-01
Publicis	2.4	2022-04-01 18:03:02.333535	22-04-01
Danone	1.94	2022-04-01 18:03:02.333535	22-04-01
Flow Traders	1.1475	2022-04-01 18:03:02.333535	22-04-01
Moury Construct	5.88	2022-04-01 18:03:02.333535	22-04-01
Holland Colours	5.1425	2022-04-01 18:03:02.333535	22-04-01
Scor	1.8	2022-04-01 18:03:02.333535	22-04-01
CBO Territoria	0.24	2022-04-01 18:03:02.333535	22-04-01
Van de Velde	1.4	2022-04-01 18:03:02.333535	22-04-01
IDI	3.4	2022-04-01 18:03:02.333535	22-04-01
Rubis	1.8	2022-04-01 18:03:02.333535	22-04-01
Sanofi	3.33	2022-04-01 18:17:55.575836	22-04-01
AXA	1.54	2022-04-01 18:17:55.575836	22-04-01
ABC Arbitrage	0.4	2022-04-01 18:17:55.575836	22-04-01
Publicis	2.4	2022-04-01 18:17:55.575836	22-04-01
Danone	1.94	2022-04-01 18:17:55.575836	22-04-01
Flow Traders	1.1475	2022-04-01 18:17:55.575836	22-04-01
Moury Construct	5.88	2022-04-01 18:17:55.575836	22-04-01
Holland Colours	5.1425	2022-04-01 18:17:55.575836	22-04-01
Scor	1.8	2022-04-01 18:17:55.575836	22-04-01
CBO Territoria	0.24	2022-04-01 18:17:55.575836	22-04-01
Van de Velde	1.4	2022-04-01 18:17:55.575836	22-04-01
IDI	3.4	2022-04-01 18:17:55.575836	22-04-01
Rubis	1.8	2022-04-01 18:17:55.575836	22-04-01
Sanofi	3.33	2022-04-01 18:17:59.175731	22-04-01
AXA	1.54	2022-04-01 18:17:59.175731	22-04-01
ABC Arbitrage	0.4	2022-04-01 18:17:59.175731	22-04-01
Publicis	2.4	2022-04-01 18:17:59.175731	22-04-01
Danone	1.94	2022-04-01 18:17:59.175731	22-04-01
Flow Traders	1.1475	2022-04-01 18:17:59.175731	22-04-01
Moury Construct	5.88	2022-04-01 18:17:59.175731	22-04-01
Holland Colours	5.1425	2022-04-01 18:17:59.175731	22-04-01
Scor	1.8	2022-04-01 18:17:59.175731	22-04-01
CBO Territoria	0.24	2022-04-01 18:17:59.175731	22-04-01
Van de Velde	1.4	2022-04-01 18:17:59.175731	22-04-01
IDI	3.4	2022-04-01 18:17:59.175731	22-04-01
Rubis	1.8	2022-04-01 18:17:59.175731	22-04-01
Sanofi	3.33	2022-04-01 18:20:37.232668	22-04-01
AXA	1.54	2022-04-01 18:20:37.232668	22-04-01
ABC Arbitrage	0.4	2022-04-01 18:20:37.232668	22-04-01
Publicis	2.4	2022-04-01 18:20:37.232668	22-04-01
Danone	1.94	2022-04-01 18:20:37.232668	22-04-01
Flow Traders	1.1475	2022-04-01 18:20:37.232668	22-04-01
Moury Construct	5.88	2022-04-01 18:20:37.232668	22-04-01
Holland Colours	5.1425	2022-04-01 18:20:37.232668	22-04-01
Scor	1.8	2022-04-01 18:20:37.232668	22-04-01
CBO Territoria	0.24	2022-04-01 18:20:37.232668	22-04-01
Van de Velde	1.4	2022-04-01 18:20:37.232668	22-04-01
IDI	3.4	2022-04-01 18:20:37.232668	22-04-01
Rubis	1.8	2022-04-01 18:20:37.232668	22-04-01
\.

COMMIT;
ANALYZE details_stg;
ANALYZE rente_stg;


