import streamlit as st

def main():
    # Page Title
    st.title("Development of Anticipatory Action Interventions")

    # Call to Action
    st.info(
        "This page highlights the development of anticipatory action interventions and their integration into social protection systems.")

    # Section: Introduction
    st.header("Introduction")
    st.markdown("""
    Anticipatory actions (AAs) are interventions designed to mitigate the severity of a predicted hazard or shock. 
    These actions aim to:
    - Provide support to at-risk populations before the disaster materializes.
    - Reduce humanitarian costs and protect livelihoods.
    - Enhance community resilience to disasters like droughts.
    """)

    # Section: Setting Anticipatory Actions
    st.header("Setting Anticipatory Actions")
    st.markdown("""
    Anticipatory actions can be implemented at various levels:
    - **Household Level:** Provide cash transfers to allow families to buy essentials or evacuate.
    - **Community Level:** Maintain critical infrastructure like irrigation systems and health clinics.
    - **Regional/National Level:** Ensure the availability of key services such as clean water and electricity.

    **Examples of Anticipatory Actions:**
    - Distribution of drought-resistant seeds to farmers.
    - Maintenance of critical irrigation infrastructure.
    - Provision of cash transfers to affected households.
    - Health supplies for drought-related illnesses.
    """)

    # Section: Integration with Social Protection Programs
    st.header("Integration with Social Protection Programs")
    st.markdown("""
    To scale anticipatory actions effectively, they should leverage existing social protection systems. This ensures:
    - **Rapid Implementation:** By using existing delivery mechanisms like payment systems.
    - **Wide Coverage:** Reaching large segments of vulnerable populations.
    - **Cost-Effectiveness:** Avoiding duplication of resources and efforts.

    **Key Steps for Integration:**
    1. Assess feasibility of integration into social protection systems.
    2. Establish governance structures for joint decision-making.
    3. Design anticipatory action plans that align with social protection systems.
    4. Activate anticipatory actions once triggers are met.
    5. Evaluate the impact and incorporate lessons learned.
    """)

    # Section: Characteristics of Anticipatory Actions
    st.header("Key Characteristics of Anticipatory Actions")
    st.markdown("""
    Effective anticipatory actions share the following characteristics:
    - **Time-Bound:** Executed during the critical window between early warning and disaster impact.
    - **Protective Intent:** Focused on mitigating impacts and reducing vulnerabilities.
    - **Evidence-Based:** Guided by historical data and forecasts.
    - **Scalable:** Designed to be implemented at local, regional, and national levels.
    """)


if __name__ == "__main__":
    main()
