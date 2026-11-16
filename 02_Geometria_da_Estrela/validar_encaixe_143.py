#!/usr/bin/env python3
"""Confere 143 retângulos Instax Mini dentro de estrela regular de 5 pontas.
Reproduz as verificações do documento técnico. Dependências: shapely.
A entrada CSV é de posições já identificadas; este programa não otimiza a distribuição.
"""
import csv, math, sys
from pathlib import Path
from shapely.geometry import Polygon, box

H = 1800.0  # altura útil mm sem base
R = H / (1 + math.sin(math.radians(54)))
r = R * (3-math.sqrt(5))/2
vertices = []
for k in range(10):
    theta = math.radians(90 - 36*k)
    radius = R if k % 2 == 0 else r
    vertices.append((radius * math.cos(theta), radius * math.sin(theta)))
minx = min(p[0] for p in vertices); miny = min(p[1] for p in vertices)
star = Polygon([(x-minx,y-miny) for (x,y) in vertices])
W = max(x for x,y in vertices) - minx
csv_path = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('Botafogo_143_Posicoes_por_Face.csv')
with csv_path.open(encoding='utf-8-sig',newline='') as fd:
    data = list(csv.DictReader(fd))
rects = []
for row in data:
    x=float(row['x_mm_a_partir_da_esquerda']); y=float(row['y_mm_a_partir_da_base_da_estrela'])
    w=float(row['largura_mm']); h=float(row['altura_mm'])
    rects.append(box(x,y,x+w,y+h))
assert len(rects) == 143, f'CSV tem {len(rects)} posicoes; esperado 143'
assert all(star.covers(z) for z in rects), 'Ao menos uma foto sai do contorno'
assert all(rects[i].intersection(rects[j]).area < 1e-6 for i in range(len(rects)) for j in range(i+1,len(rects))), 'Ha sobreposicao'
edge = min(z.distance(star.boundary) for z in rects)
gap = min(rects[i].distance(rects[j]) for i in range(len(rects)) for j in range(i+1,len(rects)))
assert edge >= 29.99, f'recuo insuficiente: {edge:.2f} mm'
assert gap >= 3.99, f'folga insuficiente: {gap:.2f} mm'
print(f'VALIDADO: {len(rects)} fotos, estrela {H:.0f} mm x {W:.1f} mm, area {star.area/1e6:.4f} m2')
print(f'Recuo minimo: {edge:.2f} mm; folga minima: {gap:.2f} mm; sobreposicoes: 0')
print('ATENCAO: geometria validada, nao constitui aceite de producao ou teste de colagem.')
