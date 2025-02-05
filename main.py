import streamlit as st

# --- CONFIGURACIÓN DEL MENÚ FIJO ---
st.sidebar.markdown("### 🌟 Menú Principal")

# Lista de páginas disponibles
pages = {
    "🏠 Acerca de Mí": "about_me",
    "📊 Tablero de Datos": "dashboard",
    "🤖 Chat Bot": "chatbot",
}

# Contenedor para los botones
with st.sidebar:
    for title, page_name in pages.items():
        if st.button(title, use_container_width=True):
            st.session_state.page = page_name
        st.markdown("---")  # Línea divisoria para mejorar el diseño

# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
try:
    st.image("assets/logo.png", use_column_width=True)  # Logo compartido
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo 'logo.png' esté en la carpeta 'assets/'.")

st.sidebar.markdown("Hecho con ❤️ por [Tu Nombre](https://tupagina.com)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if "page" not in st.session_state:
    st.session_state.page = "about_me"  # Página predeterminada

# Importar dinámicamente la página seleccionada
if st.session_state.page == "about_me":
    from pages.about_me import main as about_me_main
    about_me_main()
elif st.session_state.page == "dashboard":
    from pages.dashboard import main as dashboard_main
    dashboard_main()
elif st.session_state.page == "chatbot":
    from pages.chatbot import main as chatbot_main
    chatbot_main()
