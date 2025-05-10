# codesys SDK

A Python SDK for interacting with the Claude CLI tool.

## Installation

```bash
pip install codesys
```

## Requirements

- Python 3.8+
- Claude CLI tool must be installed, available in your PATH, and set up with your api key.

## Quick Start

```python
from codesys import Agent

# Initialize with a working directory
agent = Agent(working_dir="/path/to/your/project")

# Run Claude with a prompt
result = agent.run("Your prompt here")
print(result)

# Auto-streaming output (prints automatically)
lines = agent.run("Generate a story", stream=True)

# Manual streaming (if you need more control)
process = agent.run("Another prompt", stream=True, auto_print=False)
for line in process.stdout:
    print(line, end="")
```

## Features

- Simple interface to the Claude CLI tool
- Support for all Claude CLI options
- Automatic or manual streaming output
- Customizable tool access

## API Reference

### Agent Class

```python
Agent(working_dir=None, allowed_tools=None)
```

**Parameters:**
- `working_dir` (str, optional): The working directory for Claude to use. Defaults to current directory.
- `allowed_tools` (list, optional): List of tools to allow Claude to use. Defaults to ["Edit", "Bash", "Write"].

### Methods

#### run

```python
run(prompt, stream=False, output_format=None, additional_args=None, auto_print=True)
```

Run Claude with the specified prompt.

**Parameters:**
- `prompt` (str): The prompt to send to Claude.
- `stream` (bool): If True, handles streaming output. If False, returns the complete output.
- `output_format` (str, optional): Optional output format (e.g., "stream-json").
- `additional_args` (dict, optional): Additional arguments to pass to the Claude CLI.
- `auto_print` (bool): If True and stream=True, automatically prints output. If False, you need to handle streaming manually.

**Returns:**
- If `stream=False`: Returns the complete output as a string.
- If `stream=True` and `auto_print=False`: Returns a subprocess.Popen object for manual streaming.
- If `stream=True` and `auto_print=True`: Automatically prints output and returns collected lines as a list.

#### run_with_tools

```python
run_with_tools(prompt, tools, stream=False, auto_print=True)
```

Run Claude with specific allowed tools.

**Parameters:**
- `prompt` (str): The prompt to send to Claude.
- `tools` (list): List of tools to allow Claude to use.
- `stream` (bool): If True, handles streaming output.
- `auto_print` (bool): If True and stream=True, automatically prints output.

**Returns:**
- If `stream=False`: Returns the complete output as a string.
- If `stream=True` and `auto_print=False`: Returns a subprocess.Popen object.
- If `stream=True` and `auto_print=True`: Automatically prints output and returns collected lines.

## Example: Automatic Streaming

```python
from codesys import Agent

agent = Agent()
# This will automatically print the output line by line
lines = agent.run("Generate a short story", stream=True)
```

## Example: Manual Streaming with JSON parsing

```python
from codesys import Agent
import json

agent = Agent()
process = agent.run("Generate a short story", stream=True, output_format="stream-json", auto_print=False)

for line in process.stdout:
    if line.strip():
        try:
            data = json.loads(line)
            print(data.get("content", ""))
        except json.JSONDecodeError:
            print(f"Error parsing JSON: {line}")
```

# Examples

```python
from codesys import Agent

# Initialize with a working directory
agent = Agent(working_dir="/Users/seansullivan/lmsys-sdk/")

# Run Claude with a prompt and automatically print streaming output
lines = agent.run("create another example of example1_custom_tools.py which shows how to use read only tools. note the source code of the sdk in codesys/agent.py", stream=True)

```

```python
"""
Example 1: Customizing tools during initialization

This example demonstrates how to initialize an Agent with only specific tools.
"""

from codesys import Agent

# Initialize with only specific tools
restricted_agent = Agent(
    working_dir="./",
    allowed_tools=["Edit", "Write", "View"]  # Only allow editing, writing files and viewing
)  # Implementation in agent.py lines 19-39

print(f"Agent initialized with tools: {restricted_agent.allowed_tools}")
```

```python

from codesys import Agent

# Initialize with default tools
agent = Agent(working_dir="./")  # Implementation in agent.py lines 19-39
print(f"Default tools: {agent.allowed_tools}")

# Run with only specific tools for one operation
bash_only_response = agent.run_with_tools(
    prompt="List files in the current directory",
    tools=["Bash"],  # Only allow Bash for this specific run
    stream=False
)  # Implementation in agent.py lines 132-155

print(f"Tools after run_with_tools: {agent.allowed_tools}  # Original tools are restored")
```

```python
"""
Example 3: Manual handling of streaming output

This example demonstrates how to manually handle streaming output from the agent.
"""

from codesys import Agent
import json
import time

# Initialize an agent
agent = Agent(working_dir="./")

# Get a process for streaming manually
process = agent.run(
    prompt="Explain what an LLM Agent is in 3 sentences",
    stream=True,
    auto_print=False  # Don't auto-print, we'll handle the output manually
)  # Implementation in agent.py lines 41-96 (stream=True, auto_print=False path)

print("Streaming output manually, processing each line:")
for i, line in enumerate(process.stdout):
    # Parse the JSON line
    try:
        data = json.loads(line)
        # Do something with each piece of output
        print(f"Line {i+1}: {data.get('content', '')}")
    except json.JSONDecodeError:
        print(f"Raw line: {line}")

    # Simulate processing time
    time.sleep(0.1)
    # Compare with agent.py lines 98-116 (auto-handling of streaming)
```

```python
"""
Example 4: Using output formats and additional arguments

This example demonstrates how to use different output formats and pass additional arguments.
"""

from codesys import Agent

# Initialize an agent
agent = Agent(working_dir="./")

# Run with custom output format and additional arguments
response = agent.run(
    prompt="What can you tell me about this codebase?",
    output_format="json",  # Request JSON output
    additional_args={
        "temperature": 0.7,     # Set temperature
        "max-tokens": 500,      # Limit output tokens
        "silent": True          # Suppress progress output
    }
)  # Implementation in agent.py lines 41-70 (output_format handling), 74-80 (additional_args)

print(f"Response type: {type(response)}")
print("First 100 characters of response:", response[:100] if isinstance(response, str) else "Not a string")
```



## License

MIT
#### CodeSYS
