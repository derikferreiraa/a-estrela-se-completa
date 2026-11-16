from pathlib import Path
import csv
R=Path(__file__).resolve().parents[1]
for folder in ('assets','docs','dados'): assert (R/folder).is_dir(),folder
for name,required in [('aderencia-briefing.csv',{'id','status_revisao','evidencia'}),('registro-decisoes.csv',{'id','status_de_projeto','aprovar_em_producao'}),('plano-validacao.csv',{'id','status','evidencia'})]:
 with (R/'dados'/name).open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
 assert rows and required.issubset(rows[0].keys()),name
 if name=='aderencia-briefing.csv':assert all(x['status_revisao']=='nao verificado' and not x['evidencia'] for x in rows)
 if name=='plano-validacao.csv':assert all(x['status']=='nao verificado' and not x['evidencia'] for x in rows)
 if name=='registro-decisoes.csv':assert all(not x['aprovar_em_producao'] for x in rows)
assert len(list((R/'docs').glob('*.md')))==10
assert len(list((R/'assets').glob('grafico*.png')))==4
print('OK: 10 estudos, 4 gráficos e modelos sem aceites ou evidências fictícios.')

with (R/'dados'/'alternativas-conceituais.csv').open(encoding='utf-8-sig',newline='') as f:
 rows=list(csv.DictReader(f))
assert len(rows)==3 and sum(x['situacao_de_projeto'].startswith('selecionada') for x in rows)==1
assert all(not x['evidencia_de_teste'] and not x['aceite_saf'] for x in rows)
print('OK: 3 alternativas sem notas ou aprovações fictícias.')
