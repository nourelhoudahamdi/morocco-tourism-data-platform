import pandas as pd
import matplotlib.pyplot as plt

# 1. Lire les données nettoyées
input_file = "data/processed/tourism_nights_clean.csv"
df = pd.read_csv(input_file)

# 2. Trier les destinations selon les nuitées de 2019
df = df.sort_values(by="2019", ascending=False)

# 3. Préparer le graphique
df.plot(
    x="provinces",
    y=["2019", "2020"],
    kind="bar",
    figsize=(12, 6)
)

# 4. Ajouter le titre et les noms des axes
plt.title("Comparaison des nuitées touristiques : 2019 vs 2020")
plt.xlabel("Destination")
plt.ylabel("Nombre de nuitées")

# 5. Améliorer la lisibilité
plt.xticks(rotation=45, ha="right")
plt.legend(title="Année")
plt.tight_layout()

# Sauvegarder le graphique
output_file = "data/processed/comparison_2019_2020.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Graphique enregistré dans : {output_file}")

# Afficher le graphique
plt.show()