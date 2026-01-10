# AI Research Assistant - Multi-Agent System

A production-ready multi-agent AI system that conducts research using three specialized agents: Researcher, Writer, and Critic.

## Architecture

```
User Query → Researcher Agent → Writer Agent → Critic Agent → Final Report
```

- **Researcher**: Searches the web and gathers information using SerperDev API
- **Writer**: Transforms research into structured markdown report
- **Critic**: Reviews and polishes the final output for publication quality

## Tech Stack

- **CrewAI**: Multi-agent orchestration framework
- **Ollama**: Local LLM inference (llama3.1)
- **Streamlit**: Interactive web interface
- **SerperDev API**: Web search tool for agents

## Features

✅ Sequential multi-agent workflow  
✅ Real-time web search capabilities  
✅ Markdown report generation  
✅ Download reports as .md files  
✅ 100% local LLM inference (zero API costs)  
✅ Interactive Streamlit UI  

## Installation

### 1. Install Ollama
```bash
# Download from: https://ollama.ai
# Then pull the model:
ollama pull llama3.1
```

### 2. Clone & Setup
```bash
git clone https://github.com/Donald8585/ai-research-assistant.git
cd ai-research-assistant

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# OR: venv\Scripts\activate.bat  # Windows CMD

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
# Copy template
cp .env.template .env

# Edit .env and add your Serper API key
# Get free key: https://serper.dev (100 free searches)
```

### 4. Run Ollama Server
```bash
# In a separate terminal:
ollama serve
```

### 5. Launch Application
```bash
streamlit run app.py
```

## Usage

1. Open the Streamlit interface (usually http://localhost:8501)
2. Enter your research topic
3. Click "Start Research"
4. Wait 2-3 minutes for agents to complete workflow
5. Download the final report

## Example Topics

- "Latest trends in AI agents 2026"
- "Machine learning model deployment best practices"
- "Comparison of vector databases for RAG systems"

## Project Structure

```
ai-research-assistant/
├── agents.py          # Agent definitions
├── tasks.py           # Task definitions
├── crew.py            # Crew orchestration
├── app.py             # Streamlit UI
├── requirements.txt   # Python dependencies
├── .env               # API keys (not committed)
└── README.md
```

## Cost Analysis

- **Ollama (LLM)**: $0.00 (local inference)
- **SerperDev**: $0.00 (100 free searches/month)
- **Total**: $0.00/month for moderate usage

## Performance

- **Latency**: ~2-3 minutes per research task
- **Quality**: High-quality reports with proper structure
- **Scalability**: Limited by local GPU/CPU resources

## Author

**Alfred So**  
- LinkedIn: [https://www.linkedin.com/in/alfred-so/](https://www.linkedin.com/in/alfred-so/)  
- GitHub: [https://github.com/Donald8585/](https://github.com/Donald8585/)  

## License

MIT License
