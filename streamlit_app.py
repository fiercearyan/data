import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Navbar configuration
st.set_page_config(page_title="Navbar and Sidebar Demo", layout="wide")

# Add a navbar
with st.container():
    selected_nav = option_menu(
        menu_title="Main Menu",
        options=["Home", "About", "Contact"],
        icons=["house", "info-circle", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

# Add a sidebar for selection
st.sidebar.title("Select Data to View")
selection = st.sidebar.radio("Choose a Dataset:", ["Dataset 1", "Dataset 2", "Dataset 3"])

# Sample DataFrames
data1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
})

data2 = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": [1000, 500, 300],
    "Stock": [50, 200, 150]
})

data3 = pd.DataFrame({
    "Country": ["USA", "Canada", "Mexico"],
    "Population (M)": [331, 38, 126],
    "GDP (B$)": [21137, 1643, 1258]
})

# Display selected content in the main area
st.title(f"You selected: {selection}")
if selection == "Dataset 1":
    st.subheader("Dataset 1: User Information")
    st.table(data1)
elif selection == "Dataset 2":
    st.subheader("Dataset 2: Product Details")
    st.table(data2)
elif selection == "Dataset 3":
    st.subheader("Dataset 3: Country Statistics")
    st.table(data3)

# Handle navigation bar actions
if selected_nav == "About":
    st.sidebar.info("This app demonstrates navigation using a navbar and sidebar.")
    st.write("This is a demo application created using Streamlit.")
elif selected_nav == "Contact":
    st.sidebar.info("Contact us at support@example.com")
    st.write("Feel free to reach out!")
