# 03 · Capacidade operacional: premissas reproduzíveis

## A equação presente no slide 04 do projeto

```text
fotógrafos = 4
janela_operacional = 100 min
aproveitamento_efetivo = 0,75
tempo_por_grupo = 3 min

capacidade = fotógrafos × janela × aproveitamento / tempo_por_grupo
           = 4 × 100 × 0,75 / 3
           = 100 grupos da torcida
```

**Interpretação:** 100 grupos é uma meta nominal de planejamento, **não uma previsão estatística de participação**, não uma promessa de público atendido e não uma medição feita no estádio.

### O que entra no ciclo de 3 minutos?

Abordagem/convite, confirmação de que o grupo aceita participar, posicionamento, dois disparos, entrega das duas fotografias e reposicionamento do profissional para a abordagem seguinte. A **revelação ~90 s** acontece em paralelo e **não é acrescida integralmente** ao ciclo do fotógrafo. A estimativa de 3 min ainda depende de ensaio com o equipamento exato.

### Custos de filme sem confundir com vazão de atendimento

O projeto indica **300 exposições**: 100 grupos da torcida × 2 = **200 fotos**; até 25 grupos dos bastidores × 2 = **50 fotos**; **50 fotos** de testes/perdas. O segmento de bastidores tem cronograma de Comunicação/Futebol próprio, não consome automaticamente os 100 minutos destinados aos quatro fotógrafos itinerantes.

### Sensibilidade simples

| Ciclo por grupo | Eficiência 60% | Eficiência 75% | Eficiência 90% |
| ---: | ---: | ---: | ---: |
| 2,5 min | 96 | 120 | 144 |
| 3,0 min | 80 | **100** | 120 |
| 3,5 min | 68 | 85 | 102 |
| 4,0 min | 60 | 75 | 90 |

Quantidades inteiras **arredondadas para baixo** (sem prometer que atingiremos o teto). Cenários não representam resultados observados. Valores detalhados no CSV e na calculadora Python.

### Gargalos que o cálculo não resolve sozinho

- **Conversão do convite:** um profissional pode dedicar tempo a pessoas que não querem participar; a perda é parcialmente representada no fator de eficiência, mas não foi medida.
- **Cartuchos/filmes:** troca e reposição, falha de flash, duas exposições por grupo, iluminação, assentimento e segurança precisam caber no ciclo.
- **Chegada à estrela:** mesmo que a vazão média projetada seja 1 grupo/minuto, horários de pico podem concentrar 2–5 grupos em poucos segundos.
- **Dois apoios:** se cada um leva `s` segundos para orientar uma colagem, a capacidade nominal conjunta é `120/s grupos por minuto`; com `s=60`, seria 2 grupos/minuto antes de descontar pausas. É apenas um **modelo de teste**, não promessa de fluxo livre.
- **Acessibilidade e crianças:** ritmo variável e tempo de participação não devem ser artificialmente reduzidos para “bater meta”.
- **Tempo de revelação:** pode afetar o momento de escolha/colagem, mas não exige que o fotógrafo continue com o grupo; a espera não pode causar aglomeração na passagem.

### Regras para revisar a meta após o ensaio

1. Cronometrar pelo menos uma amostra de grupos de tamanhos e perfis distintos, medindo **ciclo completo**, sem constranger os participantes.
2. Registrar variação e momentos de acúmulo, não apenas média global.
3. Checar a taxa de colagem por minuto separadamente da taxa de fotografia.
4. Atualizar tempo médio de grupo e eficiência real; recalcular a meta sem elevar automaticamente o número de filmes ou a ocupação da estrela.
5. Rebaixar a meta ou encurtar a área de captação se Segurança/Operações exigir.

**Código-fonte da conta:** [`scripts/calcular_slide4.py`](../scripts/calcular_slide4.py).
