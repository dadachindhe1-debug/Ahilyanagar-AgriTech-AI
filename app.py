import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# १. वेब-ॲपचे शीर्षक आणि डिझाईन
st.set_page_config(page_title="Ahilyanagar Agri-Tech AI", page_icon="🌾")
st.title("🌾 Ahilyanagar Agri-Tech AI")
st.subheader("APMC Onion Market Price Predictor & Farmer Advisor")
st.write("Adjust the sliders below to predict onion prices based on supply and weather conditions.")

# २. मशीन लर्निंग मॉडेल ट्रेनिंग
market_data = np.array((
    (5000, 2),
    (4000, 4),
    (3000, 5),
    (2000, 7),
    (1500, 9)
))
onion_prices = np.array((1200, 1800, 2400, 3200, 4000))

ai_model = LinearRegression()
ai_model.fit(market_data, onion_prices)

# ३. वेब-ॲपवर सुंदर स्लायडर्स (Sliders) तयार करणे
st.sidebar.header("Market Inputs")
supply = st.slider("Expected Onion Supply (in Quintals)", min_value=1000, max_value=6000, value=2500, step=100)
rain_impact = st.slider("Rain / Weather Impact Scale (1 = Low, 10 = High)", min_value=1, max_value=10, value=5)

# ४. बटण दाबल्यावर निकाल दाखवणे
if st.button("Predict Market Price 🚀"):
    test_input = np.array(((supply, rain_impact),))
    predicted_price = round(float(ai_model.predict(test_input).item()), 2)
    
    st.markdown("---")
    st.metric(label="AI Predicted Onion Price", value=f"₹ {predicted_price} / Quintal")
    
    if predicted_price >= 3000:
        st.success("✅ AI Advice: High market demand! Best time to sell your harvest for maximum profit.")
    elif predicted_price >= 2000:
        st.warning("⚠️ AI Advice: Moderate market price. You can sell partially or monitor for a few days.")
    else:
        st.error("🛑 AI Advice: Low price alert! Consider storing the onions until supply drops.")
