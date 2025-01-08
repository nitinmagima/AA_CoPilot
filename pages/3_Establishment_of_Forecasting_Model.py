import streamlit as st


def main():
    # Page Title
    st.title("Establishment of the Forecasting Model for Anticipatory Actions")

    # Call to Action
    st.info(
        "This page highlights the importance of forecasting models and helps users understand how to link forecasts to anticipatory actions effectively.")

    # Section: Introduction
    st.header("Introduction")
    st.markdown("""
    The establishment of a forecasting model is crucial for linking anticipatory actions (AA) to actionable triggers. 
    This involves selecting reliable forecasts, setting thresholds, and defining triggers that activate interventions at the right time.
    """)

    # Section: Selecting Forecasts for AA
    st.header("Selecting Forecasts for AA")
    st.markdown("""
    It is important to identify early warning information that is:
    - **Timely:** Available at critical points before hazards materialize.
    - **Accurate:** Providing reliable forecasts for the relevant area and timescale.
    - **Comprehensive:** Including a mix of probabilistic precipitation, agricultural drought, and seasonal observation indicators.

    Examples of relevant indicators include:
    - Probabilistic precipitation forecasts.
    - Vegetation health indices (e.g., NDVI).
    - Seasonal observation indicators such as SPI (Standardized Precipitation Index).
    """)


    # Section: Peer Review Framework
    st.header("Peer Review Framework")
    st.markdown("""
    OCHA has introduced a Peer Review Framework to support decision-makers in evaluating predictive models. 
    This framework assesses:
    1. **Technical Rigor:** Evaluates accuracy, hit rate, and miss rate of forecasts.
    2. **Operational Readiness:** Checks data availability, lead time, and implementation feasibility.
    3. **Ethical Concerns:** Considers biases, false positives, and negative consequences of forecasts.

    **Framework Steps:**
    - **Model Submission:** Create a report documenting forecast parameters and methodologies.
    - **Technical Review:** Assess spatial resolution, geographic scope, and accuracy.
    - **Implementation Plan Submission:** Outline activities and funding for the trigger mechanism.
    - **Ethical Review:** Identify potential biases and assess risks.
    """)

    # Add Table: Peer Review Framework
    st.markdown("""
    | Step                      | Output                       | Roles                          |
    |---------------------------|------------------------------|--------------------------------|
    | Model Submission          | Model Card                  | Client, Moderator              |
    | Technical Review          | Evaluation Matrix           | Client, Moderator, Reviewer    |
    | Implementation Plan       | Implementation Card         | Client, Moderator              |
    | Ethical Review            | Ethical Matrix              | Client, Moderator, Ethical Reviewer |
    """)

    # Section: Key Factors for Forecasting
    st.header("Key Factors for Forecasting")
    st.markdown("""
    Key factors for forecasting models include:
    - **Location:** Focus on regions most prone to hazards.
    - **Forecast Lead Times:** Consider appropriate lead times for operational readiness.
    - **Accuracy:** Use historical data to validate forecast accuracy.

    **Questions for Decision-Makers:**
    1. What forecasts are being used, and when will they be issued?
    2. What is the resolution and accuracy of the selected forecasts?
    3. What is the uncertainty between different climate models?
    """)

    # Add Figure: Example Timeline for Forecast Triggers
    st.image("pages/images/2.png", caption="Example Timeline for Forecast Triggers",
             use_container_width=True)  # Replace with the actual image path

# Add a copyright line at the bottom of the page
    st.markdown(
    "<div style='text-align: center; margin-top: 50px; font-size: 12px; color: gray;'>"
    "© The National Center for Disaster Preparedness (NCDP) Columbia Climate School, at Columbia University. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
