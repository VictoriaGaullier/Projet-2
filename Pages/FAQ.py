import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL de l'animation Lottie du panda
lottie_url_panda = "https://assets9.lottiefiles.com/packages/lf20_puwecidm.json"
lottie_panda = load_lottieurl(lottie_url_panda)

# Configuration de la sidebar
with st.sidebar:
    # Ajouter un espace vertical pour centrer l'animation Lottie
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    
    # Afficher l'animation Lottie du panda
    st_lottie(lottie_panda, width=400, height=400, key="panda", loop=True)

st.title('Foire Aux Questions')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.header("Qu'est ce qu'un système de recommandation ?")
st.write('')
st.write("Un système de recommandation est utilisé pour permettre à un utilisateur d'avoir une recommandation basée sur sur ses goûts")
st.write('Nous nous sommes basé sur la base de données disponible sur IMDb')
st.write('')
st.write('')
st.write('')
st.write('')
st.header("Comment utiliser notre système de recommandation ?")
st.write('')
st.write("Pour utiliser ce système de recommandation, c'est simple : il faut avoir aimer au moins un film ! Une fois cela fait, il faut rentrer le titre du film dans la barre de sélection qui grâce à un algorithme vous recommendera des films que vous serez susceptible d'apprécier.")
st.write('')
st.write('')
st.write('')
st.write('')
st.header('Qui sommes-nous ?')
st.write('')
st.write('Nous sommes le cinéma LE SENECHAL basé dans la Creuse. Nous avons souhaité diversifier notre offre et vous offrir ce système de recommandation de films.')
st.write('')
st.write('')
st.write('')
st.write('')
st.header('Qui sont les CinéHackers ?')
st.write('')
st.write("Cinéhackers est une entreprise de Data Analyse créee en 2023. C'est à elle que nous lui avons demandé de réaliser cette application.")