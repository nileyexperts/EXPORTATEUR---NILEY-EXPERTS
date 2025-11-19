# Démonstrateur Streamlit — Fiches Pays avec Carte Interactive

Ce projet inclut :
- Liste des pays avec drapeaux et coordonnées géographiques
- Recherche, filtres par continent
- Carte interactive (pydeck)

## Structure
```
lexportateur_like_streamlit_v4/
├── app.py
├── pages/
│   ├── 1_Actualités.py
│   ├── 2_Guides.py
│   ├── 3_Outils.py
│   ├── 4_Contact.py
│   └── 5_Pays.py
├── data/
│   └── pays.json
├── assets/
│   └── styles.css
├── lib/
│   └── ui.py
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── README.md
```

## Lancer en local
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
