# food-agent

A production-style starter project for a simple **Google ADK** food recommendation agent.

## What is ADK?
Google **ADK (Agent Development Kit)** is a framework for building, running, and evaluating AI agents with tool usage, tracing, and runtime visibility.

## Project structure

```text
.
├── README.md
└── food-agent/
    ├── agent.py
    ├── prompt.py
    ├── tools.py
    ├── pyproject.toml
    ├── .env.example
    ├── eval/
    │   └── test_set.json
    └── screenshots/
        └── placeholder.txt
```

## Install dependencies

```bash
cd food-agent
uv venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
uv sync
```

## Configure environment

```bash
cp .env.example .env
# then set GOOGLE_API_KEY in .env
```

## Run the project

The agent entrypoint is `agent.py` and exposes `root_agent`. Prompt text and tools are split into `prompt.py` and `tools.py`.


## Open the ADK Dev UI

```bash
cd ..
adk web agent:root_agent --host 0.0.0.0 --port 8080
```

Then open:

```text
http://localhost:8080
```

Check swagger:

```text
http://localhost:8000/docs
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
