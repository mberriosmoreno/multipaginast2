import streamlit as st

# --- AJUSTES DE ESTILO PARA REDUCIR ESPACIOS ---
st.markdown("""
<style>
/* Reducir el espacio entre el menú y el contenido */
div[data-testid="stSidebar"] {
    padding-top: 0rem;
    padding-bottom: 0rem;
}
/* Reducir el margen superior del contenido principal */
div[data-testid="stAppViewContainer"] {
    padding-top: 0rem;
}
/* Estilo compacto para los botones del menú */
button[kind="secondary"] {
    margin: 0.2rem 0;
    padding: 0.5rem;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# --- CONFIGURACIÓN DE PÁGINAS ---
def about_me():
    st.title("🏠 Acerca de Mí")
    st.write("""
    Esta es la página "Acerca de Mí". Aquí puedes incluir información sobre ti,
    tu proyecto o cualquier otro detalle relevante.
    """)

def dashboard():
    st.title("📊 Tablero de Datos")
    st.write("Esta es la página del tablero de datos.")

    # Ejemplo de un DataFrame
    import pandas as pd
    data = {
        "Nombre": ["Juan", "María", "Pedro"],
        "Edad": [25, 30, 35],
        "Ciudad": ["Madrid", "Barcelona", "Valencia"],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

def chatbot():
    st.title("🤖 Chat Bot")
    st.write("Esta es la página del Chat Bot.")

    # Ejemplo de un chat interactivo
    user_input = st.text_input("Escribe algo:")
    if user_input:
        st.write(f"El bot responde: ¡Hola! Has escrito '{user_input}'.")

# --- MENÚ FIJO CON BOTONES ESTILIZADOS ---
st.sidebar.markdown("### 🌟 Menú Principal")

# Lista de páginas disponibles
pages = {
    "🏠 Acerca de Mí": about_me,
    "📊 Tablero de Datos": dashboard,
    "🤖 Chat Bot": chatbot,
}

# Contenedor para los botones
with st.sidebar:
    for title, page_func in pages.items():
        if st.button(title, width=200):
            st.session_state.page = page_func
        st.markdown("---")  # Línea divisoria para mejorar el diseño

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
try:
    st.image("assets/logo.png", width=200)  # Logo compartido
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo 'logo.png' esté en la carpeta 'assets/'.")

st.sidebar.markdown("Hecho con ❤️ por [Tu Nombre](https://tupagina.com)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if "page" not in st.session_state:
    st.session_state.page = about_me  # Página predeterminada

# Contenedor principal para el contenido
with st.container():
    st.session_state.page()
