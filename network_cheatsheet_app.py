import streamlit as st
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Datakommunikasjon Cheatsheet",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .section-container {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        margin-bottom: 10px;
        background-color: white;
        height: 100%;
    }

    .section-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
        font-size: 16px;
        cursor: pointer;
        border-bottom: 1px solid #e0e0e0;
        position: sticky;
        top: 0;
        z-index: 1000;
    }

    .section-content {
        padding: 15px;
        height: 500px;
        overflow-y: auto;
    }

    .blue-header {
        color: #1E88E5;
        background-color: #E3F2FD;
        padding: 5px 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        font-weight: bold;
    }

    .bullet-point {
        margin-left: 20px;
        margin-bottom: 10px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .emoji {
        font-size: 1.2em;
        margin-right: 6px;
    }

    .highlight {
        background-color: #fff8e1;
        padding: 5px;
        border-left: 3px solid #ffc107;
        margin: 10px 0;
    }

    .divider {
        margin: 15px 0;
        border-bottom: 1px dashed #e0e0e0;
    }

    .scroll-btn {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
    }

    .scroll-btn button {
        padding: 0.4rem 1rem;
        font-size: 14px;
        border: none;
        border-radius: 5px;
        background-color: #1E88E5;
        color: white;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for expandable sections and scroll buttons
st.markdown("""
<script>
function scrollDiv(divId, amount) {
    const div = document.getElementById(divId);
    if (div) div.scrollBy({ top: amount, behavior: 'smooth' });
}
</script>
""", unsafe_allow_html=True)

# --- Lese inn ekstern tekst fra filer ---
kategori_1 = Path("huskelapp.txt").read_text(encoding="utf-8")
kategori_2 = Path("forkortelser.txt").read_text(encoding="utf-8")
kategori_3 = Path("ovingsoppgaver.txt").read_text(encoding="utf-8")

# Create three columns layout
col1, col2, col3 = st.columns(3)

# First column - Huskelapp
with col1:
    with st.expander("📘 Huskelapp – Utvidet oversikt over sentrale nettverkskomponenter og konsepter", expanded=True):
        st.markdown('<div id="div1" class="section-content">' + kategori_1 + '</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="scroll-btn">
            
        </div>
        ''', unsafe_allow_html=True)

# Second column - Forkortelser
with col2:
    with st.expander("📘 Forkortelser i datakommunikasjon (INFT1007)", expanded=True):
        st.markdown('<div id="div2" class="section-content">' + kategori_2 + '</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="scroll-btn">
            
        </div>
        ''', unsafe_allow_html=True)

# Third column - Øvings-eksamen
with col3:
    with st.expander("📘 Øvings-eksamen i INFT1007: Datakommunikasjon", expanded=True):
        st.markdown('<div id="div3" class="section-content">' + kategori_3 + '</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="scroll-btn">
        
        </div>
        ''', unsafe_allow_html=True)

# Footer with instructions
st.markdown("---")
st.info("""
### Hvordan bruke denne appen:
1. Klikk på seksjonstitler for å utvide/skjule innholdet
2. Hver seksjon har egen scrollbar med opp/ned-knapper
3. Titlene forblir synlige når du scroller
4. Du kan enkelt kopiere tekst fra hver seksjon
""")

st.markdown("""
### Hvor du kan legge til ditt eget innhold:
For å oppdatere innholdet, rediger tekstfilene:
1. `huskelapp.txt`
2. `forkortelser.txt`
3. `ovingsoppgaver.txt`
""")
