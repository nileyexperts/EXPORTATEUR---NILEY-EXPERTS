import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Guides", page_icon="📚")
st.header("📚 Guides pratiques")
st.caption("Publiez des tutoriels et fiches pratiques en Markdown.")

md_path = Path('data/guides.md')
if md_path.exists():
    st.markdown(md_path.read_text(encoding='utf-8'))
else:
    st.info("Créez un fichier **data/guides.md** et rédigez vos contenus en Markdown.")
