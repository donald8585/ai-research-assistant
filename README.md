---
title: AI Research Assistant
emoji: 🔬
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.25.0
app_file: app.py
pinned: false
---


# 🤖 AI Research Assistant - Multi-Agent System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.8.0-green.svg)](https://github.com/crewAIInc/crewAI)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-llama3.1-red.svg)](https://ollama.ai/)

> 🎯 Production-ready multi-agent AI system demonstrating agentic workflows, local LLM deployment, and MLOps best practices

A sophisticated research assistant that orchestrates three specialized AI agents to automatically generate comprehensive, well-structured research reports with zero API costs.

[📺 Demo](#demo) | [🚀 Quick Start](#quick-start) | [🏗️ Architecture](#architecture) | [📝 Examples](#examples)

---

## ✨ Features

- **🔄 Multi-Agent Collaboration**: Three specialized agents working sequentially (Researcher → Writer → Critic)
- **💰 Zero API Costs**: 100% local LLM inference using Ollama llama3.1
- **🔍 Real-Time Web Search**: SerperDev API integration for current information gathering
- **📊 Structured Reports**: Markdown-formatted reports with proper citations and source attribution
- **🎨 Interactive UI**: Clean Streamlit interface with real-time agent workflow visualization
- **📥 Export Functionality**: Download reports as `.md` files for documentation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Input (Topic)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   🔍 Researcher Agent         │
        │   - Web search (SerperDev)    │
        │   - Data gathering            │
        │   - Source identification     │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   ✍️  Writer Agent            │
        │   - Report structuring        │
        │   - Content organization      │
        │   - Markdown formatting       │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   🎯 Critic Agent             │
        │   - Quality review            │
        │   - Accuracy check            │
        │   - Final polishing           │
        └──────────────┬────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │   📄 Final Report             │
        │   (Markdown with citations)   │
        └──────────────────────────────┘
```

### Agent Roles

| Agent | Role | Responsibilities | Tools |
|-------|------|-----------------|-------|
| 🔍 **Researcher** | Senior Research Analyst | Web search, data gathering, source identification | SerperDev API |
| ✍️ **Writer** | Technical Content Writer | Report structuring, content organization, markdown formatting | None |
| 🎯 **Critic** | Quality Assurance Specialist | Accuracy review, completeness check, final polishing | None |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.ai/) installed and running
- SerperDev API key (100 free searches/month at [serper.dev](https://serper.dev))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Donald8585/ai-research-assistant.git
   cd ai-research-assistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv

   # Windows (Git Bash)
   source venv/Scripts/activate

   # Windows (CMD)
   venv\Scripts\activate.bat

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Pull Ollama model**
   ```bash
   ollama pull llama3.1
   ```

5. **Start Ollama server** (in a separate terminal)
   ```bash
   ollama serve
   ```

6. **Configure API keys**

   Create a `.env` file in the project root:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   ```

7. **Run the application**
   ```bash
   streamlit run app.py
   ```

8. **Open browser**

   Navigate to `http://localhost:8501`

---

## 📝 Examples

### Example Topics to Try

- "Latest MLOps tools and practices in 2026"
- "AI agent frameworks comparison: LangGraph vs CrewAI vs AutoGen"
- "Machine learning engineering skills for San Francisco tech jobs"
- "Best practices for deploying large language models in production"

### Sample Output

The system generates comprehensive reports with:
- ✅ Executive summary
- ✅ Key findings with bullet points
- ✅ Detailed analysis sections
- ✅ Proper source citations
- ✅ Conclusion and recommendations

---

## 🛠️ Tech Stack

### Core Frameworks
- **[CrewAI](https://github.com/crewAIInc/crewAI)** (1.8.0) - Multi-agent orchestration
- **[Ollama](https://ollama.ai/)** - Local LLM inference (llama3.1, 8B parameters)
- **[Streamlit](https://streamlit.io/)** (1.52.2) - Interactive web interface
- **[LangChain](https://www.langchain.com/)** - Tool integration framework

### APIs & Tools
- **SerperDev API** - Real-time web search
- **LiteLLM** - LLM provider abstraction layer
- **Python-dotenv** - Environment variable management

### Infrastructure
- **Python 3.13**
- **Local deployment** (zero cloud costs)
- **No GPU required** (CPU inference with Ollama)

---

## 📂 Project Structure

```
ai-research-assistant/
├── agents.py              # Agent definitions and LLM configuration
├── tasks.py               # Task definitions for each agent
├── crew.py                # Crew orchestration logic
├── app.py                 # Streamlit UI application
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .env.template          # Template for environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

---

## 💡 Key Technical Decisions

### Why Multi-Agent Architecture?

1. **Separation of Concerns**: Each agent focuses on a specific task (research, writing, review)
2. **Quality Assurance**: Critic agent ensures output meets quality standards
3. **Scalability**: Easy to add new agents or modify workflows
4. **Maintainability**: Clear responsibilities make debugging easier

### Why Ollama + Local Inference?

1. **Zero API Costs**: No per-token charges from cloud providers
2. **Data Privacy**: All processing happens locally
3. **No Rate Limits**: Unlimited usage without throttling
4. **Offline Capability**: Works without internet (except for web search)

### Why Sequential Process?

1. **Predictable Workflow**: Clear progression through stages
2. **Quality Control**: Each stage builds on previous work
3. **Debugging**: Easy to identify which agent caused issues
4. **Resource Efficiency**: One agent active at a time

---

## 🎯 Performance Metrics

| Metric | Value |
|--------|-------|
| **Report Generation Time** | 2-3 minutes |
| **Cost per Report** | $0.00 (local inference) |
| **Model Size** | 8B parameters (llama3.1) |
| **Memory Usage** | ~8GB RAM |
| **Concurrent Users** | 1 (local deployment) |

---

## 🔧 Configuration

### Environment Variables

```env
# Required
SERPER_API_KEY=your_serper_api_key

# Optional (defaults provided)
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=NA
```

### Agent Configuration

Agents can be customized in `agents.py`:
- **Role**: Agent's job title and expertise
- **Goal**: What the agent aims to achieve
- **Backstory**: Agent's background and specialization
- **Tools**: Available tools (e.g., SerperDevTool)
- **LLM**: Model to use (e.g., "ollama/llama3.1:latest")

---

## 🚧 Troubleshooting

### Common Issues

**Issue**: "Error: Fallback to LiteLLM is not available"
- **Solution**: Install litellm: `pip install litellm`

**Issue**: "Model llama3.1 not found"
- **Solution**: Pull the model: `ollama pull llama3.1`

**Issue**: "Connection refused to localhost:11434"
- **Solution**: Start Ollama server: `ollama serve`

**Issue**: "Received None or empty response from LLM"
- **Solution**: Ensure `memory=False` in `crew.py` (Ollama doesn't support embeddings)

---

## 🔮 Future Enhancements

- [ ] Add support for multiple LLM backends (OpenAI, Anthropic, Groq)
- [ ] Implement streaming responses for real-time output
- [ ] Add report templates for different domains
- [ ] Support for PDF and DOCX export formats
- [ ] Multi-language report generation
- [ ] Agent memory for conversation history
- [ ] Parallel agent execution for faster processing
- [ ] Custom tool integration (e.g., academic databases)

---

## 📊 Use Cases

- **Research & Analysis**: Generate comprehensive reports on any topic
- **Content Creation**: Automate blog post research and drafting
- **Market Research**: Analyze industry trends and competitors
- **Technical Documentation**: Research and document technical topics
- **Learning & Education**: Explore new subjects with structured reports

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Alfred So**

- LinkedIn: [https://www.linkedin.com/in/alfred-so/](https://www.linkedin.com/in/alfred-so/)
- GitHub: [https://github.com/Donald8585/](https://github.com/Donald8585/)
- Kaggle: [https://www.kaggle.com/sword4949/code](https://www.kaggle.com/sword4949/code)

---

## 🙏 Acknowledgments

- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent orchestration framework
- [Ollama](https://ollama.ai/) - Local LLM deployment
- [Meta AI](https://ai.meta.com/) - LLaMA 3.1 model
- [Streamlit](https://streamlit.io/) - Interactive UI framework
- [SerperDev](https://serper.dev/) - Web search API

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/Donald8585/ai-research-assistant?style=social)
![GitHub forks](https://img.shields.io/github/forks/Donald8585/ai-research-assistant?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Donald8585/ai-research-assistant?style=social)

---

<div align="center">

**Built with ❤️ using CrewAI and Ollama**

⭐ Star this repo if you find it helpful!

</div>
