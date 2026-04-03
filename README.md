# Terminal Buddy

Terminal Buddy is a specialized Python-based command-line tool that leverages local Large Language Models (LLMs) via Ollama to convert plain English instructions into Bash commands. It provides a straightforward interface to generate and safely execute shell scripts.

## Features

- Converts natural English prompts into executable Bash commands.
- Allows selection among different local language models available in your Ollama installation.
- Built-in security restrictions to block any commands involving 'sudo' or administrative privileges.
- Prompts for user confirmation before executing any generated command.

## Prerequisites

- Python 3.x
- Ollama installed and running locally.
- At least one model pulled in Ollama (e.g., 'ollama pull llama3').

## Setup

1. Set up a virtual environment:
   ```bash
   python -m venv terminal_buddy_venv
   source terminal_buddy_venv/bin/activate
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Execute the script by passing your prompt as an argument. You can also specify an optional model index.

**Basic Usage:**
```bash
python terminal_buddy.py "list all text files in the current directory"
```

**Specifying a Model Index:**
```bash
python terminal_buddy.py 2 "find all python files modified in the last 7 days"
```

The application will present the generated command and prompt you for confirmation before execution.

## Example Commands to Try

**1. File Management**
- Create a file: `"create a python file named app.py"`
- Create a folder: `"make a directory called backups"`
- Move files: `"move all .txt files to the backups folder"`
- Rename: `"rename old_script.py to main.py"`

**2. Searching & Finding**
- Find specific files: `"find all javascript files in this folder"`
- Find recent files: `"list all files modified in the last hour"`
- Search inside files: `"search for the word 'database' in all python files"`

**3. System Info & File Details**
- Check file type: `"what kind of file is data.bin"`
- Check disk space: `"how much free space is left on my drive"`
- List with details: `"show me all files including hidden ones with their sizes"`

**4. Developer Shortcuts**
- Count lines: `"count how many lines of code are in main.py"`
- Check Python version: `"check which version of python is currently active"`
- Environment check: `"list all installed python packages"`

## Output Example

![Terminal Buddy Output](output.png)
