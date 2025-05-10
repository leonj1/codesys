"""
Advanced usage examples for the LMSYS Agent SDK.

This file demonstrates:
1. How to customize tools for the agent
2. How to use the run_with_tools method
3. How to handle streaming output manually
4. How to use additional arguments and output formats
5. Error handling
"""

from codesys import Agent
import os
import json
import time

# -----------------------------------------------------
# Example 1: Customizing tools during initialization
# -----------------------------------------------------
print("\n--- Example 1: Customizing tools during initialization ---")

# Initialize with only specific tools
restricted_agent = Agent(
    working_dir="./",
    allowed_tools=["Edit", "Write", "View"]  # Only allow editing, writing files and viewing
)  # Implementation in agent.py lines 19-39

print(f"Agent initialized with tools: {restricted_agent.allowed_tools}")

# -----------------------------------------------------
# Example 2: Using run_with_tools for temporary tool changes
# -----------------------------------------------------
print("\n--- Example 2: Using run_with_tools for temporary tool changes ---")

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

# -----------------------------------------------------
# Example 3: Manual handling of streaming output
# -----------------------------------------------------
print("\n--- Example 3: Manual handling of streaming output ---")

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

# -----------------------------------------------------
# Example 4: Using output formats and additional arguments
# -----------------------------------------------------
print("\n--- Example 4: Using output formats and additional arguments ---")

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

# -----------------------------------------------------
# Example 5: Error handling
# -----------------------------------------------------
print("\n--- Example 5: Error handling ---")

try:
    # Attempt to use an invalid configuration
    agent.run(
        prompt="This should fail",
        additional_args={"invalid_param": True}  # Invalid parameter
    )  # Implementation in agent.py lines 119-130 (error handling in subprocess.run)
except Exception as e:
    print(f"Caught expected error: {str(e)}")

# -----------------------------------------------------
# Example 6: Working with different project directories
# -----------------------------------------------------
print("\n--- Example 6: Working with different project directories ---")

# Create an agent for a specific project
project_agent = Agent(working_dir=os.path.expanduser("~/my-project"))  # Implementation in agent.py lines 19-27 (working_dir parameter)

# Run a prompt related to that project
print("Running agent in a specific project directory...")
# Commented out to avoid actual execution:
# project_agent.run("Summarize this project", stream=True)  # Implementation in agent.py line 91 (cwd=self.working_dir)

print("Advanced examples completed!")
