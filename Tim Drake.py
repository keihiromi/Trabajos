import streamlit as st

st.set_page_config(
    page_title="Tim Drake",
    page_icon=":coffee:"
    )
st.header("")
st.title(
"""
Tim Drake
Si eres fanático del universo de DC Comics, no puedes pasar por alto a Tim Drake, el tercer Robin, y uno de los personajes más inteligentes y estratégicos de toda la Bat-familia. A diferencia de sus predecesores, Tim no llegó al manto de Robin por tragedia, sino por convicción. Su historia es una de determinación, ingenio y lealtad. En este recorrido exploraremos su evolución, sus momentos más destacados, su vínculo con Batman, y cómo ha construido una identidad propia, más allá del traje rojo y amarillo.
"""
)

st.badge("Página verificada y visitada por los más curiosos", color="green", icon=":material/done_outline:")

st.divider()

st.image("timdrake1.jpg")
    
st.header("Historia", divider=True)
col1, col2 = st.columns(2)
col1.write(
"""
Timothy Jackson Drake debutó en Batman #436 (1989), durante el arco Batman: A Lonely Place of Dying, escrito por Marv Wolfman y dibujado por Jim Aparo. Desde pequeño, Tim fue un niño extremadamente inteligente, con una mente analítica que lo llevó a descubrir por sí solo las identidades de Batman y Robin, tras observar las acrobacias de Dick Grayson en los medios y compararlas con las de Robin.
Tim creció en una familia adinerada, pero emocionalmente distante. Tras la muerte de Jason Todd, Gotham estaba más oscura que nunca y Batman se volvía cada vez más violento. Tim entendió que Bruce necesitaba un Robin, no solo como compañero de lucha, sino como ancla emocional. Así, convenció a Alfred y a Dick de que él era el indicado. Con entrenamiento intensivo por parte de Batman, Nightwing y otros, Tim se convirtió oficialmente en el tercer Robin.
A diferencia de Jason, Tim no fue adoptado inmediatamente por Bruce, pero con el tiempo, tras la muerte de sus padres (en distintos eventos), se convirtió en su tutor legal. Su enfoque siempre fue más detective, más cerebral. En muchos sentidos, es considerado el "mejor Robin" en cuanto a estrategia e investigación, un digno sucesor del legado de Batman.
Con el tiempo, adoptó nuevas identidades: primero como Red Robin y más recientemente como Robin Drake o simplemente Tim Drake, dependiendo de la línea editorial. A pesar de todos los cambios, siempre ha sido uno de los miembros más constantes y leales de la Bat-familia.
"""
 )
col2.write(
"""
La relación de Tim con Bruce Wayne es más de respeto mutuo y admiración intelectual. Bruce confía profundamente en su capacidad como detective y estratega, incluso dejándolo a cargo de Gotham en varias ocasiones.
Después de dejar el manto de Robin cuando Damian Wayne fue designado como su sucesor, Tim adoptó la identidad de Red Robin, utilizando un nuevo traje más oscuro, con capa roja y símbolo distintivo. Como Red Robin, viajó por el mundo en busca de Bruce Wayne tras su aparente muerte (Final Crisis), demostrando ser uno de los pocos que creyó que Batman seguía vivo.
En esta etapa, lideró a los Teen Titans y se consolidó como un estratega de nivel Liga de la Justicia. Red Robin no era solo una nueva identidad: era una evolución. Aunque más serio y táctico, Tim nunca perdió su esencia de héroe ético y comprometido con la justicia.
Tim ha aparecido en múltiples adaptaciones animadas:

En The New Batman Adventures, es el Robin oficial al lado de Bruce.

En Young Justice, aparece como Red Robin en la segunda temporada.

En Batman: Arkham Knight (videojuego), es un personaje jugable y pieza clave de la historia.

En la serie Titans, Tim aparece como un joven inteligente y curioso que busca ser el siguiente Robin, similar a su origen en los cómics.

Aunque a veces se le ve como “el Robin olvidado”, muchos fans lo consideran el Robin más equilibrado: el perfecto punto medio entre la disciplina de Dick, la rebeldía de Jason y la arrogancia de Damian.
"""
           )

col1.write(
"""
_Tim Drake es más que el tercer Robin. Es el detective del futuro, el líder silencioso, y uno de los pilares más firmes de la Bat-familia. En un mundo donde muchos caen, Tim sigue de pie. Siempre listo. Siempre observando. Siempre un paso adelante._
"""
           )
col1.image("timdrake2.jpg", caption="**Adaptaciones del personaje**")
col2.video("https://www.youtube.com/watch?v=8RQHY9mDyd4")