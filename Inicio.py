# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("DCuriosos")
st.badge("contenido basado y relatado sobre los comics", color="red" , icon=":material/done_outline:")

# Sutítulo
st.header("*Universo de Gotham*", divider=True)
st.image("gotham portada.jpg", caption="Gotham City")
st.write(
"""
Bienvenido a las sombras.
En el corazón de la metrópolis más oscura, Gotham no es solo una ciudad, sino un campo de batalla para el alma humana.
Cada uno de sus habitantes, desde el vigilante solitario que se alza contra la oscuridad, teje una historia de lucha, redención y esperanza.
Aquí te adentrarás en un universo de personajes complejos y llenos de matices.
Explorarás la dualidad de héroes que, bajo la guía de Batman, han encontrado su propio camino para proteger a los inocentes.
Entre estos valientes se encuentra el legado de *Robin*, una figura que ha evolucionado con cada joven que ha portado el manto.
Desde el espíritu acrobático y la alegría de *Dick Grayson*, el primer Robin que se convirtió en un líder por derecho propio;
hasta el temperamento rebelde e impulsivo de *Jason Todd*, cuya historia de vida y muerte desafió la moral de Batman.
Conoce también la brillante mente de *Tim Drake*, el detective que descubrió la identidad del Caballero Oscuro por sí mismo,
y la intensa disciplina de *Damian Wayne*, el hijo de Bruce.
Cada uno de ellos representa una faceta distinta de la lucha por la justicia.

Esta es tu entrada a un mundo de leyendas, donde cada máscara oculta una historia.
Prepárate para descubrir los orígenes, las motivaciones y el legado de los héroes que han hecho del universo de Batman un mito eterno.

"""
    )