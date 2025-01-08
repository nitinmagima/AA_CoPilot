from openai import OpenAI
import streamlit as st
from PyPDF2 import PdfReader

# Set the page configuration with a custom page name
st.set_page_config(
    page_title="🌍 Anticipatory Action AI Chatbot",  # Title for the browser tab
    page_icon="🌟",  # Optional icon
    layout="wide",  # Optional layout choice
    initial_sidebar_state="expanded"  # Optional initial state of the sidebar
)

# Sidebar for OpenAI API Key
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

    # Add radio buttons for predefined sections from the document
    st.markdown("### Select a Section of AA Framework to Focus On With the Chatbot")
    context_option = st.radio("Choose a section:", [
        "Defining Risk and Establishing A Crisis Timeline",
        "Establishment of the Forecasting Model for Anticipatory Actions",
        "Development of Anticipatory Actions Interventions",
        "Associating Anticipatory Actions with Predictive Models",
        "Activating the Monitoring System of Anticipatory Actions",
        "Designing and Implementing M&E for Anticipatory Actions",
        "Developing Anticipatory Action Plans (AAPs)",
    ])

    # Add copyright and name at the top
    st.markdown(
        "<div style='text-align: center; font-size: 12px; color: gray;'>"
        "© The National Center for Disaster Preparedness (NCDP) Columbia Climate School, at Columbia University. \nAll rights reserved."
        "</div>",
        unsafe_allow_html=True
    )

def main():
    st.title("🌍 Anticipatory Action AI Chatbot for Disaster Managers")
    st.caption("🚨 AI Co Pilot for Disaster Management and Decision-making for Drought")
    st.markdown(""" 
    
    - Enter your **OpenAI API Key** in the sidebar. If you don’t have one, click the provided link to get an API key. 
    - Use the sidebar's radio buttons to select a specific section of the Anticipatory Action framework to focus on. 
    - To understand each step of the AA framework, explore the pages on the left sidebar.
    
    This chatbot uses GPT-4o Mini.
    
    For further inquiries or support, please Nitin Magima at nitin.magima@columbia.edu.
    
    """)

if __name__ == "__main__":
    main()

# Display chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": (
                "Hello! I am the Anticipatory Action Assistant for Disaster Managers. My goal is to support you in making proactive decisions to mitigate "
                "the impacts of disasters. Select a section from the sidebar, upload relevant documents, or ask a question to get started!"
            ),
        }
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# File upload for relevant documents
uploaded_file = st.file_uploader("If needed, upload an additional PDF document (e.g., guidelines) to provide context for the chatbot. Ensure the file size does not exceed 200 MB and that the content is primarily text-based for accurate processing.", type=["pdf"])

document_text = ""
if uploaded_file:
    # Extract text from uploaded PDF
    pdf_reader = PdfReader(uploaded_file)
    document_text = "".join(page.extract_text() for page in pdf_reader.pages)
    st.success("Document uploaded successfully. The chatbot will use this for context.")

    # Add extracted content to the chat history for context
    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": (
                f"I have successfully uploaded the provided document. Based on the selected section '{context_option}', "
                "I can provide tailored advice. Feel free to ask specific questions or provide scenarios where you need support."
            ),
        }
    )

# System-level prompt for context
general_prompt = (
    "You are an expert assistant on disaster management. Focus on providing tailored strategies and actions based on the selected section and the "
    "uploaded document. Use the following document as context for your responses."
)

# User input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Combine document text, selected context, and general system prompt
    context = f"{general_prompt}\n\nSelected Section:\n{context_option}\n\nDocument Content:\n{document_text}\n\nUser Query: {prompt}"

    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": general_prompt},
            {"role": "assistant", "content": f"Selected Section:\n{context_option} for Drought\n\nDocument Content:\n{document_text}"},
        ]
        + [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages],
        max_tokens=1000,
    )

    # Process response
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

# Add a copyright line at the bottom of the page
st.markdown(
    "<div style='text-align: center; margin-top: 50px; font-size: 12px; color: gray;'>"
    "© The National Center for Disaster Preparedness (NCDP) Columbia Climate School, at Columbia University. All rights reserved."
    "</div>",
    unsafe_allow_html=True
)
