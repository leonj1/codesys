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