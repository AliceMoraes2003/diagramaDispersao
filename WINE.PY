from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

wine = fetch_ucirepo(id=109)
# print(wine)

ash = wine.data.features["Ash"]
alchohol = wine.data.features["Alcohol"]

plt.figure(figsize=(8, 6))
plt.scatter(ash, alchohol, c=range(len(ash)), cmap='inferno')
plt.xlabel("Ash")
plt.ylabel("Alcohol")
plt.title("Diagrama de dispersão Wine")

plt.colorbar(label='Pontos')
plt.show()