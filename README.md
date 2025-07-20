
# Copilot Project 

A multi-agent AI-powered Copilot system designed to enhance productivity, automate tasks, and provide intelligent assistance in development workflows. This project brings together several agents to handle different responsibilities such as documentation generation, question answering, summarization, SDLC insights, and more.

---

## Tech Stack

- **Language**: Python 3.x
- **AI Frameworks**: LangChain, OpenAI API
- **Environment Management**: `.env` for API keys
- **Workspace**: Visual Studio Code (`.code-workspace` file included)

---

## Folder Structure

- `3P-LLM/` – Agent focused on three-phase LLM tasks.
- `GraspXL/` – Enhanced document understanding and summarization.
- `InterDreamer/` – Agent for creative ideation and interaction.
- `ModaLink/` – Possibly focused on code linking or fashion use-cases.

---

## Agents Overview

Each of these `.py` files defines an individual AI agent:

| File | Description |
|------|-------------|
| `copilot.py` | Central script to initialize and coordinate AI agents. |
| `healthagent.py` | AI agent focused on health-related queries. |
| `ragagent.py` | Retrieval-Augmented Generation (RAG)-based assistant. |
| `sdlcagent.py` | Helps with SDLC-related questions or tasks. |
| `question_and_answeragent.py` | Q&A system for general or domain-specific queries. |
| `summarize.py` | Text summarization agent. |

---

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Gemini API Key](https://aistudio.google.com/apikey)
- Recommended: VS Code + Python extension

### Setup

```bash
# Clone the repository
git clone https://github.com/tharun-pandya/copilot_project.git
cd copilot_project

# Install dependencies
pip install -r requirements.txt

# Set your API key
echo "OPENAI_API_KEY=your-api-key" > api_key.env
```

---

## Usage

You can run each agent script individually, for example:

```bash
python copilot.py
python healthagent.py
```

Some agents may expect prompts or documents as input. Refer to the source code comments for additional instructions.

---

## Purpose

This project is part of an exploration into **AI assistant development**, problem solving, and workflow automation. Ideal for:

- Learning how multi-agent systems work
- Using LangChain with OpenAI
- Enhancing your development productivity

---

## Author

Developed by **Tharun Pandya**
Email: ktharunpandya@gmail.com
LinkedIn : https://linkedin.com/in/tharun-pandya-kodi
