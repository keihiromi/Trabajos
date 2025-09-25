# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("Sobre nosotros")
st.badge("nuevo", color="green")
page_icon=":star:"

# Sutítulo
st.header("DCuriosos, una página de aficionados y fanáticos", divider=True)
st.image("cara.jpg", caption="hiiii:)")
st.write(
"""
¿Quiénes somos?
¡Bienvenidos a DCuriosos! el lugar de encuentro para todos los apasionados por el complejo y fascinante universo de Batman.
Nuestra página nació de una idea simple: crear un espacio exhaustivo y dedicado a los personajes que han hecho de Gotham City una leyenda, inicialmente abordaremos la historia de 4 generaciones de Robins.

No somos una gran corporación, sino un grupo de amigos y seguidores que crecimos leyendo cómics y viendo a nuestros personajes favoritos en la pantalla grande. Nuestro objetivo es ser su guía definitiva, un portal que no solo les dé información, sino que celebre la riqueza de las historias que han cautivado a generaciones.
Página anonima hasta mayor popularidad :'l
"""
    )
st.audio("miedo.mp3")