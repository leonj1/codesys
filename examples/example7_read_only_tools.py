"""
Example 7: Using read-only tools

This example demonstrates how to initialize an Agent with only read-only tools,
which can be useful for analysis tasks where file modifications should be prevented.
"""

from codesys import Agent

# Initialize with only read-only tools
read_only_agent = Agent(
    working_dir="./",
    allowed_tools=[
        "View",        # For reading files
        "GlobTool",    # For finding files by pattern
        "GrepTool",    # For searching file contents
        "LSTool",      # For listing directory contents
        "WebFetchTool" # For fetching web content
    ]
)  # Implementation in agent.py lines 19-39

# Prompt that demonstrates the read-only nature
prompt = """
generate a plan which lays out how 
"""

print(f"Agent initialized with read-only tools: {read_only_agent.allowed_tools}")
print("\nRunning Claude with read-only permissions...\n")

# Run Claude with the prompt
response = read_only_agent.run(prompt)

# Print the completion of the task
print("\nAnalysis task completed with read-only permissions.")