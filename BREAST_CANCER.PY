import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Fetch dataset
breast_cancer = fetch_ucirepo(id=17)


# # para descobri que chave targets que eu posso colocar ali embaixo (descobri que é "Diagnosis")
# print(breast_cancer.data.targets.keys())


# Data
X = breast_cancer.data.features
y = breast_cancer.data.targets["Diagnosis"]



# # Imprimindo o DataFrame X
# print(X.head())

# # Verificando as variáveis disponíveis para usar no exemplo (escolhi rádio e a textura para comparação)
# print(breast_cancer.variables)


# Escolha das variáveis
radius1 = X["radius1"]
texture1 = X["texture1"]


# Verificando as classes únicas na variável alvo (para diferenciar as cores coloco essa informação na linha 89 em target ==)
# unique_classes = y.unique()
# print(f"Classes únicas na variável alvo: {unique_classes}")


# Mapeando as classes para as cores
colors = ["blue" if target == "B" else "red" for target in y]

# Criando o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(radius1, texture1, c=colors, s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de Dispersão para Breast Cancer')
plt.xlabel('Raio Médio')
plt.ylabel('Textura Média')

# Adicionando legendas
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Benigno'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Maligno')
], loc='upper right')

plt.show()