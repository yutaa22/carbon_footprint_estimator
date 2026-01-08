import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load model and encoder
model = joblib.load("carbon_model.pkl")
encoder = joblib.load("diet_encoder.pkl")

st.title("🌱 Carbon Footprint Estimator")
st.write("Estimate your monthly carbon footprint using AI")

# User inputs
electricity = st.slider("Monthly Electricity Usage (kWh)", 50, 500, 150)
fuel = st.slider("Monthly Fuel Usage (liters)", 0, 100, 20)
transport = st.slider("Public Transport Distance (km)", 0, 300, 50)
diet = st.selectbox("Diet Type", ["veg", "mixed", "non-veg"])

# Encode diet
diet_encoded = encoder.transform([diet])[0]

# Predict button
if st.button("Calculate Carbon Footprint"):
    input_data = np.array([[electricity, fuel, transport, diet_encoded]])
    prediction = model.predict(input_data)[0]
    st.subheader(f"Estimated Carbon Footprint: {prediction:.2f} kg CO₂ / month")

    if prediction < 250:
        st.success("Low Carbon Footprint.. Keep it up!")
        st.write("🌱 Suggestions:")
        st.write("- Continue using energy-efficient appliances")
        st.write("- Prefer public transport and cycling")
    
    elif prediction < 450:
        st.warning("Medium Carbon Footprint")
        st.write("🌱 Suggestions:")
        st.write("- Reduce electricity usage (LEDs, turn off unused devices)")
        st.write("- Use public transport more often")
        st.write("- Reduce fuel consumption")
    
    else:
        st.error("High Carbon Footprint!!")
        st.write("🌱 Suggestions:")
        st.write("- Switch to renewable energy if possible")
        st.write("- Reduce private vehicle usage")
        st.write("- Try more plant-based meals")

    # chart1
    st.subheader("Carbon Footprint Comparison")

    chart_data = pd.DataFrame({
    "Category": ["Your Footprint", "Recommended Limit"],
    "CO₂ (kg/month)": [prediction, 250]
   })

    fig, ax = plt.subplots()

    colors = ["green", "orange"]
    ax.bar(chart_data["Category"], chart_data["CO₂ (kg/month)"], color=colors)

    ax.set_ylabel("CO₂ (kg/month)")
    ax.set_title("Carbon Footprint Comparison")

    st.pyplot(fig)


    # chart2
    st.subheader("Usage Overview")

    usage_data = pd.DataFrame({
    "Factor": ["Electricity (kWh)", "Fuel (liters)", "Transport (km)"],
    "Value": [electricity, fuel, transport]
   })

    #st.bar_chart(usage_data.set_index("Factor"))
    fig2, ax2 = plt.subplots()

    usage_colors = ["blue", "red", "purple"]
    ax2.bar(usage_data["Factor"], usage_data["Value"], color=usage_colors)

    ax2.set_ylabel("Usage Value")
    ax2.set_title("Energy & Transport Usage")

    st.pyplot(fig2)





    