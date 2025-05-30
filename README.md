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

## Directory Structure

```text
.
├── chess/
│   ├── create_chess/             # Data generation for Chess
│   ├── evaluate_chess/           # LLM-based rule inference + evaluation

├── Texas_holdem/
│   ├── create_texas_holdem/      # Hand construction with NR/SR rules
│   ├── evaluate_texas_holdem/    # Reasoning + rule validation
├── Dice/
│   ├── create_dice_game/         # Dice roll generation under mixed rules
│   ├── evaluate_dice_game/       # Rule-based LLM evaluation
├── BJ/
│   ├── create_blackjack/         # Blackjack hand generation
│   ├── evaluate_blackjack/       # Reasoning evaluation
```

# Environment Setup
To set up the environment, use Conda to create a new environment with the required dependencies.
## Step 1: Create a Conda Environment
```
conda create -n InductArena python=3.10
conda activate InductArena
pip install torch torchvision transformers openai==1.66.3
```
## Step 2: Generate Data
We take Chess as an example.
To generate gameplay episodes with sampled Normal and Special Rules:
```
cd Chess/create_chess
python generate_data.py
```

## Step 3: Evaluation
To evaluate the model's ability to infer rules from the generated data:
```
cd Chess/evaluate_chess
python run_evaluation.py
```
# TODO

We currently include a sample Chess episode in `data/chess/` as an example.

We plan to release additional example transcripts for the following tasks:

- [ ] Texas Hold’em
- [ ] Dice Games
- [ ] Blackjack

These will be added under the `data/` directory in future updates.

Multiple models have already been evaluated in our experiments, including:
- GPT-4o
- Claude
- Gemini
- DeepSeek
- Qwen

We plan to unify their inference interfaces in future releases to make model benchmarking easier and more extensible.