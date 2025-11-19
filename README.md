# Démonstrateur Streamlit — Fiches Pays (v5)

Cette version inclut :
- 175 entrées pays (avec indicateurs publics **simulés** pour démonstration),
- Drapeaux via flagcdn.com, coordonnées (lat/lon),
- Carte interactive (pydeck),
- Export PDF des fiches (ReportLab),
- Recherche + filtres par continent.

> Remplacez les *placeholders* par des données réelles issues de sources publiques (Banque mondiale, FMI, OMC) si nécessaire.

## Lancement local
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Déploiement Streamlit Cloud
1) Poussez ce dossier sur GitHub  
2) Créez une app sur https://share.streamlit.io  
3) Fichier principal: `app.py`
