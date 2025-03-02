import streamlit as st

# Set page configuration (must be before containers)
st.set_page_config(page_title="Vehicles", page_icon=":tada:", layout="wide")

# Title and description
st.title("Varieties of Car 🚗")
st.write("Transform your old vehicle into a new updated model!")
st.write("You can know more about me in the sidebar :point_left:")

# Main content container
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)  # Corrected columns to 2

    with left_column:
        st.header("What I Do")
       
        st.write("""
        1. Cars come in a wide range of varieties, each designed to suit different needs, preferences, and lifestyles. 
        2. SUVs and crossovers provide ample space and rugged capabilities, making them ideal for families and off-road enthusiasts. 
        3. Electric and hybrid vehicles are gaining popularity as eco-friendly options, offering sustainability without compromising on innovation.
        """)

        st.markdown("## Show some love! ❤️")

        # Social media buttons
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("Instagram"):
                st.markdown("[Follow us on Instagram](https://www.instagram.com)", unsafe_allow_html=True)
                
        with col2:
            if st.button("Facebook"):
                st.markdown("[Follow us on Facebook](https://www.facebook.com)", unsafe_allow_html=True)
        with col3:
            if st.button("Twitter 🦅"):
                st.markdown("[Follow us on Twitter](https://www.twitter.com)", unsafe_allow_html=True)
        with col4:
            if st.button("Website"):
                st.markdown("[Follow us on Facebook](https://www.elitecars.com)", unsafe_allow_html=True)
