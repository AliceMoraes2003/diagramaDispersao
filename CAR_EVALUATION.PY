import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

car_evaluation = fetch_ucirepo(id=19)

# print(car_evaluation.data.targets.keys()) # descobrimos que o index a ser usado é o "class"

X = car_evaluation.data.features
y = car_evaluation.data.targets["class"]


# escolhi compra e segurança para comparação)
# print(X.head())
# print(car_evaluation.variables)


buying = X["buying"]
safety = X["safety"]


# Verificando as classes únicas na variável alvo (para diferenciar as cores)
# unique_classes = y.unique()
# print(f"Classes únicas na variável alvo: {unique_classes}") # aqui descobrimos as labels certas para usar!  ['unacc' 'acc' 'vgood' 'good']


# Mapeando as classes para as cores
mapped_colors = ["blue" if target == "unacc" else
                 "green" if target == "acc" else
                 "orange" if target == "good" else
                 "red" for target in y]

# Criando o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(buying, safety, c=mapped_colors, s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de Dispersão para Car Evaluation')
plt.xlabel('Compra')
plt.ylabel('Segurança')

# Adicionando legendas
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='unacc'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='acc'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='good'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='vgood')
], loc='upper right')

plt.show()