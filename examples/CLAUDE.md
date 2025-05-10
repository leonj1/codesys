# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the **codesys SDK**, a Python package that provides a simple interface for interacting with the Claude CLI tool. The SDK allows users to programmatically send prompts to Claude, control which tools Claude can use, and manage output streaming.

## Code Structure

- `codesys/agent.py`: Core implementation of the Agent class
- `codesys/__init__.py`: Exports Agent class and defines version
- Example files (example1_custom_tools.py, etc.): Demonstrate various SDK features

## Key Components

### Agent Class

The main class for interacting with the Claude CLI tool. Located in `codesys/agent.py`.

Core functionality:
- `__init__`: Initialize with working directory and allowed tools
- `run`: Main method to execute Claude with a prompt and various options
- `run_with_tools`: Temporarily override allowed tools for a single execution

## Development Commands

### Installation

```bash
# Install in development mode
pip install -e .

# Install from PyPI (when published)
pip install codesys
```

### Building and Distribution

```bash
# Build the package
python -m build

# Run tests (if/when tests are added)
pytest

# Build distribution packages
python -m build
```

### Running Examples

```bash
# Run an example
python example1_custom_tools.py

# Run the example with read-only tools
python example7_read_only_tools.py
```

## Important Considerations

1. **Tool Control**: The SDK allows fine-grained control over which tools Claude can use (Bash, Edit, Write, etc.)
2. **Streaming**: Both automatic and manual streaming modes are supported
3. **Error Handling**: The SDK handles Claude CLI errors and provides meaningful error messages
4. **Output Formats**: Support for various output formats including json and stream-json

## Prerequisites

- Python 3.8 or higher
- Claude CLI tool must be installed and available in the system PATH