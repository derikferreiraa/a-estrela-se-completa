"""Verifica apenas consistência aritmética do projeto; NÃO comprova testes de campo."""
from pathlib import Path
import csv

GRUPOS_TORCIDA=100
GRUPOS_BASTIDORES_MAX=25
FOTOS_POR_GRUPO=2
RESERVA_TESTES_PERDAS=50
FOTOS_POR_CARTUCHO=10

torcida=GRUPOS_TORCIDA*FOTOS_POR_GRUPO
bastidores=GRUPOS_BASTIDORES_MAX*FOTOS_POR_GRUPO
total=torcida+bastidores+RESERVA_TESTES_PERDAS
assert (torcida,bastidores,total)==(200,50,300)
assert total%FOTOS_POR_CARTUCHO==0
print(f'Torcida: {torcida} exposições')
print(f'Bastidores: até {bastidores} exposições')
print(f'Testes/refações/perdas: {RESERVA_TESTES_PERDAS} exposições')
print(f'Total: {total} exposições = {total//FOTOS_POR_CARTUCHO} cartuchos de 10')
print('ATENÇÃO: o cálculo não substitui a cotação dos filmes nem o ensaio operacional.')
