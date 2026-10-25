import streamlit as st

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction System")

st.markdown("Enter the details below to predict crop yield:")

# Inputs
area = st.number_input("Area (in hectares)", min_value=0.0, step=0.1)

crop_type = st.selectbox(
    "Crop Type",
    ["Wheat", "Rice", "Maize", "Sugarcane", "Cotton"]
)

ph = st.slider("Soil pH Value", 0.0, 14.0, 7.0)

soil_type = st.selectbox(
    "Soil Type",
    ["Clay", "Sandy", "Loamy", "Black Soil", "Red Soil"]
)

rainfall = st.number_input("Rainfall (in mm)", min_value=0.0, step=1.0)

# Button
if st.button("Predict Yield"):
    # Dummy prediction (replace with your ML model)
    predicted_yield = area * 2.5  

    st.success(f"🌱 Predicted Crop Yield: {predicted_yield:.2f} tons")