import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'scripts'))
from calcular_slide4 import capacidade_grupos, deslocamento, espera_ate_escolha

class CalculosDoSlide4(unittest.TestCase):
    def test_capacidade_projeto(self):
        self.assertEqual(capacidade_grupos(),100)

    def test_cenario_vinte_metros(self):
        x=deslocamento(20,0.8)
        self.assertAlmostEqual(x['caminhada_seg'],25)
        self.assertAlmostEqual(x['residual_aprox_seg'],65)

    def test_revelacao_com_etapas(self):
        x=deslocamento(20,0.8,15,20)
        self.assertAlmostEqual(x['decorrido_seg'],60)
        self.assertAlmostEqual(x['residual_aprox_seg'],30)

    def test_cenario_lento_25_metros(self):
        self.assertAlmostEqual(deslocamento(25,.6)['caminhada_seg'],41.6666667,places=5)

    def test_escolha_ainda_nao_visivel(self):
        self.assertEqual(espera_ate_escolha(60,80),20)

    def test_escolha_ja_possivel(self):
        self.assertEqual(espera_ate_escolha(60,45),0)

    def test_erro_de_velocidade(self):
        with self.assertRaises(ValueError):
            deslocamento(20,0)

if __name__=='__main__':
    unittest.main()
