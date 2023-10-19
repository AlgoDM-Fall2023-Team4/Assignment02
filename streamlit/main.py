# %%
import streamlit as st
import roi

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["HOME", "CLV", "PCS", "ROI"])

if page == "CLV":
    # clv_model()
    pass
elif page == "HOME":
    # homepage()
    pass
elif page == "ROI":
    roi.main()
