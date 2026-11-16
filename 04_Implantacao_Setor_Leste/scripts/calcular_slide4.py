#!/usr/bin/env python3
"""Calculadora auditável do slide 04 do projeto. Somente biblioteca padrão.

Premissas são cenários, não dados de vistoria. 90 s é média aproximada de
revelação da Instax Mini (fabricante), NÃO uma duração garantida.
"""
import argparse
import math

FOTOGRAFOS = 4
JANELA_MIN = 100.0
EFICIENCIA = 0.75
CICLO_MIN = 3.0
REVELACAO_SEG = 90.0


def capacidade_grupos(fotografos=FOTOGRAFOS, janela_min=JANELA_MIN,
                     eficiencia=EFICIENCIA, ciclo_min=CICLO_MIN):
    if fotografos < 0 or janela_min < 0 or not 0 <= eficiencia <= 1 or ciclo_min <= 0:
        raise ValueError('Premissas inválidas de capacidade')
    return math.floor(fotografos * janela_min * eficiencia / ciclo_min)


def deslocamento(distancia_m, velocidade_mps, manuseio_seg=0,
                 interacao_seg=0, revelacao_seg=REVELACAO_SEG):
    if min(distancia_m, manuseio_seg, interacao_seg, revelacao_seg) < 0 or velocidade_mps <= 0:
        raise ValueError('Distâncias, tempos e velocidade devem ser válidos')
    caminhada = distancia_m / velocidade_mps
    decorrido = manuseio_seg + caminhada + interacao_seg
    return {
        'caminhada_seg': caminhada,
        'decorrido_seg': decorrido,
        'residual_aprox_seg': max(0.0, revelacao_seg - decorrido),
        'revelacao_referencial_ultrapassada': decorrido >= revelacao_seg,
    }


def espera_ate_escolha(decorrido_seg, instante_escolha_seg):
    """Espera teórica até escolher a foto, usando tempo medido em ensaio.

    Ambos os tempos são contados desde a ejeção da segunda fotografia.
    Não presume que 90 segundos seja o instante da primeira imagem visível.
    """
    if decorrido_seg < 0 or instante_escolha_seg < 0:
        raise ValueError('Tempos não podem ser negativos')
    return max(0.0, instante_escolha_seg - decorrido_seg)


def main():
    p = argparse.ArgumentParser(description='Memória de cálculo — Slide 04 SAF Botafogo ()')
    p.add_argument('--distancia', type=float, default=20, help='m, hipótese; NÃO medido no estádio')
    p.add_argument('--velocidade', type=float, default=0.8, help='m/s, hipótese')
    p.add_argument('--manuseio', type=float, default=0, help='s da ejeção à saída, hipótese')
    p.add_argument('--interacao', type=float, default=0, help='s para observar antes da colagem, hipótese')
    p.add_argument('--revelacao', type=float, default=90, help='s referenciais, variáveis com temperatura')
    p.add_argument('--foto-escolhivel', type=float, default=None, help='s MEDIDOS desde a segunda ejeção até foto escolhível; não estimar sem ensaio')
    p.add_argument('--fotografos', type=int, default=FOTOGRAFOS)
    p.add_argument('--janela', type=float, default=JANELA_MIN)
    p.add_argument('--eficiencia', type=float, default=EFICIENCIA)
    p.add_argument('--ciclo', type=float, default=CICLO_MIN)
    args=p.parse_args()
    cap=capacidade_grupos(args.fotografos,args.janela,args.eficiencia,args.ciclo)
    des=deslocamento(args.distancia,args.velocidade,args.manuseio,args.interacao,args.revelacao)
    print('Slide 04 — SAF Botafogo')
    print(f'Capacidade projetada: {cap} grupos da torcida (não é dado observado)')
    print(f'Caminhada: {des["caminhada_seg"]:.1f} s')
    print(f'Decorrido desde a ejeção considerada: {des["decorrido_seg"]:.1f} s')
    print(f'Residual até o marco APROX. de {args.revelacao:.0f} s: {des["residual_aprox_seg"]:.1f} s')
    print('A imagem revela gradualmente; não há garantia de tempo fixo, nem medição do percurso real.')
    if args.foto_escolhivel is not None:
        print(f'Espera teórica por escolha, a partir do teste: {espera_ate_escolha(des["decorrido_seg"], args.foto_escolhivel):.1f} s')
    print('Hipóteses históricas: distância 15–25 m; velocidade e interações: editar após ensaio.')

if __name__=='__main__':
    main()
