import streamlit as st


def main():
    # Page Title
    st.title("Activating the Monitoring System of Anticipatory Actions")

    # Call to Action
    st.info(
        "This page provides an overview of monitoring systems, communication strategies, and challenges for activating anticipatory actions.")

    # Section: Introduction
    st.header("Introduction")
    st.markdown("""
    Monitoring systems are essential to ensure that anticipatory actions (AAs) are triggered based on accurate forecasts and thresholds.
    Effective monitoring systems:
    - Enable real-time tracking of hazard developments.
    - Support decision-making for activation of anticipatory actions.
    - Ensure that triggers are met before implementing interventions.
    """)

    # Section: Monitoring Forecasts and Triggers
    st.header("Monitoring Forecasts and Triggers")
    st.markdown("""
    The monitoring system involves:
    - **Forecast Monitoring:** Regularly tracking key indicators such as rainfall, drought indices, and vegetation health.
    - **Threshold Validation:** Comparing forecasts against predefined thresholds for readiness and activation phases.
    - **Trigger Activation:** Ensuring that predefined triggers are met before initiating actions.

    **Key Steps:**
    1. Establish monitoring protocols for critical forecasts and observational data.
    2. Assign roles and responsibilities for monitoring, analysis, and communication.
    3. Use dashboards or automated systems to streamline the monitoring process.
    """)

    # Section: Communication Strategies
    st.header("Communication Strategies for Trigger Activation")
    st.markdown("""
    Effective communication is key to ensuring timely activation of AAs. This includes:
    - **Internal Communication:** Informing stakeholders within the organization about trigger activation and next steps.
    - **External Communication:** Notifying government agencies, humanitarian partners, and communities.
    - **Products and Channels:** Using dashboards, reports, and real-time alerts to disseminate information.

    **Key Activities:**
    - Regular updates on forecast and monitoring results.
    - Alert messages when thresholds are met.
    - Coordination meetings to review activation readiness.
    """)

if __name__ == "__main__":
    main()
