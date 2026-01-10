import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
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
    st.markdown("- SerperDev API")
    
    st.markdown("---")
    st.markdown("Built with CrewAI | By Alfred So")

# Get API keys
cohere_api_key = st.secrets.get("COHERE_API_KEY", "")
serper_api_key = st.secrets.get("SERPER_API_KEY", "")

if not cohere_api_key or not serper_api_key:
    st.warning("⚠️ Please add API keys in Streamlit Cloud settings!")
    st.info("""
    ### Get FREE API Keys:
    
    **1. Cohere (for AI):**
    - Visit: [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)
    - 1000 calls/month FREE
    
    **2. SerperDev (for search):**
    - Visit: [serper.dev](https://serper.dev)
    - 2500 searches FREE
    
    **Add to Streamlit secrets:**
    ```
    COHERE_API_KEY = "your_cohere_key"
    SERPER_API_KEY = "your_serper_key"
    ```
    """)
    st.stop()

# Set environment variable for SerperDev
os.environ["SERPER_API_KEY"] = serper_api_key

# Initialize LLM using CrewAI's LLM class (NOT LangChain!)
llm = LLM(
    model="cohere/command-r7b-12-2024",
    api_key=cohere_api_key,
    temperature=0.7
)

# Initialize search tool
search_tool = SerperDevTool()

# Define Agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments and trends in {topic}",
    backstory="""You are an expert research analyst with years of experience in 
    gathering and synthesizing information from various sources. You excel at 
    finding accurate, relevant, and up-to-date information using web search.""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[search_tool]
)

writer = Agent(
    role="Technical Content Writer",
    goal="Create comprehensive, well-structured technical reports on {topic}",
    backstory="""You are a skilled technical writer who specializes in creating 
    clear, engaging, and informative content. You excel at organizing complex 
    information into readable, professional reports.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

critic = Agent(
    role="Quality Assurance Critic",
    goal="Review and polish reports to ensure highest quality standards",
    backstory="""You are a meticulous editor and quality assurance specialist. 
    You have a keen eye for detail and ensure all reports are accurate, 
    well-formatted, and professionally written.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Research form
with st.form("research_form"):
    topic = st.text_input(
        "Enter research topic:",
        placeholder="Latest MLOps tools and practices in 2026"
    )
    
    submitted = st.form_submit_button("🚀 Start Research", use_container_width=True)

if submitted and topic:
    st.markdown("---")
    
    try:
        with st.spinner("🔍 Research in progress... This may take 60-90 seconds"):
            
            # Define tasks
            research_task = Task(
                description=f"""Research {topic} using web search. Focus on:
                1. Latest developments and trends in 2026
                2. Key tools, technologies, and platforms
                3. Best practices and industry recommendations
                4. Reliable sources and current data
                
                Use the search tool to gather comprehensive, accurate, up-to-date information.
                Include specific examples, version numbers, and sources.""",
                agent=researcher,
                expected_output="Detailed research findings with sources"
            )
            
            write_task = Task(
                description=f"""Using the research findings, write a comprehensive report on {topic}.
                
                Required Structure:
                # [Report Title]
                
                ## Executive Summary
                Brief overview (2-3 sentences)
                
                ## Key Findings
                - Finding 1
                - Finding 2
                - Finding 3
                (Use bullet points)
                
                ## Detailed Analysis
                Comprehensive discussion with examples
                
                ## Conclusion
                Summary and recommendations
                
                ## Sources
                List sources found during research
                
                Make it clear, professional, and well-formatted in markdown.""",
                agent=writer,
                expected_output="Well-structured markdown report"
            )
            
            review_task = Task(
                description="""Review the report for:
                1. Accuracy and completeness
                2. Clarity and readability
                3. Proper markdown formatting
                4. Grammar and spelling
                5. Professional tone
                
                Polish and finalize the report.""",
                agent=critic,
                expected_output="Final polished report in markdown"
            )
            
            # Create crew
            crew = Crew(
                agents=[researcher, writer, critic],
                tasks=[research_task, write_task, review_task],
                process=Process.sequential,
                verbose=False
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
            data=str(result),
            file_name=f"{topic.replace(' ', '_')}_report.md",
            mime="text/markdown",
            use_container_width=True
        )
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        
        import traceback
        with st.expander("🐛 Technical Details"):
            st.code(traceback.format_exc())
        
        st.info("""
        💡 **Troubleshooting:**
        - Check both API keys are valid
        - Agents take 60-90 seconds
        - SerperDev free tier: 2500 searches
        - Cohere free tier: 1000 calls/month
        """)

# Footer
st.markdown("---")
st.markdown("### 💡 Tips:")
st.markdown("- Be specific with your research topic")
st.markdown("- Agents perform LIVE web searches")
st.markdown("- Results include current 2026 data")
st.markdown("- Download reports for later reference")
