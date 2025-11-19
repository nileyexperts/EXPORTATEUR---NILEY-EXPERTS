from pathlib import Path
import json
import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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

def country_card_html(c):
    img_html = f'<div class="card-image"><img src="{c.get("flag")}" alt="drapeau"/></div>' if c.get('flag') else ''
    parts = []
    parts.append('<div class="card">')
    parts.append(img_html)
    parts.append('<div class="card-header">')
    parts.append(f'<div class="card-title">{c.get("name")}</div>')
    parts.append(f'<div class="card-meta">{c.get("continent")}</div>')
    parts.append('</div>')
    parts.append(f'<div class="card-body">Code ISO: {c.get("iso")}<br/>PIB: {c.get("GDP","-")}<br/>Population: {c.get("Population","-")}</div>')
    link = f'<a href="{c["source"]}" target="_blank">🔗 Source</a>' if c.get('source') else ''
    parts.append('<div class="card-actions">' + link + '</div>')
    parts.append('</div>')
    return ''.join(parts)

def render_country_cards(countries):
    if not countries:
        st.info("Aucun pays trouvé.")
        return
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    for c in countries:
        st.markdown(country_card_html(c), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def build_country_pdf_bytes(c):
    buf = BytesIO()
    cnv = canvas.Canvas(buf, pagesize=A4)
    cnv.setTitle(f"Fiche {c.get('name')}")
    cnv.setFont("Helvetica-Bold", 16)
    cnv.drawString(50, 800, f"Fiche Pays : {c.get('name')}")
    cnv.setFont("Helvetica", 12)
    y = 770
    lines = [
        f"Code ISO : {c.get('iso')}",
        f"Continent : {c.get('continent')}",
        f"PIB (USD) : {c.get('GDP','-')}",
        f"Population : {c.get('Population','-')}",
        f"Source : {c.get('source','-')}"
    ]
    for line in lines:
        cnv.drawString(50, y, line)
        y -= 20
    cnv.showPage()
    cnv.save()
    buf.seek(0)
    return buf
