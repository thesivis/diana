from sqlalchemy import create_engine
# Import pandas
import pandas as pd
import math
import sys
import psycopg2

engine = create_engine('postgresql://postgres:123@localhost:5432/diana')

renomear1 = {'ALT (m)':'alt','COB. PAIS (%)':'cob_pais',
'COB. ARB.(%)':'cob_arb','SOLO EXP.(%)':'solo_exp','A. PAV.(%)':'a_pav','A. EDF. (%)':'a_edf','ÁGUA(%)':'agua'}

renomear2 = {'T(°C) ':'temp','Ur (%)':'ur','ALT (m)':'alt','V(km/h)':'v'}

# Assign spreadsheet filename to `file`
'''file = 'DADOS REDE NEURAL COBERTURA DO SOLO TRANSECTOS.xlsx'
xl = pd.ExcelFile(file)
for sheet in xl.sheet_names:
    planilha = xl.parse(sheet)
    planilha.rename(columns=renomear1,inplace=True)
    planilha.columns = map(str.lower, planilha.columns)
    print(planilha.columns)
    planilha.to_sql(sheet.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower(), engine)
'''
file = 'DADOS REDE NEURAL ESTAÇÕES UTM.xlsx'
xl = pd.ExcelFile(file)

con = psycopg2.connect(host='localhost', database='diana',user='postgres', password='123')

for sheet in xl.sheet_names:
    print(sheet)
    if('VERÃO' in sheet):
      planilha = xl.parse(sheet)
      planilha.rename(columns=renomear2,inplace=True)
      planilha.columns = map(str.lower, planilha.columns)
      tabela = sheet.replace('.csv','').replace(' ','_').replace('VERÃO','VERAO').lower()
      planilha.to_sql(tabela, engine)
      cur = con.cursor()
      tab = 'cob._transecto_2011-2012'
      if('2016' in sheet):
          tab = 'cob._transecto_2016'
      sql = """CREATE TABLE """+tabela+"""_solo_tudo as select row_number() over (ORDER BY i1.index),i1.index as index_solo, i1.long as long_solo, i1.lat as lat_solo, i1.alt as alt_solo, i1.pontos as pontos_solo, i1.cob_pais as cob_pais_solo, i1.cob_arb as cob_arb_solo, i1.solo_exp as solo_exp_solo, i1.a_pav as a_pav_solo, i1.a_edf as a_edf_solo, i1.agua as agua_solo, i2.index as index, i2.dia as dia, i2.long as long, i2.lat as lat, i2.hora as hora, i2.temp as temp, i2.ur as ur, i2.alt as alt, i2.v as v, sqrt((i1.LONG - i2.LONG)*(i1.LONG - i2.LONG) + (i1.LAT - i2.LAT)*(i1.LAT - i2.LAT)) as distance 
      from \""""+tab+"""\" i1, """+tabela+""" i2"""
      cur.execute(sql)
      con.commit()
      sql = """create index """+tabela+"""_index on """+tabela+""" (index);"""
      cur.execute(sql)
      con.commit()
      sql = """create index """+tabela+"""_solo_tudo_index on """+tabela+"""_solo_tudo (index);"""
      cur.execute(sql)
      con.commit()
      sql = """create table """+tabela+"""_fim as
  select * from """+tabela+"""_solo_tudo i3
  where i3.row_number in (
  select  (
    SELECT i2.row_number 
      from """+tabela+"""_solo_tudo i2
    where i2.index = i1.index
    order by i2.distance
    limit 1
    ) from """+tabela+""" i1 where i1.index = i3.index
  )"""
      cur.execute(sql)
      con.commit()
      sql = """drop table """+tabela+"""_solo_tudo;"""
      cur.execute(sql)
      con.commit()
      sql = """drop table """+tabela+""";"""
      cur.execute(sql)
      con.commit()
