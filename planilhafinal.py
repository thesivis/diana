from sqlalchemy import create_engine
# Import pandas
import pandas as pd
import math
import sys
import psycopg2
import psycopg2.extras

con = psycopg2.connect(host='localhost', database='diana',user='postgres', password='123')

cur = con.cursor(cursor_factory = psycopg2.extras.DictCursor)
cur2011 = con.cursor()
limit = 3
tabelas = ['verao']

for tabela in tabelas:

    sql = 'select dia, long, lat, hora, temp, ur, alt, v, cob_pais_solo, cob_arb_solo, solo_exp_solo, a_pav_solo, a_edf_solo, agua_solo from '+tabela+'_2016_fim order by dia, hora'
    cur.execute(sql)
    colnames2016 = [desc[0] for desc in cur.description]
    criar = True
    for d2016 in cur:
        cur2011.execute("select dia, long, lat, hora, temp, ur, alt, v, cob_pais_solo, cob_arb_solo, solo_exp_solo, a_pav_solo, a_edf_solo, agua_solo from "+tabela+"_2012_fim  order by sqrt((long-"+str(d2016['long'])+")*(long-"+str(d2016['long'])+")+(lat-"+str(d2016['lat'])+")*(lat-"+str(d2016['lat'])+")) limit " + str(limit))    

        if(criar):
            colnames2011 = [desc[0] for desc in cur2011.description]
            nomes = list(colnames2016)
            for i in range(limit):
                nomes = nomes+list(colnames2011)
            res = pd.DataFrame(columns=nomes)
            criar = False
            idx=0

        linha = list(d2016)
        for d2011 in cur2011:
            linha = linha + list(d2011)
        res.loc[idx] = linha

        if(idx % 100 == 0):
            print(tabela, idx)

        idx = idx + 1

    res.to_csv('DadosFinal/'+tabela + '.csv',index=False)
con.close()