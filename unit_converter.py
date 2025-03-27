import streamlit as st

st.title("Unit Converter")

conversion_type = st.selectbox("Choose conversion type", ("Length", "Weight"))

def convert_length(value, from_unit, to_unit):
    units_in_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Inches": 0.0254,
        "Feet": 0.3048
    }
    value_in_meters = value * units_in_meters[from_unit]
    return value_in_meters / units_in_meters[to_unit]

def convert_weight(value, from_unit, to_unit):
    units_in_kg = {
        "Kilograms": 1,
        "Grams": 0.001
    }
    value_in_kg = value * units_in_kg[from_unit]
    return value_in_kg / units_in_kg[to_unit]

if conversion_type == "Length":
    st.header("Length Converter")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit", ["Kilometers", "Meters", "Inches", "Feet"])
    to_unit = st.selectbox("To unit", ["Kilometers", "Meters", "Inches", "Feet"])

    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif conversion_type == "Weight":
    st.header("Weight Converter")
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From unit", ["Kilograms", "Grams"])
    to_unit = st.selectbox("To unit", ["Kilograms", "Grams"])

    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
