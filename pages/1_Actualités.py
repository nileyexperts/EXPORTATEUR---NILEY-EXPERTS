import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Actualités", page_icon="📰")
st.header("📰 Actualités")
st.caption("Liste et catégorisation de vos contenus éditoriaux.")

articles_path = Path('data/articles.json')
if articles_path.exists():
    try:
        articles = json.loads(articles_path.read_text(encoding='utf-8'))
    except Exception as e:
        st.error(f"Erreur de lecture: {e}")
        st.stop()

    # Catégories
    categories = sorted({a.get('category','Divers') for a in articles})
    cat = st.selectbox("Filtrer par catégorie", options=["Toutes"] + categories)
    if cat != "Toutes":
        articles = [a for a in articles if a.get('category','Divers') == cat]

    for a in articles:
        with st.expander(a.get('title','(sans titre)'), expanded=False):
            st.write(a.get('summary','(pas de résumé)'))
            if a.get('url'):
                st.link_button("Lire", a['url'])
else:
    st.info("Ajoutez **data/articles.json** (format: liste de dictionnaires avec `title`, `date`, `category`, `summary`, `url`, `image`).")
