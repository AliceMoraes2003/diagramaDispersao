import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

mushroom_data = fetch_ucirepo(id=73)

# print(mushroom_data.data.targets.keys()) # descobrimos que o index a ser usado é o "poisonous"

X = mushroom_data.data.features
y = mushroom_data.data.targets["poisonous"]


# # escolhi forma do chapéu e cor do chapéu para comparação)
# print(X.head())
# print(mushroom_data.variables)


cap_shape = X["cap-shape"]
cap_color = X["cap-color"]


# # Verificando as classes únicas na variável alvo (para diferenciar as cores)
# unique_classes = y.unique()
# print(f"Classes únicas na variável alvo: {unique_classes}") # aqui descobrimos as labels certas para usar! ('p' e 'e')


colors = ["green" if target == "e" else "red" for target in y]

plt.figure(figsize=(8, 6))
plt.scatter(cap_shape, cap_color, c=colors, s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de Dispersão para Mushroom')
plt.xlabel('Forma do Chapéu')
plt.ylabel('Cor do Chapéu')

plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Comestível'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Venenoso')
], loc='upper right')

plt.show()