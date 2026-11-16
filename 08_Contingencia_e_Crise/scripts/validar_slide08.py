#!/usr/bin/env python3
"""Verifica integridade dos modelos, nao certifica a seguranca nem declara GO."""
import csv
from pathlib import Path
D=Path(__file__).resolve().parent.parent/'dados'
def load(name):
 with (D/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def check():
 marcos=load('marcos-de-decisao.csv'); planos=load('planos-e-aceites.csv'); gates=load('checklist-go-nogo.csv')
 assert [x['marco'] for x in marcos]==['D-2','12h','13h30','15h','16h (prev.)']
 assert [x['plano'] for x in planos]==['A','B','C']
 assert len(gates)>=8
 allowed={'nao verificado','em analise','aprovado','reprovado'}
 for table in (marcos,planos,gates):
  for row in table:
   assert all(k.strip() for k in row.keys())
   assert any(v.strip() for v in row.values())
 for row in marcos:assert row['situacao'] in allowed
 for row in planos:
  for k in ('local_autorizado','teste_de_fixacao','circulacao_aprovada','aceite_operacoes','resultado'):
   assert row[k] in allowed
 for row in gates:assert row['situacao'] in allowed
 # A conclusão operacional exige registro específico; status não verificado jamais equivale a GO.
 go=all(x['situacao']=='aprovado' for x in gates if x['criticidade']=='critico')
 print('Estrutura e campos: OK | Marcos: 5 | Planos: 3 | Verificacoes: '+str(len(gates)))
 print('Liberacao operacional automatica: '+('NAO APLICAVEL — aceite humano ainda obrigatorio' if go else 'NAO — existe validacao critica pendente'))
if __name__=='__main__':check()
