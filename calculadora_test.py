import unittest
from calculadora import Calculadora


# INSTALAÇÃO NECESSÁRIA:
# pip install unittest-xml-reporting
# pip install coverage

# EXECUTAR OS TESTES:
# py -m unittest discover -v
# py -m unittest calculadora_test.py
# python -m coverage run -m unittest calculadora_test.py
# python -m coverage report -m


class TestCalculadora(unittest.TestCase):
    """
    Classe de testes unitários para o sistema de Calculadora.
    Baseada nos casos de uso UC-01, UC-02, UC-03 e UC-04.
    Testes simplificados mantendo cobertura completa.
    """

    # ========== TESTES UC-01: REALIZAR SOMA ==========
    
    def test_soma_casos_basicos(self):
        """Testa soma com diferentes combinações - Fluxo Principal"""
        self.assertEqual(Calculadora.soma(3, 2), 5)
        self.assertEqual(Calculadora.soma(-5, -3), -8)
        self.assertEqual(Calculadora.soma(-1, 1), 0)
        self.assertEqual(Calculadora.soma(0, 5), 5)
    
    def test_soma_overflow(self):
        """Testa overflow em ambas direções - Fluxo Alternativo 5b"""
        self.assertEqual(Calculadora.soma(60, 50), "Erro: Overflow")
        self.assertEqual(Calculadora.soma(-60, -50), "Erro: Overflow")
        # Valores no limite exato (aceitos)
        self.assertEqual(Calculadora.soma(50, 50), 100)
        self.assertEqual(Calculadora.soma(-50, -50), -100)

    # ========== TESTES UC-02: REALIZAR SUBTRAÇÃO ==========
    
    def test_subtracao_casos_basicos(self):
        """Testa subtração com diferentes combinações - Fluxo Principal"""
        self.assertEqual(Calculadora.subtracao(10, 5), 5)
        self.assertEqual(Calculadora.subtracao(-10, -20), 10)
        self.assertEqual(Calculadora.subtracao(10, -5), 15)
        self.assertEqual(Calculadora.subtracao(0, 5), -5)
    
    def test_subtracao_overflow(self):
        """Testa overflow em ambas direções - Fluxo Alternativo 5b"""
        self.assertEqual(Calculadora.subtracao(150, -50), "Erro: Overflow")
        self.assertEqual(Calculadora.subtracao(-50, 60), "Erro: Overflow")
        # Valores no limite exato (aceitos)
        self.assertEqual(Calculadora.subtracao(150, 50), 100)
        self.assertEqual(Calculadora.subtracao(-50, 50), -100)

    # ========== TESTES UC-03: REALIZAR MULTIPLICAÇÃO ==========
    
    def test_multiplicacao_casos_basicos(self):
        """Testa multiplicação com diferentes combinações - Fluxo Principal"""
        self.assertEqual(Calculadora.multiplicacao(3, 2), 6)
        self.assertEqual(Calculadora.multiplicacao(-3, -2), 6)
        self.assertEqual(Calculadora.multiplicacao(3, -2), -6)
        self.assertEqual(Calculadora.multiplicacao(5, 0), 0)
        self.assertEqual(Calculadora.multiplicacao(5, 1), 5)
    
    def test_multiplicacao_overflow(self):
        """Testa overflow em ambas direções - Fluxo Alternativo 5b"""
        self.assertEqual(Calculadora.multiplicacao(20, 10), "Erro: Overflow")
        self.assertEqual(Calculadora.multiplicacao(-20, 10), "Erro: Overflow")
        # Valores no limite exato (aceitos)
        self.assertEqual(Calculadora.multiplicacao(10, 10), 100)
        self.assertEqual(Calculadora.multiplicacao(-10, 10), -100)

    # ========== TESTES UC-04: REALIZAR DIVISÃO ==========
    
    def test_divisao_casos_basicos(self):
        """Testa divisão com diferentes combinações - Fluxo Principal"""
        self.assertEqual(Calculadora.divisao(10, 2), 5)
        self.assertEqual(Calculadora.divisao(-10, -2), 5)
        self.assertEqual(Calculadora.divisao(10, -2), -5)
        self.assertEqual(Calculadora.divisao(0, 5), 0)
        # Resultado decimal
        self.assertAlmostEqual(Calculadora.divisao(10, 3), 3.333333, places=5)
    
    def test_divisao_por_zero(self):
        """Testa divisão por zero - Fluxo Alternativo 5a"""
        self.assertEqual(Calculadora.divisao(10, 0), "Erro: divisão por zero")
        self.assertEqual(Calculadora.divisao(0, 0), "Erro: divisão por zero")
        self.assertEqual(Calculadora.divisao(-10, 0), "Erro: divisão por zero")
    
    def test_divisao_overflow(self):
        """Testa overflow em ambas direções - Fluxo Alternativo 5b"""
        self.assertEqual(Calculadora.divisao(1000, 5), "Erro: Overflow")
        self.assertEqual(Calculadora.divisao(-1000, 5), "Erro: Overflow")
        # Valores no limite exato (aceitos)
        self.assertEqual(Calculadora.divisao(200, 2), 100)
        self.assertEqual(Calculadora.divisao(-200, 2), -100)


if __name__ == '__main__':
    unittest.main()