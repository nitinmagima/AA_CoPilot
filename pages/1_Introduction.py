import streamlit as st


def main():
    st.title("Introduction")



    st.markdown("""
    
    Anticipatory Actions (AA) aim to prevent or reduce the impact of predicted imminent extreme weather events on at-risk populations linking forecast triggers to previously determined humanitarian actions. It requires defined actions and prearranged funding, by stakeholders and partners, to reach households or communities ahead of a forecasted weather shock. Actions such as cash, in-kind support such as food assistance, and early warning messaging can be implemented in the critical window between a forecast and an extreme weather event to reduce its impact on vulnerable populations, save lives and protect livelihoods.
    
    The anticipatory action system seeks to complement rather than replace other risk management activities, including disaster risk reduction, preparedness, and early action. In protracted crises, where emergency preparedness, response, and recovery are already ongoing, this program works in complementarity to address new risks predicted to impact vulnerable communities1.
    
    """)

    # Add Disaster Risk Reduction Process Example
    st.image("pages/images/5.png", caption="Disaster Risk Reduction Process",
             use_container_width=True)

    # Add Different Disaster Relief Mechanisms Example
    st.image("pages/images/6.png", caption="Different Disaster Relief Mechanisms",
             use_container_width=True)

    st.markdown("""
    Key Definitions
    
    - **Frequency/Return Period**: Description for an extreme weather event: “once in N years.” Return periods are not a literal count of the years that have passed between similarly extreme events, nor are they a guarantee that a given number of years will pass before a similar event happens again. E.g., once in a 2-year drought (50% frequency)/ once in a 5-year drought (20% frequency)/ once in a 10-year drought (10% frequency).
    - **Threshold**: Thresholds are defined for each severity level (Eg - Mild, Moderate, and Severe) for the hazard using the concept of frequency or return period.
    - **Trigger**: A trigger defines a set of conditions for a particular threshold, which, upon being met, enables the release of pre-arranged funds for the immediate commencement of pre-agreed anticipatory activities. Each anticipatory action pilot involves setting up a trigger mechanism that corresponds directly to the hazard(s) expected to emerge in a given region. Triggers can be ‘hard’, relying on objectively verified data, or ‘soft’, including an element of discretion.
    - **Predictive Trigger**: A type of trigger that is forecast-informed and based on the probability of the shock event occurring. The anticipatory activities are activated if the pre-specified probability threshold is met/surpassed.
    - **Observational Trigger**: A type of trigger based on measures capturing observable facts, such as a shock has occurred. If the specific threshold for this event is met/surpassed, then the anticipatory activities are activated.
    - **Predictive Model**: Projects may choose from various types of triggers and use an innovative hybrid trigger model composed of a predictive and observational component. The hybrid trigger model signals the activation of a specific package of the pre-agreed action plan, ensuring that anticipatory activities are implemented when they are most effective.
    - **AAs (Anticipatory Actions)**: Aim to prevent or mitigate predictable humanitarian impacts before a specific shock or acute humanitarian needs manifest. AA has a readiness phase and an activation phase.
    - **Readiness Phase**: If AAs are triggered, during this process, stakeholders implement readiness actions needed to implement the prioritized anticipatory actions and ensure all operational requirements are in place (i.e., targeting, delivery systems, contracts with cooperating partners, etc.).
    - **Activation Phase**: During this process, stakeholders implement the prioritized anticipatory actions and monitor them.
    - **Operational Readiness**: The ability to act quickly upon trigger activation. A key constraint on the selection of activities, especially in sudden onset disasters. While funding can be released almost immediately upon a trigger activation, the time-consuming process of procuring and pre-positioning items can delay the time taken for the financing to move into the hands of those targeted. A way to approach this challenge is by funding time-bound “readiness activities” during the readiness phase.
    - **AAP (Anticipatory Action Plans)**: Developed AAPs are standard protocols that link hazard thresholds and forecast triggers with anticipatory actions, timelines, location(s), costs, and entities responsible for such actions to ensure that planned activities are successfully implemented in the window of time available between the given ‘forecast alert’ and ‘the event.’
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
