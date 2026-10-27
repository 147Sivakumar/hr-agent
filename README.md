# AutoGen HR Assistant Agent

## Project Overview
This project demonstrates how to build a simple HR Assistant Agent using Python, Microsoft AutoGen, and the OpenAI API.

The agent generates a five-line job description for a Junior Python Developer.

## Technologies Used
- Python
- AutoGen AgentChat
- OpenAI GPT-4o mini
- Python-dotenv
- Asyncio

## Project Structure

```text
hr-agent/
├── hr_agent.py
├── README.md
├── .env
├── .gitignore
└── venv/
```

**Note:** The `.env` file and `venv/` directory must not be uploaded to GitHub.

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Environment

Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -U "autogen-agentchat" "autogen-ext[openai]" python-dotenv
```

### 4. Configure the API Key

Create a `.env` file in the project folder:

```dotenv
OPENAI_API_KEY=your-actual-openai-api-key
```

Replace the placeholder with your actual OpenAI API key. Never commit this file to GitHub.

### 5. Run the Agent

```bash
python hr_agent.py
```

## How It Works

1. **Brain:** `OpenAIChatCompletionClient` connects the agent to the OpenAI language model.
2. **Agent:** `AssistantAgent` is configured with the name `hr_assistant` and the system message `You are an HR assistant.`
3. **Run:** The agent receives a task requesting exactly five numbered points for a Junior Python Developer job description.
4. **Display:** `Console` streams the conversation and response to the terminal.
5. **Cleanup:** The model client is closed after execution.

## Expected Output

The assistant generates five numbered points describing the responsibilities of a Junior Python Developer.

## Security

Add the following entries to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

Never publish your OpenAI API key or other credentials.

## Author

Created as part of an AutoGen agent-building assignment.
