import streamlit as st

# Projects Page
st.header("Our Projects")
st.write(
    """
    At **Burst Software Development**, we take pride in delivering innovative and impactful 
    software solutions, with a special focus on **Streamlit applications**. Below are some 
    of our recent projects that showcase our expertise in creating interactive, data-driven 
    web apps.
    """
)

# Project 1
st.subheader("Project 1: Sales Dashboard")
st.write(
    """
    **Description**: Developed a custom Streamlit app for a retail client to visualize 
    sales performance across multiple regions. The dashboard features interactive charts, 
    real-time data updates, and user-friendly filters.
    - **Technologies**: Streamlit, Pandas, Plotly
    - **Impact**: Improved decision-making by providing actionable insights.
    """
)

# Project 2
st.subheader("Project 2: Healthcare Analytics App")
st.write(
    """
    **Description**: Built a Streamlit-based analytics platform for a healthcare provider 
    to track patient outcomes and resource utilization. The app includes dynamic 
    visualizations and secure data handling.
    - **Technologies**: Streamlit, Python, Altair
    - **Impact**: Enhanced operational efficiency and patient care quality.
    """
)

# Project 3
st.subheader("Project 3: Financial Forecasting Tool")
st.write(
    """
    **Description**: Created a Streamlit app for a financial firm to model and forecast 
    investment scenarios. The tool offers interactive inputs and predictive analytics.
    - **Technologies**: Streamlit, NumPy, Scikit-learn
    - **Impact**: Streamlined investment planning processes.
    """
)

# Call to Action
st.markdown("---")
st.subheader("Want to See Your Project Here?")
st.write(
    """
    Have an idea for a custom **Streamlit app** or other software solution? Visit our 
    **Contact** page to discuss your project with us!
    """
)

# Footer
st.markdown("---")
st.write("© 2025 Burst Software Development. All rights reserved.")
