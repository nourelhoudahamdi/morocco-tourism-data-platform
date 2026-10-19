from pathlib import Path
import subprocess
import sys
import logging

# Racine du projet
PROJECT_ROOT = Path(__file__).resolve().parent

# Python utilisé par l'environnement virtuel
PYTHON = sys.executable

# Dossier des logs
LOGS_DIR = PROJECT_ROOT / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Configuration du logging
logging.basicConfig(
    filename=LOGS_DIR / "pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

logger.info("Début du pipeline touristique")

print("=" * 50)
print("MOROCCO TOURISM DATA PIPELINE")
print("=" * 50)

print(f"Racine du projet : {PROJECT_ROOT}")
print(f"Python utilisé : {PYTHON}")

# ==========================================
# ETAPE 1 : INGESTION DES DONNEES
# ==========================================

print("\n[1/4] Lancement de l'ingestion des données...")

result = subprocess.run(
    [PYTHON, str(PROJECT_ROOT / "src" / "ingestion" / "ingest_tourism_data.py")],
    cwd=PROJECT_ROOT,
    check=False
)

if result.returncode == 0:
    print("\nSUCCES : Ingestion terminée.")
    logger.info("Ingestion terminée avec succès.")
else:
    print("\nERREUR : L'ingestion a échoué.")
    logger.error("Échec de l'ingestion des données.")
    sys.exit(1)

# ==========================================
# ETAPE 2 : CHARGEMENT DANS POSTGRESQL
# ==========================================

print("\n[2/4] Chargement des données dans PostgreSQL...")

result = subprocess.run(
    [
        PYTHON,
        str(PROJECT_ROOT / "src" / "database" / "load_tourism_to_postgres.py")
    ],
    cwd=PROJECT_ROOT,
    check=False
)

if result.returncode == 0:
    print("\nSUCCES : Chargement PostgreSQL terminé.")
    logger.info("Chargement PostgreSQL terminé avec succès.")
else:
    print("\nERREUR : Le chargement PostgreSQL a échoué.")
    logger.error("Échec du chargement des données dans PostgreSQL.")
    sys.exit(1)

# ==========================================

# ETAPE 3 : ANALYSE DES DONNEES

# ==========================================

print("\n[3/4] Lancement de l'analyse des données...")

result = subprocess.run(
[
PYTHON,
str(PROJECT_ROOT / "src" / "analytics" / "tourism_analysis.py")
],
cwd=PROJECT_ROOT,
check=False
)

if result.returncode == 0:
    print("\nSUCCES : Analyse des données terminée.")
    logger.info("Analyse des données terminée avec succès.")
    logger.info("Pipeline terminé avec succès.")
else:
    print("\nERREUR : L'analyse des données a échoué.")
    logger.error("Échec de l'analyse des données.")
    sys.exit(1)

# ==========================================

# ETAPE 4 : VISUALISATION DES DONNEES

# ==========================================

print("\n[4/4] Création du graphique touristique...")

result = subprocess.run(
[
PYTHON,
str(PROJECT_ROOT / "src" / "analytics" / "tourism_visualization.py")
],
cwd=PROJECT_ROOT,
check=False
)

if result.returncode == 0:
    print("\nSUCCES : Graphique touristique créé.")
    logger.info("Visualisation des données terminée avec succès.")

    print("\n" + "=" * 50)
    print("SUCCES : PIPELINE TERMINE AVEC SUCCES !")
    print("=" * 50)

    logger.info("Pipeline terminé avec succès.")
else:
    print("\nERREUR : La création du graphique a échoué.")
    logger.error("Échec de la visualisation des données.")
    sys.exit(1)
if result.returncode == 0:
    print("\nSUCCES : Graphique touristique créé.")
    logger.info("Visualisation des données terminée avec succès.")

    print("\n" + "=" * 50)
    