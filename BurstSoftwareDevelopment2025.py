import streamlit as st

# Set page configuration for better appearance
st.set_page_config(
    page_title="Burst Software Development",
    page_icon="💻",
    layout="centered",
)

# Header Section
st.title("Burst Software Development")
st.subheader("Custom Software Solutions for Your Business")
st.markdown("---")

# Business Information
st.header("About Us")
st.write(
    """
    Welcome to **Burst Software Development**! We specialize in delivering high-quality, 
    custom software solutions with a particular expertise in **Streamlit applications**. 
    Our team builds interactive, user-friendly, and data-driven web apps tailored to your 
    business needs. With a focus on innovation and reliability, we help you achieve your 
    goals through cutting-edge technology.
    """
)

# Services Section
st.header("Our Services")
st.write(
    """
    At Burst Software Development, we excel in creating **Streamlit apps** that empower 
    businesses with dynamic, data-driven solutions. Our services include:
    - **Custom Streamlit App Development**: Build interactive dashboards and web apps.
    - **Data Visualization Solutions**: Transform data into actionable insights.
    - **Web and Mobile App Development**: Comprehensive software solutions for all platforms.
    - **Consulting & Support**: Expert guidance to bring your ideas to life.
    """
)

# Contact Information
st.header("Contact Information")
st.write("**Owner**: Nathan Rossow")
st.write("**Phone**: (507) 810-9226")
st.write("**Email**: burstsoftwaredevelopment@gmail.com")  # Replace with actual email

# Business Hours
st.header("Business Hours")
st.write("**Sunday - Friday**: 7:00 AM - 4:00 PM Central Time")
st.write("**Closed**: Saturday")

# Call to Action
st.markdown("---")
st.subheader("Get in Touch!")
st.write(
    """
    Ready to elevate your business with a custom **Streamlit app** or other software solution? 
    Contact us today to discuss your project!
    """
)
if st.button("Contact Us"):
    st.write("Please call (507) 810-9226 or email contact@burstsoftware.com to get started!")

# Footer
st.markdown("---")
st.write("© 2025 Burst Software Development. All rights reserved.")
