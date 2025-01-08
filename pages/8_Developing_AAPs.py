import streamlit as st


def main():
    # Page Title
    st.title("Developing Anticipatory Action Plans (AAPs)")

    # Call to Action
    st.info(
        "This page provides guidance on how to develop an anticipatory action plan to ensure effective disaster response.")

    # Section: Introduction
    st.header("Introduction")
    st.markdown("""
    Anticipatory Action Plans (AAPs) are standard protocols that guide the implementation of anticipatory actions (AAs).
    They link hazard thresholds and triggers to specific actions, timelines, and costs. A well-designed AAP ensures:
    - Timely activation of AAs.
    - Effective resource allocation.
    - Clear roles and responsibilities for stakeholders.
    """)

    # Section: Key Components of AAPs
    st.header("Key Components of AAPs")
    st.markdown("""
    An effective AAP includes:
    - **Hazard Thresholds and Triggers:** Defined levels of risk that activate actions.
    - **Anticipatory Actions:** Predefined interventions tailored to the expected hazard.
    - **Timelines:** Detailed schedules for readiness and activation phases.
    - **Budgets:** Estimated costs for each action and the overall plan.
    - **Roles and Responsibilities:** Clear assignment of tasks to stakeholders.
    """)

    # Add Diagram: AAP Core Components
    st.image("pages/images/1.png", caption="Core Components of Anticipatory Action Plans",
             use_container_width=True)

    # Section: Steps to Develop AAPs
    st.header("Steps to Develop AAPs")
    st.markdown("""
    **1. Define Hazard Thresholds and Triggers:**
    - Use historical data and predictive models to identify thresholds.
    - Align triggers with forecast lead times for timely activation.

    **2. Design Anticipatory Actions:**
    - Tailor actions to the specific hazard (e.g., cash transfers, health supplies).
    - Ensure actions are time-bound and cost-effective.

    **3. Establish Timelines:**
    - Map out readiness and activation phases.
    - Identify key windows of opportunity for intervention.

    **4. Allocate Resources and Define Budgets:**
    - Estimate the cost of each action and the overall plan.
    - Ensure pre-arranged financing mechanisms are in place.

    **5. Assign Roles and Responsibilities:**
    - Engage stakeholders in the planning process.
    - Clearly define tasks for government agencies, NGOs, and other partners.
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
