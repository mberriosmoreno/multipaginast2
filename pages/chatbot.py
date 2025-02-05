import streamlit as st

def main():
    st.title("🤖 Chat Bot")
    st.write("Esta es la página del Chat Bot.")

    # Ejemplo de un chat interactivo
    user_input = st.text_input("Escribe algo:")
    if user_input:
        st.write(f"El bot responde: ¡Hola! Has escrito '{user_input}'.")
