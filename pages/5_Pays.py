import streamlit as st
import pydeck as pdk
from lib.ui import load_json, inject_css, render_country_cards, build_country_pdf_bytes

st.set_page_config(page_title="Fiches Pays", page_icon="🌍", layout="wide")
inject_css()

st.header("🌍 Fiches Pays — Carte interactive + Export PDF")
st.caption("Recherche, filtres par continent, drapeaux, indicateurs (démonstration), export PDF.")

countries = load_json('data/pays.json')

col1, col2 = st.columns([2,2])
with col1:
    search = st.text_input("🔎 Rechercher un pays", placeholder="Nom du pays…")
with col2:
    continents = sorted({c.get('continent') for c in countries})
    selected_cont = st.selectbox("Filtrer par continent", options=["Tous"] + continents)

filtered = countries
if search:
    q = search.lower()
    filtered = [c for c in filtered if q in c.get('name','').lower()]
if selected_cont != "Tous":
    filtered = [c for c in filtered if c.get('continent') == selected_cont]

# Carte interactive
if filtered:
    st.subheader("🗺️ Carte interactive")
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=filtered,
        get_position='[lon, lat]',
        get_radius=350000,
        get_fill_color='[13,92,99,160]',
        pickable=True
    )
    view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1.2)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"}))

st.subheader("📋 Liste des pays")
# Bouton d'export PDF global (zip non implémenté côté UI, PDF à l'unité)
cols = st.columns(3)
render_country_cards(filtered)

# Export PDF unitaire
st.divider()
st.info("Sélectionnez un pays pour exporter sa fiche en PDF :")
names = [c.get('name') for c in filtered]
sel = st.selectbox("Choisir le pays", options=names if names else [""])
if sel:
    payload = next((c for c in filtered if c.get('name') == sel), None)
    if payload:
        buf = build_country_pdf_bytes(payload)
        st.download_button(
            label=f"📄 Exporter la fiche PDF — {payload.get('name')}",
            data=buf,
            file_name=f"fiche_{payload.get('iso','XX')}.pdf",
            mime='application/pdf'
        )
