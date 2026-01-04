# Generated from: AgenticAI.ipynb
# Converted at: 2026-01-04T17:09:11.571Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# app/agent/planner.py

class Planner:
    def plan(self, goal: str):
        goal = goal.lower()
        steps = []

        if "summarize" in goal:
            steps.extend([
                "read_file",
                "summarize_text",
                "write_file"
            ])

        elif "analyze" in goal:
            steps.extend([
                "read_file",
                "analyze_text",
                "write_file"
            ])

        return steps


import os

# Create the directory structure
!mkdir -p app/agent app/tools app/utils

# Create empty __init__.py files to make them Python packages
!touch app/__init__.py app/agent/__init__.py app/tools/__init__.py app/utils/__init__.py

print("Directory structure and __init__.py files created.")

%%writefile app/agent/planner.py
# app/agent/planner.py

class Planner:
    def plan(self, goal: str):
        goal = goal.lower()
        steps = []

        if "summarize" in goal:
            steps.extend([
                "read_file",
                "summarize_text",
                "write_file"
            ])

        elif "analyze" in goal:
            steps.extend([
                "read_file",
                "analyze_text",
                "write_file"
            ])

        return steps

%%writefile app/agent/memory.py
# app/agent/memory.py

class AgentMemory:
    def __init__(self):
        self.memory = []

    def store(self, content: str):
        self.memory.append(content)

    def retrieve(self):
        return self.memory

%%writefile app/tools/file_tools.py
# app/tools/file_tools.py

import os

def read_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return ""
    with open(filepath, 'r') as f:
        content = f.read()
    print(f"Read content from {filepath} (length: {len(content)})")
    return content

