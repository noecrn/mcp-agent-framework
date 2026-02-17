# 🐉 Once Upon Agentic AI: The Strands Quest

[![AWS Workshop](https://img.shields.io/badge/AWS-Workshop-orange?logo=amazon-aws)](https://catalog.us-east-1.prod.workshops.aws/workshops/e1493217-4bc7-42f4-87d9-e231acd743bc/en-US/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![SDK](https://img.shields.io/badge/SDK-Strands-blueviolet)

> *"Roll for Initiative... in Python!"*

This repository contains my code and progress through the **AWS Strands SDK Workshop**. It tracks my transformation from a coding apprentice into a master of AI agent orchestration, building a digital adventuring party capable of autonomous thought and collaboration.

## 🗺️ The Adventure Map

The project is structured into five epic chapters, each building upon the last:

### 🧙‍♂️ Chapter 1: Agent Summoning
* **Goal:** Master the fundamental ritual of agent creation.
* **Key Learning:** Configuring system prompts and model parameters within the Strands framework.

### ⚔️ Chapter 2: The Adventurer's Arsenal
* **Goal:** Equip agents with built-in magical tools.
* **Key Learning:** Implementing autonomous web scraping and information gathering with tool safety mechanisms.

### 🔨 Chapter 3: The Art of Magical Forging
* **Goal:** Create the legendary *Dice of Destiny*.
* **Key Learning:** Transforming Python functions into agent-executable tools using the `@tool` decorator.

### 🌐 Chapter 4: Planar Portals (MCP)
* **Goal:** Connect to external realms via Model Context Protocol.
* **Key Learning:** Building MCP servers and clients to bridge agents with external services.

### 🏰 Chapter 5: The Grand Alliance (A2A)
* **Goal:** Command a full D&D adventuring party.
* **Key Learning:** Orchestrating **Agent-to-Agent (A2A)** communication for complex, distributed AI tasks.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** [Strands SDK](https://strandsagents.com/latest/)
* **AI Models:** Amazon Bedrock (Claude 3 / 3.5)
* **Integration:** Model Context Protocol (MCP)

## 🚀 Installation & Setup

1. **Clone the Quest Log**
 ```bash
 git clone https://github.com/noecrn/mcp-agent-framework.git
 cd strands-quest
```

2. **Prepare your Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


3. **Configure AWS Credentials**
Ensure your AWS CLI is configured with permissions for Amazon Bedrock.

## 🎲 Journey Highlights

* **The Dice of Destiny:** A custom tool allowing agents to simulate high-stakes RPG rolls.
* **Multi-Agent Coordination:** Watching a "Dungeon Master" agent delegate lore-checking to a "Librarian" agent.

---

*“The best way to predict the future is to build the agents that will create it.”*
