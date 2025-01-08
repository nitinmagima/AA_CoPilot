import streamlit as st


def main():
    # Page Title
    st.title("Defining Risk and Establishing A Crisis Timeline")

    # Call to Action
    st.info("Use this page to understand risk and establish timelines for effective anticipatory actions.")

    # Section: Defining Risk
    st.header("Defining Risk")
    st.markdown("""
    Risk is best thought of as a function of:
    1. **Hazard:** The probability of occurrence of a threat (e.g., drought).
    2. **Exposure:** The location, attributes, and value of assets that could be affected.
    3. **Vulnerability:** The degree of susceptibility of the exposed elements based on physical, social, economic, and environmental conditions.

    **Key Types of Drought:**
    - **Meteorological Drought:** A period of below-average precipitation compared to normal conditions.
    - **Agricultural Drought:** A shortage of water impacting crops and livestock.
    - **Hydrological Drought:** Low levels of surface and groundwater, such as in streams or reservoirs.
    """)

    # Add a Diagram for Types of Drought
    st.image("pages/images/4.png", caption="Types of Drought",
             use_container_width=True)

    # Section: Establishing A Crisis Timeline
    st.header("Establishing A Crisis Timeline")
    st.markdown("""
    A crisis timeline defines windows of opportunity for anticipatory actions. It helps identify:
    - **Predictive Windows:** When forecasts are generated (e.g., seasonal forecasts).
    - **Observational Windows:** When drought effects are measured on the ground.

    **Key Steps to Create a Crisis Timeline:**
    - Overlay drought forecasts with agricultural calendars to determine impact windows.
    - Identify specific indicators to monitor drought risk and activate anticipatory actions.

    **Challenges:**
    - Slow-onset hazards like drought make it difficult to pinpoint turning points.
    - Data availability may vary across spatial and temporal scales.

    **Technical Questions for Decision-Makers:**
    1. What seasons are most suitable for anticipatory actions?
    2. How does the slow onset of drought affect the timing of actions?
    3. What lead times and spatial scales should be considered?
    4. What are the critical parameters for operational development (e.g., dry spell frequency)?
    """)

# Add a copyright line at the bottom of the page
    st.markdown(
    "<div style='text-align: center; margin-top: 50px; font-size: 12px; color: gray;'>"
    "© The National Center for Disaster Preparedness (NCDP) Columbia Climate School, at Columbia University. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
