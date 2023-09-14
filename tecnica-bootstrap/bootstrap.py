import numpy as np

#Setando a seed de onde serão retirado os dados pseudoaleatórios
np.random.seed(0) 

# Número de amostras de bootstrap a serem geradas
numero_amostras_bootstrap = 1000

# Média de 170 cm, desvio padrão de 5cm, 100 observações
# numpy.random.normal() => Geração de números aleatórios a partir de uma distribuição normal
altura_populacao = np.random.normal(170, 5, numero_amostras_bootstrap)  

# Função para calcular a média de uma amostra de bootstrap
def bootstrap(amostra):
    return np.mean(amostra)

# Gerar amostras de bootstrap
bootstrap_amostras = []
for _ in range(numero_amostras_bootstrap):
    #numpy.random.choice() 
    #Permite gerar amostras aleatórias a partir de um array ou de uma sequência de elementos
    amostra = np.random.choice(altura_populacao, size=len(altura_populacao))
    bootstrap_amostras.append(amostra)

# Calcular as médias das amostras de bootstrap
medias_bootstrap = []
for amostra in bootstrap_amostras:
    media = bootstrap(amostra)
    medias_bootstrap.append(media)
    
# Definindo os intervalos inferior e superior 
# numpy.percentile --> Calcular os percentis de um conjunto de dados
limite_inferior = np.percentile(medias_bootstrap, 2.5)
limite_superior = np.percentile(medias_bootstrap, 97.5)

print(f"Intervalo de Confiança de 95% para a Média de Altura: ({limite_inferior:.2f} cm, {limite_superior:.2f} cm)")
