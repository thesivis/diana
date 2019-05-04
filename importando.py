from sqlalchemy import create_engine
# Import pandas
import pandas as pd
import math
import sys
import os

colunas = ['DIA', 'LONG', 'LAT', 'HORA', 'T(°C) ', 'Ur (%)', 'ALT (m)', 'V(km/h)',
       'LONG.1', 'LAT.1', 'ALT (m).1', 'PONTOS',
       'COB. PAIS (%)', 'COB. ARB.(%)', 'SOLO EXP.(%)',
       'A. PAV.(%)', 'A. EDF. (%)', 'ÁGUA(%)']

renomear = {'T(°C) ':'temp','Ur (%)':'ur','ALT (m)':'alt','V(km/h)':'v','COB. PAIS (%)':'cob_pais',
'COB. ARB.(%)':'cob_arb','SOLO EXP.(%)':'solo_exp','A. PAV.(%)':'a_pav','A. EDF. (%)':'a_edf','ÁGUA(%)':'agua',
'ALT (m).1':'alt_m_1'}

engine = create_engine('postgresql://postgres:123@localhost:5432/diana')

arquivos = os.listdir('2016/')
for arquivo in arquivos:
    arq = pd.read_csv('2016/'+arquivo, usecols=colunas)
    arq.rename(columns=renomear,inplace=True)
    arq.columns = map(str.lower, arq.columns)
    arq.to_sql(arquivo.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower(), engine)


arquivos = os.listdir('2011/')
for arquivo in arquivos:
    arq = pd.read_csv('2011/'+arquivo, usecols=colunas)
    arq.rename(columns=renomear,inplace=True)
    arq.columns = map(str.lower, arq.columns)
    arq.to_sql(arquivo.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower(), engine)