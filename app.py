import json
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="L'Exportateur — Démonstrateur",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# En-tête
col1, col2 = st.columns([1, 8])
with col1:
    logo_path = Path('assets/logo.png')
    if logo_path.exists():
        st.image(str(logo_path), use_column_width=True)
    else:
        st.markdown("**L'Exportateur (démo)**")
with col2:
    st.title("Plateforme d'actualités & ressources — Démonstrateur")
    st.caption("Ce site de démonstration est un squelette Streamlit. Remplacez les contenus par les vôtres.")

st.divider()

# Zone de recherche d'articles (facultatif)
search_query = st.text_input("🔎 Rechercher dans les articles (si vous en avez ajouté)", placeholder="mots-clés…")

articles_path = Path('data/articles.json')
articles = []
if articles_path.exists():
    try:
        articles = json.loads(articles_path.read_text(encoding='utf-8'))
    except Exception as e:
        st.error(f"Impossible de lire data/articles.json : {e}")

if articles:
    # Filtrage
    if search_query:
        q = search_query.lower()
        filtered = [a for a in articles if q in a.get('title','').lower() or q in a.get('summary','').lower()]
    else:
        filtered = articles

    st.subheader(f"Articles ({len(filtered)})")
    for a in filtered:
        with st.container():
            st.markdown(f"### {a.get('title','(sans titre)')}")
            meta = []
            if a.get('date'): meta.append(a['date'])
            if a.get('category'): meta.append(a['category'])
            if meta:
                st.caption(" • ".join(meta))
            if a.get('image'):
                st.image(a['image'], use_column_width=True)
            st.markdown(a.get('summary', ''))
            if a.get('url'):
                st.link_button("Lire l'article", a['url'])
            st.divider()
else:
    st.info("Aucun article n'a été trouvé. Ajoutez un fichier **data/articles.json** pour alimenter la page d'accueil.")

st.success("Astuce : utilisez le menu à gauche pour accéder aux autres pages (Guides, Outils, Contact).")
