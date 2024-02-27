# Geocode.py

## Description

Ce script geocode un csv avec nominatim. Il prend 3 arguements entrén un csv, le champs contenant la ville et celui contenant le pays.

## Utilisation

Environnement virtuel et installation des dépendences

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r _tools/requirements.txt
```

```bash
python3 geocode.py --input ../tennis/atp_men_2024.csv --city ville --country pays
```

Le résultat est dans un fichier au même endroit que l'input file mais qui se termine par `_geocode.csv`