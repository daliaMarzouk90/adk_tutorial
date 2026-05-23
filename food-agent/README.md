# food-agent

A production-style starter project for a simple **Google ADK** food recommendation agent.

## What is ADK?
Google **ADK (Agent Development Kit)** is a framework for building, running, and evaluating AI agents with tool usage, tracing, and runtime visibility.

## Project structure

```text
food-agent/
│
├── agent.py
├── requirements.txt
├── .env.example
├── README.md
├── eval/
│   └── test_set.json
└── screenshots/
    └── placeholder.txt
```

## Install dependencies

```bash
cd food-agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Configure environment

```bash
cp .env.example .env
# then set GOOGLE_API_KEY in .env
```

## Run the project

The agent entrypoint is `agent.py` and exposes `root_agent`.

## Start the ADK API server

```bash
adk api_server agent:root_agent --host 0.0.0.0 --port 8000
```

## Open Swagger docs

After starting the API server, open:

```text
http://localhost:8000/docs
```

## Open the ADK Dev UI

```bash
adk web agent:root_agent --host 0.0.0.0 --port 8080
```

Then open:

```text
http://localhost:8080
```

## Test the agent

### 1) From Dev UI
Ask for cuisine + diet preferences, for example:
- "Egyptian vegan meal"
- "Italian protein meal"

### 2) From API (curl)

```bash
curl -X POST "http://localhost:8000/apps/food-agent/users/demo/sessions/session-1:run" \
  -H "Content-Type: application/json" \
  -d '{
    "new_message": {
      "role": "user",
      "parts": [{"text": "Recommend an Egyptian vegan meal"}]
    }
  }'
```

## Understanding ADK runtime output

- **Execution traces**: Show the full step-by-step flow of how the agent handled a request.
- **Tool calls**: Show when `recommend_meal` was invoked and what arguments were used.
- **Session state**: Stores conversation context (user preferences across turns).
- **Runtime events**: Stream of model/tool/system events generated while handling a request.

## Evaluation dataset

`eval/test_set.json` contains sample inputs and expected outputs for basic recommendation behavior.
