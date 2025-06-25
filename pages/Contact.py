import streamlit as st

# Contact Information
st.header("Contact Information")
st.write("**Owner**: Nathan Rossow")
st.write("**Phone**: (507) 810-9226")
st.write("**Email**: contact@burstsoftware.com")  # Replace with actual email
st.write("**Website**: www.burstsoftware.com")    # Replace with actual website if available

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
