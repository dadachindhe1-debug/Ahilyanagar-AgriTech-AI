import numpy as np
from sklearn.linear_model import LinearRegression

# Ahilyanagar Agri-Tech AI: Onion Price Predictor & Advisor
# Historical market data: (Supply in Quintals, Rain/Weather Impact 1-10)
market_data = np.array((
    (5000, 2),
    (4000, 4),
    (3000, 5),
    (2000, 7),
    (1500, 9)
))

# Historical onion prices (Rs per Quintal)
onion_prices = np.array((1200, 1800, 2400, 3200, 4000))

# Train the Machine Learning model
ai_model = LinearRegression()
ai_model.fit(market_data, onion_prices)

print("--- Ahilyanagar Agri-Tech AI: Onion Price Predictor & Advisor ---")
supply = float(input("Enter expected onion supply in quintals (e.g., 1500 to 5000): "))
rain_impact = float(input("Enter rain/weather impact scale (1 to 10): "))

# Predict future price
test_input = np.array(((supply, rain_impact),))
predicted_price = round(float(ai_model.predict(test_input).item()), 2)

print("---------------------------------")
print("AI Predicted Onion Price:", predicted_price, "Rs / Quintal")

# AI Decision Engine for Farmers
if predicted_price >= 3000:
    print("AI Advice: High market demand! Best time to sell your harvest for maximum profit.")
elif predicted_price >= 2000:
    print("AI Advice: Moderate market price. You can sell partially or monitor for a few days.")
else:
    print("AI Advice: Low price alert! Consider storing the onions until supply drops.")
