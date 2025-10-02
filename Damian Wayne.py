# Importar streamlit
import streamlit as st

#-------------------------------- Contenido del sitio---------------------------#
#Sección Inicial
st.set_page_config(
    page_title="Damian Wayne",
    page_icon=":warning:"
    )
# Nombre e introducción de la sección de la página
st.header("")
st.title(
"""
Damian Wayne
Si eres fanático del universo de DC Comics, seguramente conoces a Damian Wayne, el hijo biológico de Bruce Wayne y Talia al Ghul. Criado por la Liga de Asesinos y entrenado desde la infancia para ser un guerrero letal, Damian es el Robin más joven, pero también el más peligroso. Su historia es una de redención, identidad y lucha interna. Nacido en la oscuridad, pero guiado por la esperanza de ser mejor que su legado, Damian ha demostrado que ser un Wayne significa mucho más que heredar un manto: es luchar por lo correcto incluso cuando todo en ti grita lo contrario. Acompáñame a descubrir la historia de este impetuoso heredero del murciélago.
"""
)

st.badge("Página verificada y visitada por los más curiosos", color="red", icon=":material/done_outline:")

st.divider()

 # Imagen del personaje,Subtítulo y contenido

st.image("damian11.jpg")

st.header("Historia", divider=True)
col1, col2 = st.columns(2)
col1.write(
"""
Damian Wayne fue introducido en el universo de DC en Batman #655 (2006), creado por Grant Morrison y Andy Kubert. Es el hijo de Bruce Wayne y Talia al Ghul, nieto del temido Ra’s al Ghul. Desde su nacimiento fue criado por la Liga de Asesinos, y entrenado en combate, estrategia y asesinato. A los diez años, Talia lo envía a Gotham para conocer a su padre y reclamar su lugar a su lado.
Desde su primera aparición, Damian mostró una personalidad arrogante, violenta y extremadamente segura de sí mismo. No entendía ni compartía el código de no matar de Batman. Su relación con Bruce fue tensa al principio, pero con el tiempo evolucionó hacia una conexión real de padre e hijo. Cuando Bruce "muere" durante los eventos de Final Crisis, Dick Grayson toma el manto de Batman, y Damian se convierte oficialmente en Robin bajo su tutela.
Durante esta etapa (Batman and Robin de Grant Morrison), se ve el desarrollo más importante del personaje: un joven asesino que, poco a poco, aprende lo que significa ser un héroe. Damian empieza a cuestionar su educación, a formar vínculos reales y a entender los valores que su padre representa.
Damian ha liderado a los Jóvenes Titanes, ha muerto heroicamente en Batman Incorporated #8 (2013), y luego resucitado. A lo largo de los años, ha buscado su identidad más allá del nombre de Robin, adoptando distintos alias como The Demon’s Heir, Redbird, y Batman en futuros alternativos. A pesar de sus conflictos con otros miembros de la Bat-familia, su evolución lo ha convertido en un personaje clave, complejo y profundamente humano dentro del universo DC.
"""
 )
col2.write(
"""
Primera aparición (cameo): Batman #655 (septiembre de 2006)
Por Grant Morrison y Andy Kubert en el arco “Batman and Son”.
Primera aparición completa: Batman #656 (octubre de 2006)
Batman and Robin (2009–2011)
Escrita por Grant Morrison, con Damian como Robin y Dick Grayson como Batman.
Batman Incorporated (2010–2013)
Incluye el arco donde Damian muere heroicamente en Batman Incorporated #8.
Robin: Son of Batman (2015–2016)
Serie en solitario escrita por Patrick Gleason, donde Damian busca redimirse por su pasado.
Super Sons (2017–2018)
Damian hace equipo con Jonathan Kent (el hijo de Superman). Serie muy querida por los fans.
Teen Titans (Rebirth, 2016–2020)
Damian lidera un nuevo equipo de Titanes jóvenes, aunque con un estilo autoritario.
Robin (2021)
Serie escrita por Joshua Williamson, donde Damian participa en el Torneo de los Lázaros.

🎬 Adaptaciones animadas destacadas
Damian Wayne es un personaje recurrente en el DC Animated Movie Universe (DCAMU), una línea de películas animadas interconectadas iniciada en 2013:
Son of Batman (2014)
Adaptación del arco Batman and Son. Damian conoce a Bruce y se convierte en Robin.
Batman vs. Robin (2015)
Basada en elementos de Court of Owls. Explora el conflicto entre Damian y Bruce por sus métodos.
Batman: Bad Blood (2016)
Damian se une a Batwoman y Nightwing para encontrar a Batman tras su desaparición.
Justice League vs. Teen Titans (2016)
Damian es obligado a unirse a los Titanes; explora su conflicto con Raven y Trigon.
Teen Titans: The Judas Contract (2017)
Continúa su desarrollo como líder de los Titanes.
Batman: Hush (2019)
Participa en el conflicto contra Hush, aunque con un rol menor.
Justice League Dark: Apokolips War (2020)
Final del universo DCAMU; tiene un papel crucial, lleno de drama y sacrificio.
"""
           )

col1.write(
"""
_Damian Wayne es posiblemente el Robin más polémico y disruptivo.
Donde otros buscaban redención, él busca control. Donde otros obedecían, él cuestiona.
Pero esa es precisamente la riqueza del personaje: es una contradicción andante.
Es arrogante, sí, pero también profundamente leal. Es agresivo, pero protector.
Damian representa la eterna lucha entre lo que fuimos criados para ser y lo que decidimos ser.
Con el paso de los años, Damian ha demostrado que no es solo un niño con espadas: es un héroe en construcción.
Ha aprendido a sentir empatía, a valorar el trabajo en equipo, y, sobre todo, a amar a su padre, incluso si nunca lo admite abiertamente.
En él vemos reflejado el potencial de redención más puro: el del que fue creado para matar, pero elige salvar._
"""
           )
col1.image("fin.jpg", caption="**<<I know I'm supposed to be the bad son. The spoiled brat. The killer. But I don't want to be that anymore.>>**")

col2.video("https://www.youtube.com/watch?v=ICOmWEVuM1U")




