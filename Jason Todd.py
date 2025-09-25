import streamlit as st

st.set_page_config(
    page_title="Jason Todd",
    page_icon=":boom:"
    )
st.header("")
st.title(
"""
Jason Todd
Si eres fanático del universo de DC Comics, probablemente conozcas a Jason Todd, una figura compleja y fascinante.
Desde su trágico destino como el segundo Robin hasta su impactante regreso como Red Hood, la historia de Jason es una de las más oscuras y redentoras de los cómics.
Aquí, nos sumergiremos en la evolución de este personaje, explorando sus momentos más emblemáticos, su relación con Batman y el resto de la Bat-familia, y cómo ha logrado forjar su propio camino. Únete a mí en este viaje para desentrañar el legado de uno de los antihéroes más intrigantes de Gotham.
"""
)

st.badge("Página verificada y visitada por los más curiosos", color="red", icon=":material/done_outline:")

st.divider()

st.image("red hood.jpg")
    
st.header("Historia", divider=True)
col1, col2 = st.columns(2)
col1.write(
"""
Jason Peter Todd hace su primera aparición como Robin en Batman #357 (1983) Después del evento Crisis on Infinite Earths, su origen fue redefinido: era un huérfano callejero y ladrón que intentó robar el Batimóvil, y fue adoptado y entrenado por Batman.
En el arco Batman: Una muerte en la familia (1988), el Joker brutalmente golpea a Jason y lo deja morir en una explosión.
La decisión sobre su destino se tomó mediante una votación telefónica abierta a los lectores, donde por apenas unos cientos de votos venció la opción de que muriera.
Años más tarde se reveló que una sola persona pudo haber manipulado la votación automatizando llamadas, lo que generó críticas y polémica, Jason regresa a la vida gracias al Pozo de Lázaro
y asume la identidad de Red Hood, adoptando métodos violentos y cuestionables en su cruzada contra el crimen,
en parte motivado por su resentimiento hacia Batman y el Joker.
El arco Batman: Under the Red Hood (2004–2006) escrito por Judd Winick y dibujado por Doug Mahnke, revela su identidad como Red Hood,
desarrollando una trama icónica que fue adaptada en una película animada.
"""
 )
col2.write(
"""
La película narra la historia del regreso de Jason Todd, el segundo Robin, ahora como un justiciero letal conocido como Red Hood. Jason, que fue asesinado por el Joker años atrás, regresa resucitado y
con una nueva filosofía: eliminar permanentemente a los criminales de Gotham.
La película inicia con una escena desgarradora: el Joker golpea brutalmente a Jason Todd con una palanca y lo deja morir en una explosión.
Batman llega tarde para salvarlo, y la tragedia lo marca profundamente.
5 años después,Una nueva figura aparece en Gotham: el Red Hood, un vigilante brutal que se enfrenta al crimen organizado.
A diferencia de Batman, Red Hood no tiene reparos en matar, y comienza a tomar el control del submundo criminal.
El jefe criminal Black Mask se ve superado por Red Hood, quien interfiere con sus operaciones.
Desesperado, libera al Joker del Asilo Arkham, esperando que lo ayude a eliminar al nuevo vigilante.
Batman comienza a descubrir que Red Hood sabe demasiado sobre su pasado y su estilo de lucha.
Luego de una serie de enfrentamientos, Batman confirma que Red Hood es Jason Todd, de alguna forma resucitado.
En un clímax emocional, Jason confronta a Batman, acusándolo de no vengar su muerte.
Jason sostiene al Joker a punta de pistola y le exige a Batman que lo mate si no está dispuesto a hacerlo él mismo.
Batman se niega a matar, incluso cuando Jason dispara. Finalmente, una explosión interrumpe el enfrentamiento y Jason desaparece...
"""
           )

col1.write(
"""
_Después de su muerte, la historia de Jason Todd fue explorada más a fondo en varias series de cómics.
Su resurrección y su nueva identidad como Red Hood lo consolidaron como un personaje complejo y moralmente ambiguo en el Universo DC.
El arco argumental de "Batman: Under the Red Hood" es considerado uno de los relatos de Batman modernos más significativos, ya que
explora temas de segundas oportunidades, venganza y los límites éticos que Batman no está dispuesto a cruzar.
Este arco tuvo un impacto duradero en la dinámica entre Batman y sus antiguos protegidos,
lo que convirtió a Jason Todd en un personaje muy popular y en una figura central en la Bat-familia._
"""
           )
col1.image("final.jpg", caption="**<<I'm not talking about killing Penguin or Two-Face or Riddler. I'm talking about him. Just him. And doing it because… because he took me away from you.>>**")
col2.video("https://youtu.be/gTY_N9de_fU?si=LjWY9B8w7ErgWKDr")