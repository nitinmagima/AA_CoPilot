import streamlit as st

def main():
    # Page Title
    st.title("Associating Anticipatory Actions with Predictive Models")

    # Call to Action
    st.info("This page highlights how to link predictive models to anticipatory actions.")

    # Section: Historical Data and Model Validation
    st.header("Using Historical Data for Validation")
    st.markdown("""
    Historical data is essential to validate forecasts and define triggers. This process involves:
    - Identifying "bad years" or periods of significant humanitarian impact (e.g., droughts).
    - Ranking historical events by severity to inform thresholds for action.
    - Evaluating forecast accuracy using metrics such as hit rate and false positives.

    **Steps for Historical Data Validation:**
    1. Collect historical data on hazards, impacts, and vulnerabilities.
    2. Identify years with significant impacts using participatory processes.
    3. Define thresholds for severity levels (e.g., mild, moderate, severe).
    """)

    # Section: Linking Predictive Models to Actions
    st.header("Linking Predictive Models to Anticipatory Actions")
    st.markdown("""
    **Process:**
    1. **Data Selection:** Identify the relevant parameters (e.g., precipitation, vegetation indices).
    2. **Define Triggers:** Establish thresholds for readiness and activation phases.
    3. **Action Mapping:** Assign specific anticipatory actions to each severity level.

    **Example:**
    - **Mild Drought:** Distribute drought-resistant seeds and conduct awareness campaigns.
    - **Severe Drought:** Provide cash transfers and scale up health interventions.
    """)

    # Timing of Anticipatory Actions
    st.image("pages/images/3.png", caption="Timing of Anticipatory Actions",
             use_container_width=True)

    # Section: Key Features of Effective Models
    st.header("Key Features of Effective Predictive Models")
    st.markdown("""
    Predictive models for anticipatory actions should have the following features:
    - **Data Quality:** Use high-quality and complete datasets for accuracy.
    - **Forecast Skill:** Balance forecast accuracy with lead times to enable timely action.
    - **Operational Feasibility:** Ensure the model can be applied in real-time scenarios.
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
