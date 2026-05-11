# 🤖 Professional Research Assistant

An intelligent AI-powered research assistant that searches the internet for the latest news and real-time updates. This project combines LangChain agents with OpenAI's language models to provide accurate, up-to-date information through an intuitive web interface.

## ✨ Features

- **AI-Powered Search**: Uses OpenAI's language models to understand and process research queries
- **Real-Time Information**: Integrates with Tavily Search API for the latest news and updates
- **Web Interface**: User-friendly Streamlit interface for easy interaction
- **Intelligent Agent**: LangChain-based agent that intelligently uses tools to gather accurate information
- **Professional Response Format**: Receives well-structured, professional research responses

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- OpenAI API key

### Installation

1. **Clone the repository** (or set up the project directory)
   ```bash
   git clone https://github.com/timoachal/Langchain_Agent.git
   cd AI_agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root directory:
   ```
   AI_MODEL=gpt-4
   AI_API_KEY=your_openai_api_key_here
   AI_ENDPOINT=https://api.openai.com/v1
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

### Running the Application

**Option 1: Web Interface (Recommended)**
```bash
streamlit run app.py
```
This launches an interactive web interface where you can ask research questions in real-time.

**Option 2: Command Line**
```bash
python main.py
```
This runs the agent from the command line with a predefined example query.

## 📋 Project Structure

- **`app.py`** - Streamlit web application providing an interactive UI for the research assistant
- **`main.py`** - Command-line script demonstrating the agent functionality
- **`pyproject.toml`** - Project dependencies and metadata

## 🛠️ How It Works

1. **Query Input**: User enters a research question
2. **Agent Processing**: The LangChain agent analyzes the query
3. **Internet Search**: Tavily Search API retrieves the latest relevant information
4. **AI Response**: OpenAI's language model synthesizes the information into a professional response
5. **Output**: Results are displayed in a user-friendly format

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| langchain | >=1.2.18 | Agent and tool orchestration |
| langchain-community | >=0.4.1 | Community integrations |
| langchain-openai | >=1.2.1 | OpenAI integration |
| python-dotenv | >=1.2.2 | Environment variable management |
| streamlit | >=1.57.0 | Web interface framework |
| tavily-python | >=0.7.24 | Search API integration |

## 🔌 API Keys Required

### OpenAI API
- Get your key from: https://platform.openai.com/api-keys
- Supports various models 


## 💡 Usage Examples

### Web Interface
1. Open the Streamlit app
2. Enter your question: *"What are the latest news about hantavirus?"*
3. Click "Run Research"
4. View the AI-generated research response

### Command Line
Modify the query in `main.py`:
```python
response = agent.invoke({
    "messages":[("human", "your question here")]
})
```
Then run: `python main.py`

## ⚙️ Configuration

The assistant is configured with the following settings:
- **Temperature**: Set to 0 for deterministic, consistent responses
- **System Prompt**: Professional research assistant instructions
- **Search Results**: Limited to 1 result per query for focused responses


## 📈 Future Enhancements

- Support for multiple search results
- Conversation history and context
- Multiple language support
- Integration with more search APIs
- Response caching for frequently asked questions
- Custom model configuration

## 🤝 Contributing

Feel free to fork, modify, and improve this project. Some areas for contribution:
- Add more research tools
- Improve response formatting
- Add unit tests
- Enhance error handling
- UI/UX improvements

## 📝 License

This project is open-source and available under the MIT License.

## 🆘 Troubleshooting

### Streamlit won't start
- Ensure all dependencies are installed: `uv sync`
- Check that Python 3.11+ is being used

### API Key errors
- Verify `.env` file exists in the project root
- Check that API keys are correctly set and active
- Ensure you have sufficient API quota

### No search results
- Check internet connection
- Try a different query format

**Happy Researching! 🔍**
