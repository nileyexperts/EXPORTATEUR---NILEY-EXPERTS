import streamlit as st
from pathlib import Path
from lib.ui import inject_css

st.set_page_config(page_title="Plateforme — Démonstrateur", page_icon="📦", layout="wide")

i
nject_css()

st.title("Plateforme d'actualités & ressources — Démonstrateur (v5)")
st.caption("Utilisez le menu à gauche pour accéder aux fiches pays.")

st.success("Page dédiée: **Fiches Pays** (avec carte interactive & export PDF)")
