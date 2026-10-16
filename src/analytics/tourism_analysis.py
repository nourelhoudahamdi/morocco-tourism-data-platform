import pandas as pd

# Lire les données nettoyées
input_file = "data/processed/tourism_nights_clean.csv"

df = pd.read_csv(input_file)

# Afficher les données
print("Données touristiques nettoyées :")
print(df.head())

# Afficher les types de données
print("\nTypes de données :")
print(df.dtypes)

# Trouver la destination avec le plus de nuitées en 2019
top_destination = df.loc[df["2019"].idxmax()]

print("\nDestination avec le plus de nuitées en 2019 :")
print(top_destination["provinces"])

print("\nNombre de nuitées :")
print(top_destination["2019"])

# Comparer les nuitées de 2019 et 2020
df["variation_nuitees"] = df["2020"] - df["2019"]

print("\nVariation des nuitées entre 2019 et 2020 :")
print(df[["provinces", "2019", "2020", "variation_nuitees"]])

# Calculer le pourcentage de variation entre 2019 et 2020
df["variation_pourcentage"] = (
    (df["2020"] - df["2019"]) / df["2019"]
) * 100

# Afficher les résultats
print("\nPourcentage de variation des nuitées entre 2019 et 2020 :")

print(
    df[
        [
            "provinces",
            "2019",
            "2020",
            "variation_nuitees",
            "variation_pourcentage",
        ]
    ].round(2)
)

# Identifier la destination ayant connu la plus forte baisse en pourcentage
worst_destination = df.loc[df["variation_pourcentage"].idxmin()]

print("\nDestination ayant connu la plus forte baisse en pourcentage :")
print(worst_destination["provinces"])

print("\nPourcentage de variation :")
print(f'{worst_destination["variation_pourcentage"]:.2f}%')

# Sauvegarder les résultats de l'analyse

output_file = "data/processed/tourism_analysis_results.csv"

df.to_csv(output_file, index=False)

print("\nLes résultats de l'analyse ont été enregistrés dans :")
print(output_file)