# Autonomous Research Agent 🤖🔍

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Autonomous_Agents-red)](https://github.com/joaomdmoura/crewAI)
[![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green)](https://github.com/langchain-ai/langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Autonomous Research Agent** is a multi-agent system designed to automate deep-dive research on any topic. By leveraging **CrewAI**, it orchestrates specialized agents that work together to browse the web, synthesize findings, and produce a professional-grade research report.

## 🌟 Key Features

- **🕵️ Deep Research Agent**: Scours multiple search engines and web pages to find high-signal information.
- **✍️ Technical Writer Agent**: Synthesizes raw data into a structured, readable, and professional report.
- **🛡️ Fact Checker Agent**: Cross-references findings to ensure accuracy and reduce hallucinations.
- **🔄 Iterative Refinement**: Agents collaborate to improve the report through multiple internal reviews.
- **📄 Multiple Formats**: Export research results to Markdown, PDF, or structured JSON.

## 🏗️ Architecture

The system follows a sequential multi-agent workflow:
1.  **Search**: Research Agent initiates web search and data gathering.
2.  **Synthesis**: Technical Writer creates the first draft of the report.
3.  **Review**: Fact Checker evaluates the draft for accuracy and completeness.
4.  **Finalization**: Agent team finalizes the report based on review feedback.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- OpenAI API Key
- Serper API Key (for Google Search tool)

### Installation
`ash
git clone https://github.com/samraat22/Autonomous-Research-Agent.git
cd Autonomous-Research-Agent
pip install -r requirements.txt
`

### Usage
`python
from main import run_research

# Perform research on a specific topic
result = run_research(topic="The impact of Generative AI on Software Engineering in 2026")
print(result)
`

## 🛠️ Tech Stack
- **Agent Framework**: CrewAI
- **LLM Orchestration**: LangChain
- **Core LLM**: GPT-4o / Claude 3.5 Sonnet
- **Web Search**: Serper / DuckDuckGo

---
Developed with ❤️ by [Samraat](https://github.com/samraat22)