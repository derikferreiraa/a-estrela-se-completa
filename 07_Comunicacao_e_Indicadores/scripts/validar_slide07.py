from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
REQ={
 'controle-editorial.csv':('id','momento','entregavel','responsavel_previsto','resultado'),
 'matriz-validacao.csv':('id','especificacao','validacao_requerida','area_prevista','status'),
 'indicadores-modelo.csv':('indicador','unidade','meta_ou_previsao','realizado'),
}
for name,cols in REQ.items():
 with (ROOT/'dados'/name).open(encoding='utf-8-sig',newline='') as f:
  rows=list(csv.DictReader(f))
 assert rows, name+' sem linhas'
 assert set(cols).issubset(rows[0]), (name,cols)
 if name=='matriz-validacao.csv':
  assert all(row['status']=='nao verificado' for row in rows), 'O modelo nao pode presumir aprovacoes'
 if name=='indicadores-modelo.csv':
  assert all(not row['realizado'].strip() for row in rows), 'Nao inserir resultados ficticios'
ids={}
with (ROOT/'dados'/'matriz-validacao.csv').open(encoding='utf-8-sig',newline='') as f:
 ids={r['id'] for r in csv.DictReader(f)}
assert len(ids)==7
with (ROOT/'dados'/'indicadores-modelo.csv').open(encoding='utf-8-sig',newline='') as f:
 metrics={r['indicador']:r['meta_ou_previsao'] for r in csv.DictReader(f)}
assert metrics['grupos_torcida']=='100'
assert metrics['grupos_bastidores']=='ate 25'
assert metrics['exposicoes_previstas']=='300'
print('OK: estrutura e metas do projeto coerentes. Nenhuma aprovacao ou resultado preenchido.')
