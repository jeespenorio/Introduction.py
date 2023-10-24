import streamlit as st
import pandas as pd
import locale


# Page 1: Home
def main_page():
    st.title("Automation Projects for GoodCo")
    st.write("Building an automation tool for GoodCo and streamlining various tasks.")
   

# Page 2: Upload and Analyze
def page_upload_and_analyze():
    st.title("Upload and Analyze Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, low_memory=False)
        # Add your analysis code here
# Page 3: About
def page_about():
    st.title("About")
    st.write("This is the about page.")
    # You can add information about your app or project here

# Create a dictionary to map page names to their corresponding functions
pages = {
    "Home": main_page,
    "Upload and Analyze": page_upload_and_analyze,
    "About": page_about,
   # "Dashboard": None,  # Placeholder for the dashboard page
}

# Check if "Dashboard" is selected and run the subprocess accordingly
selected_page = st.sidebar.radio("Select a page", list(pages.keys()))
pages[selected_page]()

