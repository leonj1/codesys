from codesys import Agent


# Agents CANNOT see past conversations. You can see this through running this code:


# Initialize with a working directory
agent = Agent(working_dir="./")

# First session - send "hello"
print("First session:")
response1 = agent.run("hello", stream=True)
print("\n")



# Start a new session
print("New session:")
response2 = agent.run("what did i just say?", stream=True)

