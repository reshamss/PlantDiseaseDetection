import streamlit as st
from PIL import Image
from predict import predict
import base64

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# -----------------------------
# LOAD BACKGROUND IMAGE
# -----------------------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("assets/bg.png")

# -----------------------------
# CSS
# -----------------------------
st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.main-box {{
    background: rgba(255,255,255,0.88);
    padding:30px;
    border-radius:20px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}}

.title {{
    text-align:center;
    color:#1B5E20;
    font-size:48px;
    font-weight:bold;
}}

.subtitle {{
    text-align:center;
    font-size:20px;
    color:#444;
    margin-bottom:20px;
}}

.result-card {{
    background:#E8F5E9;
    padding:25px;
    border-radius:20px;
    border:3px solid #2E7D32;
    text-align:center;
}}

.disease {{
    color:#C62828;
    font-size:42px;
    font-weight:900;
}}

.confidence {{
    color:#0D47A1;
    font-size:32px;
    font-weight:bold;
}}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# MAIN CONTAINER
# -----------------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌿 Plant Disease Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload a plant leaf image to detect diseases using Artificial Intelligence</div>',
    unsafe_allow_html=True
)

uploaded = st.file_uploader(
    "📤 Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded:

    image = Image.open(uploaded)

    col1, col2 = st.columns([1,1])

    with col1:

        st.image(
            image,
            caption="Uploaded Leaf",
            use_container_width=True
        )

    with col2:

        disease, confidence = predict(image)

        disease = disease.replace("___", " - ")
        disease = disease.replace("_", " ")

        st.markdown(
            f"""
            <div class="result-card">

            <h2>🌱 Disease Prediction</h2>

            <div class="disease">
            {disease}
            </div>

            <br>

            <div class="confidence">
            🎯 Confidence: {confidence*100:.2f}%
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.progress(int(confidence*100))

st.markdown("</div>", unsafe_allow_html=True)