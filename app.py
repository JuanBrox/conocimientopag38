import streamlit as st

st.set_page_config(page_title="Reino de los Animales", page_icon="🦄", layout="centered")

st.markdown(
    """
<style>
.stApp { background: linear-gradient(180deg, #fff0fa 0%, #f0f4ff 100%); }
h1, h2, h3 { color: #8e44ad; }
.tarjeta { background: white; border-radius: 16px; padding: 14px 18px;
           border: 2px solid #f5c6ea; margin-bottom: 10px; font-size: 1.1rem; }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🦄 El Reino de los Animales 🧚")
st.caption("Repaso de Conocimiento del Medio · página 28 · Practicar y avanzar")

seccion = st.sidebar.radio(
    "¿Qué quieres practicar?",
    [
        "👂 Los sentidos",
        "🍽️ ¿Qué comen?",
        "✏️ Corrige la frase",
        "🥚 Ovíparos o vivíparos",
        "🏆 Mini quiz",
    ],
)


def resultado(ok, bien, mal):
    if ok:
        st.success(f"🌟 ¡Muy bien! {bien}")
    else:
        st.warning(f"💡 Casi. {mal}")


# ---------------------------------------------------------------- SENTIDOS
if seccion.startswith("👂"):
    st.header("👂 Los sentidos")
    st.markdown(
        '<div class="tarjeta">Los órganos de los sentidos captan información del entorno '
        "(luz, sonidos, olores, sabores, temperatura...) para que el animal pueda reaccionar.</div>",
        unsafe_allow_html=True,
    )
    sentidos = {
        "👁️ Vista": ("Ojos", "El águila ve a su presa desde muy lejos."),
        "👂 Oído": ("Orejas", "El murciélago oye los sonidos para orientarse."),
        "👃 Olfato": ("Nariz", "El perro huele para encontrar comida."),
        "✋ Tacto": ("Piel / bigotes", "Los bigotes del gato le avisan de si cabe por un hueco."),
        "👅 Gusto": ("Lengua", "La serpiente prueba el aire con la lengua."),
    }
    for nombre, (organo, ejemplo) in sentidos.items():
        with st.expander(nombre):
            st.write(f"**Órgano:** {organo}")
            st.write(f"**Ejemplo:** {ejemplo}")

    st.subheader("🎯 Une el sentido con el animal")
    pregunta = st.radio(
        "¿Qué sentido usa el perro para encontrar comida?",
        ["Vista", "Olfato", "Gusto"],
        index=None,
        key="s1",
    )
    if pregunta:
        resultado(pregunta == "Olfato", "El perro huele con su nariz.", "Piensa en la nariz del perro.")

# ---------------------------------------------------------------- ALIMENTACIÓN
elif seccion.startswith("🍽️"):
    st.header("🍽️ ¿Qué comen?")
    st.write("🌿 **Herbívoros**: plantas · 🥩 **Carnívoros**: otros animales · 🍽️ **Omnívoros**: de todo")
    animales = {
        "🐼 Panda": "Herbívoro",
        "🐅 Tigre": "Carnívoro",
        "🐑 Oveja": "Herbívoro",
        "🐦 Gaviota": "Omnívoro",
        "🪰 Mosca": "Omnívoro",
        "🦅 Buitre": "Carnívoro",
        "🕷️ Araña": "Carnívoro",
        "🐿️ Ardilla": "Herbívoro",
        "🐺 Lobo": "Carnívoro",
    }
    opciones = ["Elige...", "Herbívoro", "Carnívoro", "Omnívoro"]
    elecciones = {}
    cols = st.columns(3)
    for i, a in enumerate(animales):
        elecciones[a] = cols[i % 3].selectbox(a, opciones, key=f"al_{a}")
    if st.button("✨ Comprobar"):
        aciertos = sum(1 for a, r in animales.items() if elecciones[a] == r)
        for a, r in animales.items():
            if elecciones[a] != r:
                st.write(f"❌ {a}: es **{r}**")
        st.subheader(f"Aciertos: {aciertos} de {len(animales)}")
        if aciertos == len(animales):
            st.balloons()
            st.success("🦄 ¡Perfecto!")

# ---------------------------------------------------------------- ORACIONES
elif seccion.startswith("✏️"):
    st.header("✏️ Corrige la frase")
    frases = [
        ("Los seres humanos somos carnívoros.",
         ["Los seres humanos somos omnívoros.", "Los seres humanos somos herbívoros."],
         0),
        ("Todos los animales son ovíparos.",
         ["No todos los animales son ovíparos: hay ovíparos y vivíparos.", "Todos los animales son vivíparos."],
         0),
        ("La mayoría de los animales tienen reproducción asexual.",
         ["La mayoría de los animales tienen reproducción sexual.", "Ningún animal tiene reproducción sexual."],
         0),
        ("Algunos animales no se relacionan con el entorno.",
         ["Todos los animales se relacionan con el entorno.", "Las plantas se relacionan más que los animales."],
         0),
    ]
    for i, (mala, opts, bien) in enumerate(frases):
        st.markdown(f'<div class="tarjeta">❌ {mala}</div>', unsafe_allow_html=True)
        eleg = st.radio("¿Cómo se escribe bien?", opts, index=None, key=f"fr_{i}")
        if eleg:
            resultado(opts.index(eleg) == bien, "Así es.", "Vuelve a leerla despacio.")
        st.divider()

# ---------------------------------------------------------------- OVÍPAROS
elif seccion.startswith("🥚"):
    st.header("🥚 Ovíparos o vivíparos")
    st.write("🥚 **Ovíparos**: nacen de huevos · 🍼 **Vivíparos**: nacen del vientre de la madre")
    bichos = {"🐜 Hormiga": "Ovípara", "🐢 Tortuga (galápago)": "Ovípara",
              "🦭 Foca": "Vivípara", "🐦 Cigüeña": "Ovípara"}
    for nombre, resp in bichos.items():
        eleg = st.radio(nombre, ["Ovípara", "Vivípara"], index=None, horizontal=True, key=f"ov_{nombre}")
        if eleg:
            resultado(eleg == resp, f"{nombre} es {resp.lower()}.", "Piensa: ¿pone huevos o nace de su mamá?")

# ---------------------------------------------------------------- QUIZ
else:
    st.header("🏆 Mini quiz")
    preguntas = [
        ("¿Para qué sirven los órganos de los sentidos?",
         ["Para captar información del entorno", "Para digerir la comida", "Para respirar"], 0),
        ("El tigre es...", ["Herbívoro", "Carnívoro", "Omnívoro"], 1),
        ("Los seres humanos somos...", ["Carnívoros", "Herbívoros", "Omnívoros"], 2),
        ("La foca es...", ["Ovípara", "Vivípara"], 1),
        ("Los animales que nacen de huevos son...", ["Vivíparos", "Ovíparos"], 1),
    ]
    respuestas = []
    for i, (q, opts, _) in enumerate(preguntas):
        respuestas.append(st.radio(f"{i + 1}. {q}", opts, index=None, key=f"q_{i}"))
    if st.button("🎉 Ver mi nota"):
        if None in respuestas:
            st.info("Contesta todas las preguntas 😊")
        else:
            nota = sum(1 for (q, o, b), r in zip(preguntas, respuestas) if o.index(r) == b)
            st.subheader(f"Has acertado {nota} de {len(preguntas)}")
            if nota == len(preguntas):
                st.balloons()
                st.success("🦄 ¡Eres una experta de los animales!")
            else:
                st.info("🧚 ¡Repasa y vuelve a intentarlo!")
