import streamlit as st

# Function to display the homepage
def homepage():
    # Center the title using markdown
    st.markdown("<h1 style='text-align: center;'>AgroEndure Dashboard</h1>", unsafe_allow_html=True)

    # CSS to style the buttons with white background, outline, and smaller font
    st.markdown(
        """
        <style>
        .stButton>button {
            padding: 30px;  /* Smaller padding for smaller buttons */
            font-size: 24px;  /* Smaller font size */
            font-weight: bold;  /* Bold text */
            background-color: white;  /* White background */
            color: #333;  /* Dark text color */
            border: 3px solid #333;  /* Dark border (outline) */
            border-radius: 20px;  /* Rounded corners for a modern look */
            width: 100%;  /* Button takes up full width of the column */
            height: 150px;  /* Smaller height for smaller buttons */
            transition: all 0.3s ease;  /* Smooth transition for hover effect */
        }
        .stButton>button:hover {
            background-color: #f0f0f0;  /* Light gray background on hover */
            border-color: #555;  /* Darker border on hover */
        }
        .stColumns>div {
            padding: 10px;  /* Add space between buttons */
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Creating a layout with four clickable buttons (links)
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(f'<a href="Disease_Detection" target="_blank"><button style="font-size: 24px; padding: 30px; width: 100%; height: 150px; background-color: white; border: 3px solid #333; border-radius: 20px; font-weight: bold; text-align: center; display: flex; justify-content: center; align-items: center; color: #333;">🔧 **Disease Detection**</button></a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="PH_Value" target="_blank"><button style="font-size: 24px; padding: 30px; width: 100%; height: 150px; background-color: white; border: 3px solid #333; border-radius: 20px; font-weight: bold; text-align: center; display: flex; justify-content: center; align-items: center; color: #333;">🌱 **pH Value**</button></a>', unsafe_allow_html=True)

    col3, col4 = st.columns(2, gap="large")
    with col3:
        st.markdown(f'<a href="Crop_Budgeting" target="_blank"><button style="font-size: 24px; padding: 30px; width: 100%; height: 150px; background-color: white; border: 3px solid #333; border-radius: 20px; font-weight: bold; text-align: center; display: flex; justify-content: center; align-items: center; color: #333;">💧 **Crop Budgeting**</button></a>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<a href="Crop_Recommendation" target="_blank"><button style="font-size: 24px; padding: 30px; width: 100%; height: 150px; background-color: white; border: 3px solid #333; border-radius: 20px; font-weight: bold; text-align: center; display: flex; justify-content: center; align-items: center; color: #333;">🌾 **Crop Recommendation**</button></a>', unsafe_allow_html=True)

# Initialize the page state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Check the state to navigate to the homepage
if st.session_state.page == "home":
    homepage()
