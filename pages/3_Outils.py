import streamlit as st

st.set_page_config(page_title="Outils", page_icon="🧰")
st.header("🧰 Outils & calculateurs")
st.caption("Intégrez vos applications métiers (ex: calculateur CO₂, convertisseurs, etc.).")

with st.form("outil_demo"):
    st.subheader("Exemple : convertisseur simple")
    x = st.number_input("Valeur en kg", min_value=0.0, value=1.0)
    ratio = st.number_input("Ratio (kg → t)", min_value=0.001, value=0.001)
    submitted = st.form_submit_button("Calculer")
    if submitted:
        st.success(f"Résultat: {x * ratio:.3f} t")

st.info("Remplacez cet exemple par vos propres outils.")
