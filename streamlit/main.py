# %%
import streamlit as st
import roi, forecast_anomaly_detection,pcs

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["HOME", "CLV", "PCS", "ROI"])

if page == "HOME":
    forecast_anomaly_detection.main()
elif page == "CLV":
    # clv_model()
    pass
elif page == "PCS":
    pcs.main()
    # pcs_model()
    pass
elif page == "ROI":
    roi.main()
