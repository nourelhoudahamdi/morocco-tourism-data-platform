-- 1. Vérifier le nombre total de lignes
SELECT COUNT(*) AS total_lignes
FROM tourism_nights;


-- 2. Trouver les 5 destinations les plus visitées en 2019
SELECT
    destination,
    nights
FROM tourism_nights
WHERE year = 2019
ORDER BY nights DESC
LIMIT 5;

-- 3. Évolution des nuitées touristiques par année

SELECT
    year,
    SUM(nights) AS total_nuitees
FROM tourism_nights
GROUP BY year
ORDER BY year;

-- 4. Variation annuelle des nuitées touristiques

WITH yearly_totals AS (
    SELECT
        year,
        SUM(nights) AS total_nuitees
    FROM tourism_nights
    GROUP BY year
)
SELECT
    year,
    total_nuitees,
    LAG(total_nuitees) OVER (ORDER BY year) AS nuitees_annee_precedente,
    ROUND(
        100.0 * (
            total_nuitees - LAG(total_nuitees) OVER (ORDER BY year)
        ) / NULLIF(
            LAG(total_nuitees) OVER (ORDER BY year), 0
        ),
        2
    ) AS variation_percent
FROM yearly_totals
ORDER BY year;

-- 5. Part de chaque destination dans les nuitées de 2019

SELECT
    destination,
    nights,
    ROUND(
        100.0 * nights / SUM(nights) OVER (),
        2
    ) AS part_percent
FROM tourism_nights
WHERE year = 2019
ORDER BY nights DESC;

-- 6. Vue : résumé annuel des nuitées touristiques

CREATE OR REPLACE VIEW tourism_yearly_summary AS
SELECT
    year,
    SUM(nights) AS total_nuitees,
    COUNT(DISTINCT destination) AS nombre_destinations
FROM tourism_nights
GROUP BY year;


-- 7. Vue : comparaison des nuitées entre 2019 et 2020

CREATE OR REPLACE VIEW tourism_destination_summary AS
SELECT
    destination,
    SUM(nights) FILTER (WHERE year = 2019) AS nights_2019,
    SUM(nights) FILTER (WHERE year = 2020) AS nights_2020,
    ROUND(
        100.0 * (
            SUM(nights) FILTER (WHERE year = 2020)
            - SUM(nights) FILTER (WHERE year = 2019)
        )
        / NULLIF(
            SUM(nights) FILTER (WHERE year = 2019),
            0
        ),
        2
    ) AS variation_percent
FROM tourism_nights
WHERE year IN (2019, 2020)
GROUP BY destination;