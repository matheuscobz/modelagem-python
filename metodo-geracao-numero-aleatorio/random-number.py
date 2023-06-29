import time

# Inicializando a classe
class LinearCongruentialGenerator:
    # Armazenando o estado atual do gerador com os parâmetros
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    # Gerador de números pseudoaleatórios usando o LCG e retorna o valor da seed
    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

# Parâmetros do gerador
a = 1103515245
c = 12345
m = 2**32

# Obtendo o tempo atual em segundos como seed inicial
seed = int(time.time())

# Criando uma instância do gerador
lcg = LinearCongruentialGenerator(seed, a, c, m)

# Solicitando o valor de escala ao usuário
valor_escala = float(input("Digite o valor de escala: "))

# Limitando os valores números para serem gerados de 0 a 10 somente
for _ in range(10):
    numero_aleatorio = lcg.generate()

    # Mapeamento e escala para o intervalo [0, valor_escala]
    numero_convertido = (numero_aleatorio % (m-1)) / (m-1) * valor_escala

    # Printando o valor com algumas casas decimais
    print(round(numero_convertido, 8))
