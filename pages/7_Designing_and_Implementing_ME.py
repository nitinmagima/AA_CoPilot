import streamlit as st

def main():
    # Page Title
    st.title("Designing and Implementing M&E for Anticipatory Actions")

    # Call to Action
    st.info(
        "This page highlights the importance of designing robust M&E frameworks for anticipatory actions to improve them over time.")

    # Section: Introduction
    st.header("Introduction")
    st.markdown("""
    Monitoring and Evaluation (M&E) are essential components of the anticipatory action (AA) framework. 
    They ensure that:
    - Anticipatory actions are effectively implemented.
    - The impact on targeted populations is assessed.
    - Lessons learned are used to refine future interventions.
    """)

    # Section: Trigger Evaluation
    st.header("Trigger Evaluation")
    st.markdown("""
    Evaluating the performance of triggers is a critical part of the M&E process. This involves:
    - Assessing whether the triggers correctly anticipated the hazard.
    - Measuring the accuracy, hit rate, and false positives/negatives of forecasts.
    - Adjusting thresholds and trigger mechanisms based on results.

    **Key Steps:**
    1. Document triggers and associated actions.
    2. Compare forecasted and observed conditions during the trigger period.
    3. Conduct post-activation reviews to assess decision-making effectiveness.
    """)

    # Section: Evaluating Impact on Targeted Populations
    st.header("Evaluating Impact on Targeted Populations")
    st.markdown("""
    The impact evaluation process focuses on understanding how AAs affected vulnerable populations. This includes:
    - Measuring changes in food security, livelihoods, or health outcomes.
    - Comparing outcomes in areas where AAs were implemented versus where they were not.
    - Engaging stakeholders to validate findings.

    **Steps for Impact Evaluation:**
    1. Define clear metrics (e.g., reduction in food insecurity levels).
    2. Collect baseline and post-intervention data.
    3. Analyze data to assess outcomes and identify areas for improvement.
    """)

    # Section: Tools and Templates
    st.header("Tools and Templates for M&E")
    st.markdown("""
    To streamline the M&E process, tools and templates can be used for:
    - Monitoring: Dashboards for tracking forecasts, triggers, and actions in real-time.
    - Evaluation: Standardized forms for data collection and analysis.
    - Reporting: Templates for presenting findings to stakeholders.
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
