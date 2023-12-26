#esse eu não consegui diferenciar os pontos...

import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# dataset
spambase_data = fetch_ucirepo(id=94)

# print(spambase_data.data.targets.keys()) # descobrimos que o index a ser usado é o "Class"

# dataframe
X = spambase_data.data.features
y = spambase_data.data.targets["Class"]

# escolhi word_freq_make e word_freq_address para comparação)
# print(X.head())
# print(spambase_data.variables)

# escolhas de variáveis
word_freq_make = X["word_freq_make"]
word_freq_address = X["word_freq_address"]

# unique_classes = y.unique()
# print(f"Classes únicas na variável alvo: {unique_classes}") # aqui descobrimos as labels certas para usar! ('1' e '0')

# mapeando cores
colors = ["blue" if target == "1" else "red" for target in y]

# crianção do gráfico
plt.figure(figsize=(8, 6))
plt.scatter(word_freq_make, word_freq_address, c=colors, s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de Dispersão para Spambase')
plt.xlabel('"make"')
plt.ylabel('"address"')

# legenda
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Não Spam'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Spam')
], loc='upper right')

plt.show()