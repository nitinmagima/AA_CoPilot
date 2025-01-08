# 🌍 Anticipatory Action AI Chatbot

The **Anticipatory Action AI Chatbot** is a Streamlit-based application designed to assist disaster managers in planning and decision-making for drought-related scenarios. This AI-powered chatbot leverages OpenAI's GPT model to provide tailored insights and recommendations based on uploaded documents and selected framework sections.

---

## Features

- **Framework-Based Guidance**: Choose from predefined sections of the Anticipatory Action Framework for focused support.
- **Document Upload**: Upload relevant PDF documents (e.g., guidelines, strategies) to provide the chatbot with contextual information.
- **OpenAI Integration**: Uses OpenAI's GPT model for accurate and actionable advice.
- **Interactive Chat**: Input queries and receive responses in a conversational format.
- **Session Management**: Retains chat history during the session for easy reference.

---

## How to Use

### 1. Prerequisites
- Ensure you have Python installed.
- Obtain an OpenAI API key from the [OpenAI API Platform](https://platform.openai.com/account/api-keys).

### 2. Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/anticipatory-action-chatbot.git
   cd anticipatory-action-chatbot
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Running the Application
1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the app in your browser. The default address is `http://localhost:8501`.

### 4. Using the Chatbot
- **Enter API Key**: Add your OpenAI API key in the sidebar.
- **Select a Framework Section**: Use the radio buttons to choose the section you want to focus on.
- **Upload Documents**: Upload relevant PDFs to provide additional context for the chatbot.
- **Ask Questions**: Use the input box to interact with the chatbot. Example queries include:
  - "What steps are required to activate anticipatory actions?"
  - "How can we use forecasting models in drought management?"

---

## Application Flow

1. **Configure OpenAI API Key**:
   - The API key is required to access OpenAI's GPT model.

2. **Select Framework Section**:
   - Choose from key sections like:
     - Defining Risk and Establishing a Crisis Timeline.
     - Development of Anticipatory Actions Interventions.
     - Activating the Monitoring System of Anticipatory Actions.

3. **Upload Documents**:
   - Extracts text from uploaded PDFs for tailored advice based on the document content.

4. **Chat and Get Insights**:
   - Combines the selected section, document content, and user queries to generate responses.

---

## Code Highlights

### Key Components
1. **Sidebar**:
   - Collects the OpenAI API key.
   - Provides radio buttons for selecting the framework section.

2. **File Upload**:
   - Allows users to upload PDF documents. Extracted content is used to enhance the chatbot's context.

3. **Chat Interaction**:
   - Maintains session state to store chat history.
   - Sends user queries and document context to OpenAI for generating responses.

4. **OpenAI Integration**:
   - Combines user input, selected framework section, and document content into a comprehensive prompt for OpenAI's GPT model.

---

## Example Queries

- "What are the key steps to activate anticipatory actions for drought forecasts?"
- "How can we integrate forecasting models into decision-making processes?"
- "What are the best practices for monitoring and evaluation in drought anticipatory actions?"

---

## Troubleshooting

- **Missing API Key**:
  - If the API key is not provided, the app will prompt you to enter one in the sidebar.

- **File Upload Issues**:
  - Ensure the uploaded document is in PDF format and does not exceed the size limit.

- **Response Delays**:
  - Responses depend on OpenAI's API. Check your API usage limits or internet connection if delays occur.

---

## License

This project is licensed under the MIT License.


