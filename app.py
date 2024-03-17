import streamlit as st
import pandas as pd
import numpy as np
import joblib

def generate_energy_demand():
    hours = np.arange(24)
    demand = np.random.randint(100, 1000, size=24)  # Random demand values
    return pd.DataFrame({"Hour": hours, "Demand (MW)": demand})

# Function to load the trained decision tree model
def load_model():
    # Load your trained decision tree model here
    # For demonstration purposes, a dummy model is used
    model = joblib.load(r"C:\Users\Dell\Desktop\hackathon\models\modelRF.pkl")
    return model

# Function to predict using the trained model
def predict_output(model, input_data):
    prediction = model.predict([input_data])
    return prediction

# Function to get user input for input columns
def get_user_input():
    # Create input fields for the user to enter values for each input column
    input_values = []
    for i in ['temperature_2_m_above_gnd', 'relative_humidity_2_m_above_gnd',
       'mean_sea_level_pressure_MSL', 'total_precipitation_sfc',
       'snowfall_amount_sfc', 'total_cloud_cover_sfc',
       'high_cloud_cover_high_cld_lay', 'medium_cloud_cover_mid_cld_lay',
       'low_cloud_cover_low_cld_lay', 'shortwave_radiation_backwards_sfc',
       'wind_speed_10_m_above_gnd', 'wind_direction_10_m_above_gnd',
       'wind_speed_80_m_above_gnd', 'wind_direction_80_m_above_gnd',
       'wind_speed_900_mb', 'wind_direction_900_mb',
       'wind_gust_10_m_above_gnd', 'angle_of_incidence', 'zenith', 'azimuth']:
        input_value = st.text_input(f"Enter value for Input Column {i}", value="0")
        input_values.append(float(input_value))
    return input_values

def main():
    # Title and description for the app
    st.title("Smart Grid Management using AIML")
    st.markdown("Distribution of the energy based on the prediction ")
    user_input = st.slider("Adjust Demand (MW)", min_value=0, max_value=1000, value=500)
    # Load energy demand data (dummy data for demonstration)
    energy_demand_df = generate_energy_demand()

    # Placeholder for adjusting demand
    st.subheader("Real-Time Energy Distribution")
    st.markdown("Placeholder for adjusting demand and displaying predictions.")

    # Placeholder for hourly energy demand chart
    st.subheader("Hourly Energy Demand")
    st.line_chart(energy_demand_df.set_index("Hour"))

    # Display hourly demand DataFrame
    st.subheader("Hourly Demand DataFrame")
    st.write(energy_demand_df)

    # Placeholder for grid management content
    st.subheader("Power Generation Prediction")
    st.markdown("All the attributes effectes the power generation goes here")

    # Load the trained decision tree model
    model = load_model()

    # Get user input for input columns
    user_input = get_user_input()

    # Predicted output section
    st.subheader("Predicted Output")
    if st.button("Predict"):
        # Predict output using the model when "Predict" button is clicked
        predicted_output = predict_output(model, user_input)
        st.write(f"Predicted Output: {predicted_output}")

if __name__ == "__main__":
    main()
