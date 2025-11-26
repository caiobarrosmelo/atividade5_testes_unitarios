class Calculadora:

    @staticmethod
    def soma(a, b):
        """
        Realiza a soma entre dois números.
        Fluxo principal da UC-01:
        - Usuário informa primeiro número
        - Usuário seleciona operação
        - Usuário informa segundo número
        - Sistema calcula
        Fluxo alternativo 5b:
        - Se o resultado for maior que 100 ou menor que -100,
          o sistema retorna "Erro: Overflow"
        """
        resultado = a + b

        # Fluxo alternativo 5b — limite de resultado: 100
        if abs(resultado) > 100:
            return "Erro: Overflow"

        return resultado

    @staticmethod
    def subtracao(a, b):
        """
        Realiza subtração seguindo o mesmo fluxo principal.
        Aplica o mesmo tratamento de overflow do fluxo alternativo 5b.
        """
        resultado = a - b

        # Fluxo alternativo 5b — overflow
        if abs(resultado) > 100:
            return "Erro: Overflow"

        return resultado

    @staticmethod
    def multiplicacao(a, b):
        """
        Realiza multiplicação conforme o fluxo principal.
        Também verifica overflow conforme o caso alternativo 5b.
        """
        resultado = a * b

        # Fluxo alternativo 5b — overflow
        if abs(resultado) > 100:
            return "Erro: Overflow"

        return resultado

    @staticmethod
    def divisao(a, b):
        """
        Realiza divisão conforme o fluxo principal da UC-01.
        Fluxo alternativo 5a:
        - Se o usuário tentar dividir por zero,
          o sistema retorna "Erro: divisão por zero"
        Fluxo alternativo 5b:
        - Após o cálculo, verifica overflow
        """
        # Fluxo alternativo 5a — divisão por zero
        if b == 0:
            return "Erro: divisão por zero"

        resultado = a / b

        # Fluxo alternativo 5b — overflow
        if abs(resultado) > 100:
            return "Erro: Overflow"

        return resultado
