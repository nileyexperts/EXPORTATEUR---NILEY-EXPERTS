import streamlit as st

st.set_page_config(page_title="Contact", page_icon="✉️")
st.header("✉️ Nous contacter")
st.caption("Formulaire local (aucun envoi externe). Connectez-le à votre backend ou un service comme Formspree.")

with st.form("contact_form"):
    nom = st.text_input("Nom")
    email = st.text_input("Email")
    sujet = st.text_input("Sujet")
    message = st.text_area("Message")
    ok = st.form_submit_button("Envoyer")

if ok:
    if not (nom and email and message):
        st.error("Merci de remplir les champs obligatoires.")
    else:
        st.success("Message enregistré localement (démo). Branchez un vrai service d'envoi pour la production.")
