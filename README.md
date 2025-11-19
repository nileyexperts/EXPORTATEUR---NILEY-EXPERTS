# Démonstrateur Streamlit (style "L'Exportateur")

> ⚠️ **Important** : Ce projet n'est **pas** une copie du site [lexportateur.com](https://www.lexportateur.com/) et n'en reprend aucun contenu. Il fournit un **squelette** de fonctionnalités et d'organisation pour construire un site d'actualités/professionnel similaire sur vos **propres textes, images et données**.

## Structure du projet

```
lexportateur_like_streamlit/
├── app.py
├── pages/
│   ├── 1_Actualités.py
│   ├── 2_Guides.py
│   ├── 3_Outils.py
│   └── 4_Contact.py
├── data/
│   ├── articles.json        # (optionnel) vos articles au format JSON
│   └── guides.md            # (optionnel) vos guides en Markdown
├── assets/
│   └── logo.png             # (optionnel) votre logo
├── .streamlit/
│   └── config.toml          # thème et mise en page
├── requirements.txt
└── README.md
```

## Lancer en local

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Déployer

1. Créez un dépôt GitHub et poussez ce dossier.
2. Ouvrez [Streamlit Community Cloud](https://share.streamlit.io/) et connectez votre dépôt.
3. Choisissez `app.py` comme entrée et validez.

## Ajouter vos contenus

- Placez vos articles dans `data/articles.json` (voir format dans le code).
- Écrivez vos guides dans `data/guides.md`.
- Ajoutez `assets/logo.png`.

## Respect du droit d'auteur

N'intégrez aucun texte, image ou structure protégée provenant de sites tiers sans autorisation. Vérifiez les **Conditions d'utilisation**, le **robots.txt**, ou obtenez un **accord écrit**.
