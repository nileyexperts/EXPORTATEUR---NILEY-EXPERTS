import streamlit as st
import pydeck as pdk
from lib.ui import load_json, inject_css, render_country_cards

st.set_page_config(page_title="Fiches Pays", page_icon="🌍", layout="wide")
inject_css()

st.header("🌍 Fiches Pays")
st.caption("Recherche, filtres par continent, affichage avec drapeaux et carte interactive.")

countries = load_json('data/pays.json')

search = st.text_input("🔎 Rechercher un pays", placeholder="Nom du pays…")
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
    st.subheader("🗺 Carte interactive")
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=filtered,
        get_position='[lon, lat]',
        get_radius=500000,
        get_fill_color='[13,92,99,160]',
        pickable=True
    )
    view_state = pdk.ViewState(latitude=20, longitude=0, zoom=1.2)
    st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{name}"}))

st.subheader("📋 Liste des pays")
render_country_cards(filtered)
