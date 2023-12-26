import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# dataset
zoo_data = fetch_ucirepo(id=111)

# print(zoo_data.data.targets.keys()) # descobrimos que o index a ser usado é o "type"

# dataframe
X = zoo_data.data.features
y = zoo_data.data.targets["type"]

# print(y.value_counts())

# escolhi hair e feathers para comparação)
# print(X.head())
# print(zoo_data.variables)

# escolhas de variáveis
hair = X["hair"]
feathers = X["feathers"]

# unique_classes = y.unique()
# print(f"Classes únicas na variável alvo: {unique_classes}") # aqui descobrimos as labels certas para usar!  [1 4 2 7 6 5 3]

colors = [
    "blue" if target == 1 else
    "green" if target == 2 else
    "red" if target == 4 else
    "purple" if target == 7 else
    "orange" if target == 6 else
    "brown" if target == 3 else
    "pink" for target in y
]

# Criando o gráfico 
plt.figure(figsize=(8, 6))
plt.scatter(hair, feathers, c=colors, s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de Dispersão para Zoo')
plt.xlabel('Pelos')
plt.ylabel('Penas')

# legendas
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='1'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='2'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='4'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='purple', markersize=10, label='7'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='6'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='brown', markersize=10, label='3'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='pink', markersize=10, label='5')
], loc='upper right')

plt.show()