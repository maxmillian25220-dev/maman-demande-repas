import streamlit as st

# --- PROTECTION PAR MOT DE PASSE ---
def check_password():
    def password_entered():
        if st.session_state["password"] == "maman2026":  # Tu peux changer le mot de passe ici
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Ne pas stocker le mot de passe
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Mot de passe requis pour accéder à l'application :", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Mot de passe requis pour accéder à l'application :", type="password", on_change=password_entered, key="password")
        st.error("😕 Mot de passe incorrect")
        return False
    else:
        return True

if not check_password():
    st.stop()  # Stoppe l'affichage si le mot de passe n'est pas bon

# --- TON APPLICATION COMMENCE ICI ---
st.set_page_config(page_title="Maman Demande Repas", page_icon="🍲", layout="centered")

st.title("🍲 Maman Demande Repas")
st.write("Bienvenue ! Dis-nous ce qui te ferait plaisir pour tes repas.")

repas_proposes = [
    "Poulet rôti et pommes de terre",
    "Soupe de légumes maison",
    "Blanquette de veau",
    "Poisson et riz",
    "Gratin dauphinois",
    "Autre chose (préciser ci-dessous)"
]

choix = st.selectbox("Choisis un plat dans la liste :", repas_proposes)

autre_plat = ""
if choix == "Autre chose (préciser ci-dessous)":
    autre_plat = st.text_input("Entre le nom du plat que tu désires :")

if st.button("Envoyer ma demande 💌"):
    plat_final = autre_plat if choix.startswith("Autre chose") else choix
    if plat_final:
        st.success(f"C'est noté maman ! Ta demande pour : **{plat_final}** a bien été prise en compte. Bon appétit ! 🥰")
    else:
        st.warning("Merci de bien vouloir indiquer un plat.")

st.markdown("---")
st.caption("Application créée spécialement pour maman ❤️")