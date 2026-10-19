from pathlib import Path
import logging
import pandas as pd

# Racine du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Dossier des logs
logs_dir = PROJECT_ROOT / "logs"
logs_dir.mkdir(parents=True, exist_ok=True)

# Configuration du logging
logging.basicConfig(
    filename=logs_dir / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

logger.info("Début de l'ingestion des données touristiques")


# Chemin du fichier CSV
input_file = PROJECT_ROOT / "data" / "raw" / "tourism_nights_by_destination.csv"

# Dossier de sortie
output_dir = PROJECT_ROOT / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "tourism_nights_clean.csv"

# Lire les données touristiques
df = pd.read_csv(input_file, sep=";")

# Nettoyer les colonnes des années et convertir les valeurs en nombres
year_columns = df.columns.drop("provinces")

for column in year_columns:
    df[column] = (
        df[column]
        .str.replace(" ", "", regex=False)
        .astype(int)
    )

# Afficher les premières lignes
print("Premières lignes du dataset :")
print(df.head())

# Afficher les colonnes
print("\nColonnes du dataset :")
print(df.columns.tolist())

# Afficher le nombre de lignes et de colonnes
print("\nDimensions du dataset :")
print(df.shape)

# Vérifier les valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())

# Vérifier les types de données
print("\nTypes de données :")
print(df.dtypes)

print("\nTypes de données après transformation :")
print(df.dtypes)

print("\nAperçu des données transformées :")
print(df.head())

# Enregistrer les données nettoyées

df.to_csv(output_file, index=False)

print(f"\nDonnées nettoyées enregistrées dans : {output_file}")
logger.info("Données nettoyées enregistrées avec succès.")

# ==========================================
# PHASE 4 : CONTROLE DE LA QUALITE DES DONNEES
# ==========================================

print("\n========== CONTROLE QUALITE ==========")

# 1. Nombre de valeurs manquantes
print("\n1. Valeurs manquantes :")
print(df.isnull().sum())

# 2. Nombre de lignes dupliquees
print("\n2. Lignes dupliquees :")
print(df.duplicated().sum())

# 3. Destinations presentes plusieurs fois
print("\n3. Destinations dupliquees :")
print(df[df["provinces"].duplicated(keep=False)])

# 4. Recherche de valeurs negatives
print("\n4. Valeurs negatives :")
year_columns = df.columns.drop("provinces")

negative_values = df[year_columns].lt(0).any(axis=1)

print(df.loc[negative_values])

# 5. Verification des types
print("\n5. Types de donnees :")
print(df.dtypes)

# 6. Verification des noms des destinations
print("\n6. Verification des noms des destinations :")

print("Noms des destinations :")
print(df["provinces"].tolist())

# Detecter les espaces au debut ou a la fin
spaces = df["provinces"].str.strip().ne(df["provinces"])

print("\nNoms contenant des espaces inutiles :")
print(df.loc[spaces, "provinces"])

# 7. Verification des noms vides
print("\n7. Verification des noms vides :")

empty_names = df["provinces"].isna() | df["provinces"].str.strip().eq("")

print("Nombre de noms vides :", empty_names.sum())

if empty_names.any():
    print(df.loc[empty_names])
else:
    print("Aucun nom de destination vide.")

# 8. Verification de la structure du dataset
print("\n8. Verification de la structure du dataset :")

expected_years = [str(year) for year in range(2012, 2021)]

actual_years = [
    column for column in df.columns
    if column != "provinces"
]

print("Nombre de destinations :", len(df))
print("Nombre de colonnes :", len(df.columns))
print("Annees attendues :", expected_years)
print("Annees presentes :", actual_years)

if len(df) == 12 and actual_years == expected_years:
    print("Structure du dataset validee.")
else:
    print("Attention : verifier la structure du dataset.")