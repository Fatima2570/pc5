
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="CV de Fátima Portilla", page_icon="📄")

# Título principal
st.title("Currículum Vitae")
st.subheader("Fátima Portilla Caballero")

# Información de contacto
st.header("📞 Información de contacto")
st.write("📧 Correo: fportill2025@gmail.com")
st.write("📱 Teléfono: 933054145")
st.write("📍 Ubicación: Lima, Perú")

# Educación
st.header("🎓 Educación")
st.write("- Universidad Católica")

# Habilidades
st.header("🛠️ Habilidades")
st.write("- Creatividad")
st.write("- Liderazgo")
st.write("- Trabajo en equipo")

# Idiomas
st.header("🌍 Idiomas")
st.write("- Inglés (avanzado)")
st.write("- Francés (básico)")

# Mensaje final
st.markdown("---")
st.write("Gracias por visitar mi CV.")