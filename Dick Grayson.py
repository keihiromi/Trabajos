import streamlit as st

st.set_page_config(
    page_title="Dick Grayson",
    page_icon=":circus_tent:"
    )
st.header("")
st.title(
"""
Dick Grayson
Si eres fanático del universo de DC Comics, seguro conoces a Dick Grayson, el primer Robin y uno de los personajes más icónicos y queridos de la Bat-familia. Desde sus días como el joven compañero de Batman hasta su evolución como el intrépido Nightwing, la historia de Dick es un viaje de crecimiento, independencia y heroísmo. Acompáñame a explorar la trayectoria de este legendario personaje, sus momentos más emblemáticos, su relación con Batman y cómo se ha ganado un lugar propio en el corazón de Gotham... y del mundo.
"""
)

st.badge("Página verificada y visitada por los más curiosos", color="blue", icon=":material/done_outline:")

st.divider()

st.image("grayson.jpg")
    
st.header("Historia", divider=True)
col1, col2 = st.columns(2)
col1.write(
"""
Dick Grayson hizo su primera aparición en Detective Comics #38 (1940), creado por Bob Kane y Bill Finger, junto con el dibujante Jerry Robinson. Fue el primer Robin, y su inclusión marcó el inicio de la tradición de los "sidekicks" en los cómics. Hijo de dos acróbatas de circo, los Flying Graysons, Dick quedó huérfano tras un "accidente" provocado por la mafia. Bruce Wayne, al ver paralelismos con su propia tragedia, lo acogió y entrenó para que se convirtiera en su compañero en la lucha contra el crimen.
Con el tiempo, Dick empezó a cuestionar los métodos y decisiones de Batman. Ya no era el niño obediente, sino un joven con ideales propios. Esto lo llevó a distanciarse de su mentor y adoptar una nueva identidad: Nightwing, debutando oficialmente como tal en Tales of the Teen Titans #44 (1984), bajo la pluma de Marv Wolfman y George Pérez. Como Nightwing, Dick se estableció como líder nato, especialmente al frente de los Teen Titans, y consolidó su lugar como uno de los héroes más respetados del Universo DC.
A lo largo de los años, ha tomado incluso el manto de Batman, en momentos en que Bruce Wayne ha desaparecido o se ha considerado incapacitado, mostrando que es mucho más que el "primer Robin": es un digno heredero del legado del Caballero Oscuro.
"""
 )
col2.write(
"""
Al convertirse en Nightwing, Dick logró lo que pocos sidekicks han conseguido: dejar la sombra de su mentor y construir un legado propio. Se trasladó a la ciudad de Blüdhaven, donde enfrentó el crimen a su manera, con un enfoque más empático, ágil y humano. Su traje, azul y negro, representa ese cambio: ya no era el chico maravilla, sino un protector por derecho propio.
En arcos como Nightwing: Year One, The Judas Contract (Teen Titans), y Nightwing: Better Than Batman, su crecimiento como personaje es evidente. Sus historias combinan acción, drama y humor, manteniendo siempre ese espíritu heroico que lo define. Dick Grayson ha sido adaptado en numerosas series animadas como Batman: The Animated Series, The New Batman Adventures, Teen Titans y Young Justice, donde se explora tanto su tiempo como Robin como su evolución a Nightwing. También ha aparecido en películas animadas como Batman: Bad Blood y Justice League vs Teen Titans.
En la serie Titans (2018–2023), se narra un enfoque más maduro y oscuro de su transformación, mostrando sus conflictos internos, su compleja relación con Bruce Wayne, y su camino hacia la aceptación de su rol como líder.
"""
           )

col1.write(
"""
_Dick Grayson no es solo el primer Robin. Es el corazón de la Bat-familia, un líder nato, y uno de los personajes más completos del Universo DC. Su historia nos recuerda que incluso en un mundo de sombras, se puede elegir ser una luz._
"""
           )
col1.image("grayson2.png", caption="**<<I’m not Bruce. I’m never gonna be Bruce. I’m me.>>**")
col2.video("https://www.youtube.com/watch?v=ix5gGs7L5RA ")