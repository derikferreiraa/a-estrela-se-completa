#!/usr/bin/env python3
"""Verifica coerência de estrutura, sem atribuir aprovação aos marcos."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
with (root/'dados'/'marcos-e-aceites.csv').open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f,delimiter=';'))
expected=['D-28','D-21','D-10','D-3','D-2','JOGO','D+7']
assert [x['marco'] for x in rows]==expected, 'Marcos divergentes do projeto.'
assert len(rows)==7
assert all(x['status']=='não iniciado' for x in rows), 'Não preencha aceite sem evidência.'
assert all(x['entrega_prevista'] and x['area_que_valida'] for x in rows)
with (root/'dados'/'responsabilidades.csv').open(encoding='utf-8-sig',newline='') as f:
    resp=list(csv.DictReader(f,delimiter=';'))
assert len(resp)==7
assert all(not x['responsavel_nome'] for x in resp)
with (root/'dados'/'checklist-matchday.csv').open(encoding='utf-8-sig',newline='') as f:
    checks=list(csv.DictReader(f,delimiter=';'))
assert len(checks)>=9
assert all(not x['resultado'] for x in checks)
print(f'OK: {len(rows)} marcos; {len(resp)} áreas; {len(checks)} verificações. Sem aprovações fictícias.')
