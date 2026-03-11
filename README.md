# Multi-Agent AI System Evolution

## Project Overview
This project demonstrates the evolution of an AI system from a **basic chatbot** to a **supervised multi-agent architecture**. It highlights the incremental development, including human-in-the-loop assistance, multi-chain programming demos, debugging, and advanced multi-agent orchestration.

---

## 1️⃣ Basic Chatbot

- Implemented a **basic chatbot** capable of handling user queries.
- Added **streaming methods** and conversational **memory** to maintain context across messages.
- Explored **Streaming**, **ReAct architecture**, and integration with **tools** for extended capabilities.

---

## 2️⃣ Human-in-the-Loop Assistance

- Integrated **human intervention** for scenarios where expert guidance is needed.
- Designed a flow where the agent calls a `human_assistance` tool:
  1. The agent detects the need for help.
  2. The system pauses the workflow and waits for human input.
  3. Once a human responds, the agent resumes execution.
- Ensured that human feedback is seamlessly incorporated into agent decisions.

---

## 3️⃣ MCP Demo (Multi-Chain Programming)

- Demonstrated **MCP (Multi-Chain Programming)** using LangChain.
- Set up multiple **tool servers** (e.g., math, weather) and integrated them into an agent workflow.
- Implemented a **React-style agent** capable of calling different tools and handling multiple tasks concurrently.
- Showcased asynchronous execution and tool integration with a Groq LLM backend.

---

## 4️⃣ Debugging & Visualization

- Utilized **LangSmith** and **LangGraph Studio** to debug agent workflows.
- Tracked **state, messages, and tool interactions** to understand the internal workings of the agents.
- Enabled visualization of **graph execution**, tool calls, and interrupt handling for human-in-the-loop scenarios.
- Improved system reliability and observability through structured state tracking.

---

## 5️⃣ Simple Multi-Agent Architecture

- Built a **sequential multi-agent system** with three specialized agents:
  - **Researcher** – gathers relevant information.
  - **Analyst** – analyzes data and extracts insights.
  - **Writer** – creates summaries and reports.
- Agents communicate through a **shared state**, with task assignments passing from one agent to the next.
- Demonstrated the orchestration of multiple agents to collaboratively complete tasks.

---

## 6️⃣ Supervised Multi-Agent Architecture

- Introduced a **Supervisor Agent** to dynamically manage agent assignments.
- Supervisor tracks workflow progress, checks task completion, and decides the next agent.
- Enabled a **conditional routing system**, ensuring tasks are completed in a logical sequence:
  - Research → Analysis → Report Writing → Completion.
- Produced structured **reports** including executive summary, key findings, analysis, recommendations, and conclusions.
- Represents the culmination of the multi-agent orchestration and human-in-the-loop integration.

---

## Project Highlights

- Incremental development from a simple chatbot to a multi-agent system.
- Integration of human assistance for critical tasks.
- Multi-chain programming demonstrations for handling diverse tool interactions.
- Advanced debugging and state visualization using LangSmith and LangGraph Studio.
- Fully supervised multi-agent workflow producing professional reports.
