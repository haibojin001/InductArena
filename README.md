# Reasoning Can Hurt the Inductive Abilities of Large Language Models

This repository contains the official codebase for **Reasoning Can Hurt the Inductive Abilities of Large Language Models**. The project includes both a minimal working **demo** (`demo.py`) and a full **implementation** (`game.py`) for reproducing our experiments and analyses.

# Update
- **2025-05-29**: Initial release of the repository.
  
# Models
This project supports multiple LLMs via API calls. You will need valid API keys for the following services:

- **OpenAI**: Used for models like GPT-4o.  
  ➤ Set your API key as an environment variable or in a `.env` file:
  
  ```bash
  export OPENAI_API_KEY=your-key-here
  
# Environment Setup
To set up the environment, use Conda to create a new environment with the required dependencies.
## Step 1: Create a Conda Environment
```
conda create -n InductArena python=3.10
conda activate InductArena
pip install torch torchvision transformers openai==1.66.3
```
## Step 2: Run game.py
