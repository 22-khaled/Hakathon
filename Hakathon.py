import streamlit as st
from streamlit_bmc import st_bmc
st.set_page_config(
page_title="",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded"
)
tab1, tab2 = st.tabs(["Bussiness Model Canvas", "Bussiness Plan"])

with tab1:


    # Spawn a new MBC editor
    # Re-generate your JSON data
    data = {
        "visual": {
            "company_name": "Less is Green"
        },
        "key_partners": {
            "cards": [
                { "id":"1", "text": "Real Estate Companies" },
                { "id":"2", "text": "Technical boards providers" }
            ]
        },
        "key_activities": {
            "cards": [
                { "id":"1", "text": "Application & Smart system Development" },
                { "id":"2", "text": "Continued feedback with customers" },
                { "id":"3", "text": "Provide online and in-face consulatations" }
            ]
        },
        "key_resources": {
            "cards": [
                { "id":"1", "text": "Mobile Application" },
                { "id":"2", "text": "Technical Engineers and Skilled labor" },
                { "id":"3", "text": "Consulatations providers" },
                
            ]
        },
        "value_propositions": {
            "cards": [
                { "id":"1", "text": "Exploitation of spaces" },
                { "id":"2", "text": "Providing Free Consulatations" },
                { "id":"3", "text": "Advanced-Technical Smart Homes" }
            ]
        },
        "customer_relationship": {
            "cards": [
                { "id":"1", "text": "Online (Application)" },
                { "id":"2", "text": "In person relationships" }
            ]
        },
        "channels": {
            "cards": [
                { "id":"1", "text": "Mobile Applcation" },
                { "id":"2", "text": "Social media" },
                { "id":"3", "text": "Personal relationships"}
            ]
        },
        "customer_segments": {
            "cards": [
                { "id":"1", "text": "Companies and offices owners" },
                { "id":"2", "text": "Real estate owners and contracting companies" },
                { "id":"3", "text": "Oweners of rental departments" }
            ]
        },
        "cost_structure": {
            "cards": [
                { "id":"1", "text": "Application development" },
                { "id":"2", "text": "Marketing" },
                { "id":"3", "text": "Technical boards" },
                { "id":"4", "text": "Employees salaries" },
            ]
        },
        "revenue_streams": {
            "cards": [
                { "id":"1", "text":"Smart Homes Installation works"},
                { "id":"2", "text": "Spcaes Exploitations works" },
                { "id":"3", "text": "Premium Consultations (2nd & 3rd phase)" },
                { "id":"4", "text": "Partnerships" },
                
            ]
        }
    }

    # binding into model
    st_bmc(data)
with tab2:
    st.title("Bussiness Plan")
    cols = st.columns(spec=3, gap="Large")
    with cols[0]:
        st.image("What How.png")
        st.subheader("What do we do?")
        st.subheader("How do we do it?")
        st.subheader("Who do we serve")
    with cols[1]:
        st.image("wHY.png")
        st.subheader("Define customer problem")
        st.subheader("Define solution provided")
    with cols[2]:
        st.image("Revenue.png")
        st.subheader("Pricing + Billing startigies ")
        st.subheader("Income streams")
    
    cols1 = st.columns(spec=3, gap="Large")
    with cols1[0]:
        st.image("Marketing.png")
        st.subheader("Customer reach strategy")
        st.subheader("Referral generation strategy")
    with cols1[1]:
        st.image("Competition.png")
        st.subheader("Top competitors")
        st.subheader("Our competitive advantage")
    with cols1[2]:
        st.image("Metrics.png")
        st.subheader("Millestone 1")
        st.subheader("Millestone2")