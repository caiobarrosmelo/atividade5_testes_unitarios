# Sistema Calculadora com Testes Unitários

Sistema de calculadora básica implementado em Python com testes unitários completos utilizando o framework `unittest`.

## Descrição do Projeto

Este projeto implementa uma calculadora que realiza as quatro operações matemáticas básicas (soma, subtração, multiplicação e divisão) com validações de overflow e tratamento de erros.

### Características

- Quatro operações matemáticas básicas
- Validação de overflow (resultados limitados entre -100 e 100)
- Tratamento de divisão por zero
- Testes unitários com cobertura completa
- Implementação baseada em casos de uso documentados

## Estrutura do Projeto

```
projeto-calculadora/
│
├── calculadora.py          # Implementação da classe Calculadora
├── calculadora_test.py     # Testes unitários
├── README.md               # Este arquivo
└── atividade1.ipynb        # Documentação dos casos de uso
```

## Requisitos

- Python 3.6 ou superior
- unittest (incluído na biblioteca padrão do Python)
- coverage (opcional, para análise de cobertura)

### Instalação de Dependências Opcionais

```bash
pip install coverage
pip install unittest-xml-reporting
```

## Como Executar

### Executar a Calculadora

```python
from calculadora import Calculadora

# Exemplos de uso
resultado = Calculadora.soma(5, 3)           # Retorna: 8
resultado = Calculadora.subtracao(10, 4)     # Retorna: 6
resultado = Calculadora.multiplicacao(3, 7)  # Retorna: 21
resultado = Calculadora.divisao(10, 2)       # Retorna: 5.0

# Casos de erro
resultado = Calculadora.soma(60, 50)         # Retorna: "Erro: Overflow"
resultado = Calculadora.divisao(10, 0)       # Retorna: "Erro: divisão por zero"
```

### Executar os Testes

#### Opção 1: Executar todos os testes
```bash
python -m unittest calculadora_test.py
```

#### Opção 2: Executar com modo verbose (detalhado)
```bash
python -m unittest calculadora_test.py -v
```

#### Opção 3: Descoberta automática de testes
```bash
python -m unittest discover -v
```

### Executar com Análise de Cobertura

```bash
# Executar testes com cobertura
python -m coverage run -m unittest calculadora_test.py

# Ver relatório no terminal
python -m coverage report

# Ver relatório detalhado (com linhas não cobertas)
python -m coverage report -m

# Gerar relatório HTML
python -m coverage html
```

Após gerar o relatório HTML, abra o arquivo `htmlcov/index.html` no navegador.

## Casos de Teste

O projeto inclui **12 casos de teste** que cobrem:

### UC-01: Realizar Soma
- Casos básicos (positivos, negativos, mistos, zero)
- Overflow positivo e negativo
- Valores no limite (100 e -100)

### UC-02: Realizar Subtração
- Casos básicos (positivos, negativos, mistos, zero)
- Overflow positivo e negativo
- Valores no limite (100 e -100)

### UC-03: Realizar Multiplicação
- Casos básicos (positivos, negativos, mistos, zero, um)
- Overflow positivo e negativo
- Valores no limite (100 e -100)

### UC-04: Realizar Divisão
- Casos básicos (positivos, negativos, mistos, zero)
- Divisão por zero (erro tratado)
- Resultados decimais
- Overflow positivo e negativo
- Valores no limite (100 e -100)

## Cobertura de Testes

Os testes cobrem **99%** das funcionalidades implementadas, incluindo:

- Todos os fluxos principais de cada caso de uso
- Todos os fluxos alternativos (overflow e divisão por zero)
- Casos de borda e valores limites
- Diferentes combinações de entrada

## Regras de Negócio

### Limitação de Overflow
- Resultados **maiores que 100** ou **menores que -100** retornam `"Erro: Overflow"`
- Valores **exatamente 100 ou -100** são aceitos

### Divisão por Zero
- Qualquer tentativa de divisão por zero retorna `"Erro: divisão por zero"`

### Tipos de Retorno
- Operações bem-sucedidas retornam valores numéricos (`int` ou `float`)
- Operações com erro retornam strings descritivas do erro

## Exemplos de Uso dos Testes

```python
# Executar um teste específico
python -m unittest calculadora_test.TestCalculadora.test_soma_casos_basicos

# Executar todos os testes de uma operação
python -m unittest calculadora_test.TestCalculadora.test_soma_*
```

## Documentação Adicional

Para mais detalhes sobre os casos de uso e especificações, consulte o arquivo `casos_uso.md`.

## Desenvolvimento

### Adicionar Novos Testes

1. Abra o arquivo `calculadora_test.py`
2. Adicione um novo método de teste na classe `TestCalculadora`
3. Use o padrão de nomenclatura: `test_<operacao>_<cenario>`
4. Execute os testes para validar

Exemplo:
```python
def test_soma_novo_cenario(self):
    """Descrição do novo cenário"""
    self.assertEqual(Calculadora.soma(x, y), resultado_esperado)
```

### Boas Práticas Implementadas

- Métodos estáticos para operações sem estado
- Docstrings descritivas em todos os métodos
- Separação clara entre lógica de negócio e testes
- Nomenclatura clara e consistente
- Testes organizados por caso de uso

## Licença

Este projeto foi desenvolvido para fins educacionais.

## Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

**Desenvolvido usando Python e TDD (Test-Driven Development)**