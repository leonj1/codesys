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