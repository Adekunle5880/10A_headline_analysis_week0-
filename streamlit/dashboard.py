import streamlit as st
import pandas as pd

# Load data from Task 1 and Task 2
task1_data = pd.read_csv("notebooks/headline_analysis.ipynb")
task2_data = pd.read_csv("/Users/expert/Desktop/10-Academy-Week0/data/domains_location.csv")

# Sidebar
st.sidebar.title("Dashboard Navigation")
page = st.sidebar.radio("Go to", ["Task 1 Results", "Task 2 Results"])

# Main content
st.title("Dashboard")

if page == "Task 1 Results":
    st.header("Task 1: Analysis of News Headlines")
    # Display Task 1 results
    st.write(task1_data)

elif page == "Task 2 Results":
    st.header("Task 2: Modeling and Analysis")
    # Display Task 2 results
    st.write(task2_data)

# Additional Streamlit components can be added as needed (e.g., plots, charts, interactive widgets)
