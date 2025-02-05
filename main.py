import streamlit as st

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
        if st.button(title, use_container_width=True):
            st.session_state.page = page_func
        st.markdown("---")  # Línea divisoria para mejorar el diseño

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
try:
    st.image("assets/logo.png", use_column_width=True)  # Logo compartido
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo 'logo.png' esté en la carpeta 'assets/'.")

st.sidebar.markdown("Hecho con ❤️ por [Tu Nombre](https://tupagina.com)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if "page" not in st.session_state:
    st.session_state.page = about_me  # Página predeterminada

# Renderizar la página seleccionada
st.session_state.page()