def write_file(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Content written to {filepath} (length: {len(content)})")

%%writefile app/tools/text_tools.py
# app/tools/text_tools.py

def summarize_text(text: str) -> str:
    print(f"Summarizing text (length: {len(text)})...")
    # Placeholder for actual summarization logic
    if len(text) > 100:
        return f"Summary of: {text[:100]}..."
    return f"Summary of: {text}"

def analyze_text(text: str) -> str:
    print(f"Analyzing text (length: {len(text)})...")
    # Placeholder for actual analysis logic
    if len(text) > 100:
        return f"Analysis of: {text[:100]}..."
    return f"Analysis of: {text}"

%%writefile app/utils/logger.py
# app/utils/logger.py

import logging

def get_logger(name='agent_logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

%%writefile app/agent/executor.py
# app/agent/executor.py

from app.agent.planner import Planner
from app.agent.memory import AgentMemory
from app.tools.file_tools import read_file, write_file
from app.tools.text_tools import summarize_text, analyze_text
from app.utils.logger import get_logger

logger = get_logger()

class Executor:
    def __init__(self):
        self.planner = Planner()
        self.memory = AgentMemory()

    def execute(self, goal: str, input_file: str):
        logger.info(f"Goal received: {goal}")
        steps = self.planner.plan(goal)

        context = ""

        for step in steps:
            logger.info(f"Executing step: {step}")

            if step == "read_file":
                context = read_file(input_file)
                self.memory.store(context)

            elif step == "summarize_text":
                context = summarize_text(context)
                self.memory.store(context)

            elif step == "analyze_text":
                context = analyze_text(context)
                self.memory.store(context)

            elif step == "write_file":
                write_file("output/output.txt", context)

        return "✅ Task completed successfully"

%%writefile app/main.py
# app/main.py

from app.agent.executor import Executor

if __name__ == "__main__":
    agent = Executor()
    result = agent.execute(
        goal="Summarize the document",
        input_file="data/sample.txt"
    )
    print(result)

%%writefile data/sample.txt
This is a sample document for summarization. It contains multiple sentences and some information. The agent should be able to read this file, process its content, and then provide a summary. This is the third sentence. Let's see if the summarization works as expected.

!python app/main.py

# app/agent/memory.py

class AgentMemory:
    def __init__(self):
        self.history = []

    def store(self, data):
        self.history.append(data)

    def recall(self):
        return self.history


# app/tools/file_tools.py

def read_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# app/tools/text_tools.py

def summarize_text(text: str) -> str:
    sentences = text.split(".")
    return ".".join(sentences[:3]) + "."

def analyze_text(text: str) -> str:
    word_count = len(text.split())
    char_count = len(text)

    return (
        f"Text Analysis:\n"
        f"Words: {word_count}\n"
        f"Characters: {char_count}\n"
    )


# app/utils/logger.py

import logging

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("AgenticAI")


import os

# Create the directory structure
!mkdir -p app/agent app/tools app/utils data output

# Create empty __init__.py files to make them Python packages
!touch app/__init__.py app/agent/__init__.py app/tools/__init__.py app/utils/__init__.py

print("Directory structure and __init__.py files created.")

%%writefile app/agent/planner.py
# app/agent/planner.py

class Planner:
    def plan(self, goal: str):
        goal = goal.lower()
        steps = []

        if "summarize" in goal:
            steps.extend([
                "read_file",
                "summarize_text",
                "write_file"
            ])

        elif "analyze" in goal:
            steps.extend([
                "read_file",
                "analyze_text",
                "write_file"
            ])

        return steps

%%writefile app/agent/memory.py
# app/agent/memory.py

class AgentMemory:
    def __init__(self):
        self.memory = []

    def store(self, content: str):
        self.memory.append(content)

    def retrieve(self):
        return self.memory

%%writefile app/tools/file_tools.py
# app/tools/file_tools.py

import os

def read_file(filepath: str) -> str:
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return ""
    with open(filepath, 'r') as f:
        content = f.read()
    print(f"Read content from {filepath} (length: {len(content)})")
    return content

def write_file(filepath: str, content: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Content written to {filepath} (length: {len(content)})")

%%writefile app/tools/text_tools.py
# app/tools/text_tools.py

def summarize_text(text: str) -> str:
    print(f"Summarizing text (length: {len(text)})...")
    # Placeholder for actual summarization logic
    if len(text) > 100:
        return f"Summary of: {text[:100]}..."
    return f"Summary of: {text}"

def analyze_text(text: str) -> str:
    print(f"Analyzing text (length: {len(text)})...")
    # Placeholder for actual analysis logic
    if len(text) > 100:
        return f"Analysis of: {text[:100]}..."
    return f"Analysis of: {text}"

%%writefile app/utils/logger.py
# app/utils/logger.py

import logging

def get_logger(name='agent_logger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

%%writefile app/agent/executor.py
# app/agent/executor.py

from app.agent.planner import Planner
from app.agent.memory import AgentMemory
from app.tools.file_tools import read_file, write_file
from app.tools.text_tools import summarize_text, analyze_text
from app.utils.logger import get_logger

logger = get_logger()

class Executor:
    def __init__(self):
        self.planner = Planner()
        self.memory = AgentMemory()

    def execute(self, goal: str, input_file: str):
        logger.info(f"Goal received: {goal}")
        steps = self.planner.plan(goal)

        context = ""

        for step in steps:
            logger.info(f"Executing step: {step}")

            if step == "read_file":
                context = read_file(input_file)
                self.memory.store(context)

            elif step == "summarize_text":
                context = summarize_text(context)
                self.memory.store(context)

            elif step == "analyze_text":
                context = analyze_text(context)
                self.memory.store(context)

            elif step == "write_file":
                write_file("output/output.txt", context)

        return "✅ Task completed successfully"

%%writefile app/main.py
# app/main.py

import sys
import os

# Ensure the current directory (where 'app' is) is in sys.path
# In Colab, the root directory for mounted files is often '/content/'
# We add it if not already present to avoid duplicates
if '/content/' not in sys.path:
    sys.path.insert(0, '/content/')

from app.agent.executor import Executor

if __name__ == "__main__":
    agent = Executor()
    result = agent.execute(
        goal="Summarize the document",
        input_file="data/sample.txt"
    )
    print(result)

%%writefile data/sample.txt
This is a sample document for summarization. It contains multiple sentences and some information. The agent should be able to read this file, process its content, and then provide a summary. This is the third sentence. Let's see if the summarization works as expected.

!python app/main.py

import sys
import os

# Add the current working directory to sys.path to allow importing from 'app'
# In Colab, the root directory for mounted files is often '/content/'
if '/content/' not in sys.path:
    sys.path.insert(0, '/content/')

from app.agent.executor import Executor

# Test the import
print("Executor imported successfully!")

import sys
import os

# Fix import path (Colab / local)
if '/content/' not in sys.path:
    sys.path.insert(0, '/content/')

from app.agent.executor import Executor

# 1️⃣ Create agent instance
agent = Executor()

# 2️⃣ Execute agent with goal and input file
result = agent.execute(
    goal="Summarize the document",
    input_file="data/sample.txt"
)

# 3️⃣ Print result
print(result)

# 4️⃣ Read output file to VERIFY result
with open("output/output.txt", "r", encoding="utf-8") as f:
    print("\n--- AGENT OUTPUT ---")
    print(f.read())


{
  "goal": "Summarize the document",
  "input_file": "data/sample.txt"
}