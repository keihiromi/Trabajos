# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Personaje de DC",
    page_icon=":star:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

pg = st.navigation(["Inicio.py", "Dick Grayson.py", "Jason Todd.py", "Tim Drake.py", "Damian Wayne.py", "Sobre nosotros.py"])
pg.run()