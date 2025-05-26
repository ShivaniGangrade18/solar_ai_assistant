import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")
st.title("🔆 Solar Industry AI Assistant")
st.write("Upload a rooftop image to get a smart solar panel suitability analysis.")

@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip_model()

uploaded_file = st.file_uploader("📸 Upload a rooftop image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    with st.spinner("Analyzing image..."):
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        description = processor.decode(out[0], skip_special_tokens=True)

    st.subheader("📊 AI Interpretation of Rooftop")
    st.markdown(f"**Visual Description:** {description}")

    st.subheader("🧠 Solar Panel Suitability (Simulated)")
    if "flat roof" in description or "top" in description or "building" in description:
        st.success("✅ Suitable for solar panel installation.")
        st.markdown("""
        - Estimated Solar Output: **450–600 kWh/month**
        - Suggested Panel Layout: **10 panels (300W each)**
        - Cost Estimate: **₹1.5–2 lakhs**
        - Expected Payback Period: **3–4 years**
        """)
    else:
        st.warning("⚠️ Not enough visual data to confirm rooftop structure suitability.")
