\COPY (SELECT * FROM inverno_2011_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/inverno_2011_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM inverno_2016_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/inverno_2016_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM primavera_2011_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/primavera_2011_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM primavera_2016_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/primavera_2016_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM outono_2011_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/outono_2011_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM outono_2016_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadDadosComSoloosFinal/outono_2016_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM verao_2012_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/verao_2012_fim.csv' DELIMITER ',' CSV HEADER;
\COPY (SELECT * FROM verao_2016_fim) TO '/home/raphael/Codigo/git/theprojects/diana/DadosComSolo/verao_2016_fim.csv' DELIMITER ',' CSV HEADER;
