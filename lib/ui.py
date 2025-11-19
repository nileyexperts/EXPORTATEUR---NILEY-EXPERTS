from pathlib import Path
import json
import streamlit as st

def load_json(path):
    p = Path(path)
    if not p.exists():
        return []
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        st.error(f"Erreur de lecture: {e}")
        return []

def inject_css():
    css_path = Path('assets/styles.css')
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

def render_country_cards(countries):
    if not countries:
        st.info("Aucun pays trouvé.")
        return
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    for c in countries:
        img_html = f'<div class="card-image"><img src="{c.get("flag")}" alt="drapeau"/></div>' if c.get('flag') else ''
        card_html = (
            '<div class="card">'
            f'{img_html}'
            '<div class="card-header">'
            f'<div class="card-title">{c.get("name")}</div>'
            f'<div class="card-meta">{c.get("continent")}</div>'
            '</div>'
            f'<div class="card-body">Code ISO: {c.get("iso")}</div>'
            '<div class="card-actions">'
            f'{("<a href=""+c["source"]+"" target="_blank">🔗 Source</a>") if c.get("source") else ""}'
            '</div>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
