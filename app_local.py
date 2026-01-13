import streamlit as st
from crew import run_research_crew
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Assistant")
st.markdown("### Multi-Agent System: Researcher → Writer → Critic")

with st.sidebar:
    st.header("About")
    st.markdown("""
    This system uses 3 AI agents:
    - 🔍 **Researcher**: Gathers information
    - ✍️ **Writer**: Creates structured report
    - 🎯 **Critic**: Reviews and polishes
    """)

    st.markdown("---")
    st.markdown("**Tech Stack:**")
    st.markdown("- CrewAI")
    st.markdown("- Ollama (llama3.1)")
    st.markdown("- SerperDev API")

topic = st.text_input("Enter research topic:", placeholder="e.g., Latest trends in AI agents 2026")

if st.button("🚀 Start Research", type="primary"):
    if not topic:
        st.error("Please enter a research topic!")
    else:
        with st.spinner("🔍 Agents are working... (this may take 2-3 minutes)"):
            try:
                result = run_research_crew(topic)

                st.success("✅ Research complete!")

                st.markdown("## 📄 Final Report")
                st.markdown(result)

                st.download_button(
                    label="📥 Download Report",
                    data=str(result),
                    file_name=f"research_report_{topic.replace(' ', '_')}.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Make sure Ollama is running: ollama serve")

st.markdown("---")
st.markdown("Built with CrewAI | By Alfred So")
