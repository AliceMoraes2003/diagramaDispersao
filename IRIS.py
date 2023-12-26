from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def map_target_array(iris_class):
    if iris_class == "Iris-setosa":
        return 0
    elif iris_class == "Iris-virginica":
        return 1
    else:
        return -1

iris = fetch_ucirepo(id=53)
# print(iris)

sepal_length = iris.data.features["sepal length"]
sepal_width = iris.data.features["sepal width"]
targets = iris.data.targets["class"]

numbered_targets = list(map(map_target_array, targets))

valid_indices = [i for i, target in enumerate(numbered_targets) if target != -1]
sepal_length = [sepal_length[i] for i in valid_indices]
sepal_width = [sepal_width[i] for i in valid_indices]
numbered_targets = [target for target in numbered_targets if target != -1]

colors = ["r", "g"]

# Criando o gráfico de dispersão 2D
plt.figure(figsize=(8, 6))
plt.scatter(sepal_length, sepal_width, c=[colors[i] for i in numbered_targets], s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de dispersão da Iris')
plt.xlabel('Comprimento da Sépala')
plt.ylabel('Largura da Sépala')

# Adicionando a legenda
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=species)
    for species, color in zip(["setosa", "virginica"], colors)
]
plt.legend(handles=legend_elements, loc='upper left')

plt.show()