# News Report Crew

An AI-powered multi-agent system that researches a topic and generates a structured news-style report automatically.

This project demonstrates how multiple AI agents can collaborate to produce clear, organized, and informative content. Each agent has a defined role, creating a workflow similar to a real newsroom.

---

## Overview

News Report Crew takes a topic as input and produces a detailed news report by coordinating several specialized agents. Instead of one model doing everything, responsibilities are split across agents for better structure and clarity.

### Agents in the system

* Research Agent
  Gathers background information and context about the topic

* Analysis Agent
  Extracts key facts, trends, and insights

* Writer Agent
  Produces a polished, readable final report

---

## Features

* Multi-agent AI workflow
* Automated research and summarization
* Structured long-form report generation
* Configurable agent roles and tasks
* Modular design for easy expansion

---

## Project Structure

```
news_report_crew/
│
├── src/
│   └── news_report_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── crew.py
│       └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/news_report_crew.git
cd news_report_crew
```

Create a virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create a `.env` file and add your API key:

```
OPENAI_API_KEY=your_key_here
```

---

## Usage

Run the project:

```
python main.py
```

Enter a topic when prompted.
The system will generate a structured news report based on that topic.

---

## Configuration

You can customize the workflow by editing:

* `agents.yaml` – defines agent roles and goals
* `tasks.yaml` – defines the workflow
* `crew.py` – core orchestration logic

---

## Example Use Cases

* Automated news drafting
* Research summaries
* AI agent experimentation
* Content generation workflows

---

## Tech Stack

* Python
* CrewAI
* LangChain
* OpenAI API

---

## Future Improvements

* Web interface (Streamlit or FastAPI)
* Source citation support
* Real-time news retrieval
* Export to PDF or DOCX
* RAG-based fact retrieval

---

## Author

Dwinayan

---

## License

MIT
