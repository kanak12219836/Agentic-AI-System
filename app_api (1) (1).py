# Generated from: app_api.ipynb
# Converted at: 2026-01-04T17:12:15.135Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import sys

# Fix import path (important for deployment)
sys.path.append(os.getcwd())

from app.agent.executor import Executor

app = FastAPI(
    title="Agentic AI System",
    description="API to run Agentic AI tasks",
    version="1.0"
)

agent = Executor()

class AgentRequest(BaseModel):
    goal: str
    input_file: str

@app.post("/run-agent")
def run_agent(request: AgentRequest):
    try:
        result = agent.execute(
            goal=request.goal,
            input_file=request.input_file
        )

        # Ensure the 'output' directory exists before writing
        if not os.path.exists('output'):
            os.makedirs('output')

        # For demonstration, let's write something to output.txt if it doesn't exist
        # In a real scenario, the agent.execute would handle file output
        if not os.path.exists("output/output.txt"):
            with open("output/output.txt", "w", encoding="utf-8") as f:
                f.write(f"Goal: {request.goal}, Input File: {request.input_file}\n")
                f.write(f"Agent Result (placeholder): {result}")

        with open("output/output.txt", "r", encoding="utf-8") as f:
            output_text = f.read()

        return {
            "status": "success",
            "message": result,
            "output": output_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

!pip install "uvicorn[standard]"

# Once the Uvicorn server is running, you will see output with a local address (e.g., `http://0.0.0.0:8000`). If you are running this in a Colab environment, you might need to use a tunneling service like ngrok to expose your local server to the internet. Colab often provides an ngrok URL automatically if you run the server this way. You can then access your API endpoints, for example, by navigating to `/docs` for the Swagger UI (`<ngrok_url>/docs`).


# First, let's write your FastAPI application code into a `main.py` file. This is crucial for running Uvicorn as a separate process in the background, which is the most reliable way in Colab to avoid event loop conflicts.


app_content = '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import sys

# Fix import path (important for deployment)
sys.path.append(os.getcwd())

from app.agent.executor import Executor

app = FastAPI(
    title="Agentic AI System",
    description="API to run Agentic AI tasks",
    version="1.0"
)

agent = Executor()

class AgentRequest(BaseModel):
    goal: str
    input_file: str

@app.post("/run-agent")
def run_agent(request: AgentRequest):
    try:
        result = agent.execute(
            goal=request.goal,
            input_file=request.input_file
        )

        # Ensure the 'output' directory exists before writing
        if not os.path.exists('output'):
            os.makedirs('output')

        # For demonstration, let's write something to output.txt if it doesn't exist
        # In a real scenario, the agent.execute would handle file output
        if not os.path.exists("output/output.txt"):
            with open("output/output.txt", "w", encoding="utf-8") as f:
                f.write("Goal: {}, Input File: {}\n".format(request.goal, request.input_file))
                f.write("Agent Result (placeholder): {}\n".format(result))

        with open("output/output.txt", "r", encoding="utf-8") as f:
            output_text = f.read()

        return {
            "status": "success",
            "message": result,
            "output": output_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''

with open('main.py', 'w') as f:
    f.write(app_content)

print("Created main.py with your FastAPI application.")

# Now that `main.py` is created, you can run Uvicorn as a background process. This will start your FastAPI server. Colab typically provides a public URL (like an ngrok URL) that you can use to access your API endpoints, for example, by navigating to `/docs` for the Swagger UI (`<colab_url>/docs`).


# Start Uvicorn as a background process. The `&` symbol runs it in the background.
# `main:app` refers to the `app` object in the `main.py` file.
!uvicorn main:app --host 0.0.0.0 --port 8000 &

import os

# Create the 'app' directory if it doesn't exist
if not os.path.exists('app'):
    os.makedirs('app')

# Create the 'app/agent' directory if it doesn't exist
if not os.path.exists('app/agent'):
    os.makedirs('app/agent')

print("Created 'app' and 'app/agent' directories.")

# Create __init__.py files to make 'app' and 'app.agent' Python packages
with open('app/__init__.py', 'w') as f:
    f.write('')

with open('app/agent/__init__.py', 'w') as f:
    f.write('')

print("Created '__init__.py' files.")

# Create a placeholder executor.py file with a basic Executor class
executor_content = """
class Executor:
    def execute(self, goal: str, input_file: str):
        print(f"Executing agent with goal: {goal} and input file: {input_file}")
        # Placeholder for actual agent logic
        return "Agent execution completed (placeholder)."
"""

with open('app/agent/executor.py', 'w') as f:
    f.write(executor_content)

print("Created 'app/agent/executor.py' with a placeholder Executor class.")

uvicorn app.api:app --reload