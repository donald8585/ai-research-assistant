import streamlit as st
from crewai import Agent, Task, Crew, Process
from langchain_cohere import ChatCohere
from langchain_community.tools import DuckDuckGoSearchRun
import os

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Assistant")
st.markdown("### Multi-Agent System: Researcher → Writer → Critic")

# Sidebar
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
    st.markdown("- Cohere (command-r7b)")
    st.markdown("- DuckDuckGo Search")
    
    st.markdown("---")
    st.markdown("Built with CrewAI | By Alfred So")

# Get API key
cohere_api_key = st.secrets.get("COHERE_API_KEY", "")

if not cohere_api_key:
    cohere_api_key = st.text_input(
        "Cohere API Key", 
        type="password",
        help="Get FREE at dashboard.cohere.com/api-keys"
    )

if not cohere_api_key:
    st.warning("⚠️ Please add your Cohere API key to continue!")
    st.info("""
    ### Get FREE Cohere API Key:
    1. Visit: [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
    2. Sign up (no credit card!)
    3. Copy your API key
    4. Paste above or add to Streamlit secrets
    """)
    st.stop()

# Initialize LLM
@st.cache_resource
def get_llm(api_key):
    return ChatCohere(
        cohere_api_key=api_key,
        model="command-r7b-12-2024",
        temperature=0.7
    )

llm = get_llm(cohere_api_key)

# Initialize search tool
search_tool = DuckDuckGoSearchRun()

# Define Agents
@st.cache_resource
def create_agents(_llm):
    researcher = Agent(
        role="Senior Research Analyst",
        goal="Uncover cutting-edge developments and trends in {topic}",
        backstory="""You are an expert research analyst with years of experience in 
        gathering and synthesizing information from various sources. You excel at 
        finding accurate, relevant, and up-to-date information.""",
        verbose=True,
        allow_delegation=False,
        llm=_llm,
        tools=[search_tool]
    )
    
    writer = Agent(
        role="Technical Content Writer",
        goal="Create comprehensive, well-structured technical reports on {topic}",
        backstory="""You are a skilled technical writer who specializes in creating 
        clear, engaging, and informative content. You excel at organizing complex 
        information into readable reports.""",
        verbose=True,
        allow_delegation=False,
        llm=_llm
    )
    
    critic = Agent(
        role="Quality Assurance Critic",
        goal="Review and polish reports to ensure highest quality standards",
        backstory="""You are a meticulous editor and quality assurance specialist. 
        You have a keen eye for detail and ensure all reports are accurate, 
        well-formatted, and professionally written.""",
        verbose=True,
        allow_delegation=False,
        llm=_llm
    )
    
    return researcher, writer, critic

researcher, writer, critic = create_agents(llm)

# Research form
with st.form("research_form"):
    topic = st.text_input(
        "Enter research topic:",
        placeholder="Latest MLOps tools and practices in 2026"
    )
    
    submitted = st.form_submit_button("🚀 Start Research", use_container_width=True)

if submitted and topic:
    st.markdown("---")
    
    # Progress tracking
    progress_container = st.empty()
    status_container = st.empty()
    
    try:
        with st.spinner("🔍 Research in progress..."):
            # Define tasks
            research_task = Task(
                description=f"""Research {topic}. Focus on:
                1. Latest developments and trends
                2. Key tools and technologies
                3. Best practices and recommendations
                4. Reliable sources and data
                
                Gather comprehensive information from multiple sources.""",
                agent=researcher,
                expected_output="Detailed research findings with sources"
            )
            
            write_task = Task(
                description=f"""Using the research findings, write a comprehensive report on {topic}.
                
                Structure:
                1. Executive Summary
                2. Key Findings (with bullet points)
                3. Detailed Analysis
                4. Conclusion
                5. Sources
                
                Make it clear, professional, and well-formatted in markdown.""",
                agent=writer,
                expected_output="Well-structured markdown report"
            )
            
            review_task = Task(
                description="""Review the report for:
                1. Accuracy and completeness
                2. Clarity and readability
                3. Proper formatting
                4. Grammar and spelling
                
                Polish and finalize the report.""",
                agent=critic,
                expected_output="Final polished report in markdown"
            )
            
            # Create and run crew
            crew = Crew(
                agents=[researcher, writer, critic],
                tasks=[research_task, write_task, review_task],
                process=Process.sequential,
                verbose=True
            )
            
            # Execute
            result = crew.kickoff()
            
        # Display results
        st.success("✅ Research completed!")
        
        st.markdown("## 📄 Final Report")
        st.markdown("---")
        
        # Display report
        st.markdown(result)
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data=result,
            file_name=f"{topic.replace(' ', '_')}_report.md",
            mime="text/markdown"
        )
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.info("""
        💡 **Common issues:**
        - Make sure your Cohere API key is valid
        - CrewAI agents may take 30-60 seconds to complete
        - Try a simpler topic if it fails
        """)

# Footer
st.markdown("---")
st.markdown("### 💡 Tips:")
st.markdown("- Be specific with your research topic")
st.markdown("- Agent workflow takes 30-90 seconds")
st.markdown("- Reports are generated in markdown format")
st.markdown("- Download reports for later reference")
