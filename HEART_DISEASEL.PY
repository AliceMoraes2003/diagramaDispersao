# ATENÇÃO, ESSE CÓDIGO TEM DOIS GRÁFICOS! UM SEX X AGE E OUTRO CHOL X TRESTBPS! 
# COMENTE UM BLOCO DE CÓDIGO ANTES OU DEPOIS DO SEPRADOR PARA VISUALIZAR UM DOS DOIS POR VEZ

#importação de dados
from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import ssl

# Desativando temporariamente a verificação de certificado SSL (links que o prof seu se expiraram e eu não o porquê)
ssl._create_default_https_context = ssl._create_unverified_context

# Fetch do dataset
heart_disease = fetch_ucirepo(id=45)

# Dados
X = heart_disease.data.features
y = heart_disease.data.targets



# # Imprimindo o DataFrame X
# print(X.head())

# # Verificando as variáveis disponíveis para usar no exemplo (escolhi idade e sexo e depois o nível de colesterol junto da pressão arterial para comparação)
# print(heart_disease.variables)



# Selecionando as variáveis 'age' e 'sex'
age = X["age"]
sex = X["sex"]

# Mapeando o sexo para cores
colors = {0: 'blue', 1: 'pink'}  # 0 para masculino, 1 para feminino

# Criando o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(age, sex, c=[colors[gender] for gender in sex], s=50, alpha=0.8, edgecolors='w')
plt.title('Diagrama de dispersão -HEAT DISEASEL')
plt.xlabel('Idade')
plt.ylabel('Sexo')
plt.xticks(rotation=45)

# Adicionando a legenda
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=gender)
    for gender, color in colors.items()
]
plt.legend(handles=legend_elements, title='Sexo', loc='upper right')

#imprimindo o gráfico
plt.show()




#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




# #importação de dados
# import matplotlib.pyplot as plt
# from ucimlrepo import fetch_ucirepo
# import ssl

# # Desativando temporariamente a verificação de certificado SSL (links que o prof seu se expiraram e eu não o porquê)
# ssl._create_default_https_context = ssl._create_unverified_context

# # Fetch dataset
# heart_disease = fetch_ucirepo(id=45)




# # # para descobri que chave eu posso colocar no targets ali embaixo (descobri que é num)
# # print(heart_disease.data.targets.keys())




# # Data
# X = heart_disease.data.features
# y = heart_disease.data.targets["num"]




# # # Verificando as classes únicas na variável alvo (para diferenciar as cores coloco essa informação na linha 89 em target ==)
# # unique_classes = y.unique()
# # print(f"Classes únicas na variável alvo: {unique_classes}")




# # Selecionando as variáveis 'chol' e 'trestbps'
# chol = X["chol"]
# trestbps = X["trestbps"]

# # Criando uma lista de cores
# colors = ["blue" if target == 0 else "green" for target in y]

# # Criando o gráfico de dispersão
# plt.figure(figsize=(8, 6))
# plt.scatter(chol, trestbps, c=colors, s=50, alpha=0.8, edgecolors='w')
# plt.title('Diagrama de Dispersão para Heart Disease')
# plt.xlabel('Colesterol (chol)')
# plt.ylabel('Pressão Arterial em Repouso (trestbps)')

# # Adicionando legendas
# plt.legend(handles=[
#     plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='Sem Doença Cardíaca'),
#     plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Com Doença Cardíaca')
# ], loc='upper right')

# #imprimindo o gráfico
# plt.show()