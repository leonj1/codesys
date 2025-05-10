from codesys import Agent

# Initialize with a working directory
agent = Agent(working_dir="/Users/seansullivan/lmsys-sdk/")

# Run Claude with a prompt and automatically print streaming output
lines = agent.run("""/init""", stream=True)

