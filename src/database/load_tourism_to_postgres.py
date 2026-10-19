
from pathlib import Path
import os

import pandas as pd
import psycopg

# 1. Trouver le dossier du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "tourism_nights_by_destination.csv"
)

# 2. Lire et transformer le CSV
df = pd.read_csv(CSV_PATH, sep=";")
df = df.rename(columns={"provinces": "destination"})

df_long = df.melt(
    id_vars=["destination"],
    var_name="year",
    value_name="nights",
)

df_long["year"] = df_long["year"].astype(int)

df_long["nights"] = (
    df_long["nights"]
    .astype(str)
    .str.replace(" ", "", regex=False)
    .astype("int64")
)

# 3. Lire les paramètres de connexion
# Valeurs par défaut pour notre installation locale
db_name = os.getenv("PGDATABASE", "morocco_tourism_dw")
db_user = os.getenv("PGUSER", "postgres")
db_host = os.getenv("PGHOST", "localhost")
db_port = os.getenv("PGPORT", "5432")
db_password = os.getenv("PGPASSWORD")

if not db_password:
    raise RuntimeError(
        "Le mot de passe PostgreSQL n'est pas défini. "
        "Définissez la variable d'environnement PGPASSWORD "
        "avant de lancer le script."
    )

# 4. Insérer les données dans PostgreSQL
rows = list(
    df_long[["destination", "year", "nights"]]
    .itertuples(index=False, name=None)
)

with psycopg.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port,
) as conn:
    with conn.cursor() as cur:
       cur.executemany(
            """
            INSERT INTO tourism_nights (destination, year, nights)
            VALUES (%s, %s, %s)
            ON CONFLICT (destination, year)
            DO UPDATE SET nights = EXCLUDED.nights
            """,
            rows,
        )

print(f"Chargement terminé : {len(rows)} lignes insérées.")