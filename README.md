# Multi-GPTBot Deployment Guide

This guide explains how to set up a multi-bot environment using the Multi-GPTBot repository. The setup involves using submodules in Git to manage multiple Telegram bots, each as a separate submodule within a single project framework.

## Repository Structure

The Multi-GPTBot project is structured as follows:

```
multi-gptbot/
├── bot1/
├── bot2/
└── main.py
```

- `multi-gptbot/`: The root directory of the project.
- `bot1/`, `bot2/`: Subdirectories for each bot, implemented as Git submodules.
- `main.py`: Central script located in the root directory to run and manage all bots.

## Initial Setup

1. **Cloning the Repository**:
   Clone the repository with submodules:
   ```bash
   git clone --recurse-submodules https://github.com/andykras/multi-gptbot.git
   ```

2. **Adding a New Bot**:
   To add a new bot as a submodule:
   ```bash
   cd multi-gptbot
   git submodule add https://github.com/path/to/your/bot.git bot3
   ```

## Configuration

Each bot can have its own configurations, but since they share the same environment, you need to set API keys and tokens directly in the bot's Python files, not through environment variables. For example, in `env.py` of each bot:

```python
API_KEY = "your-api-key-here"
```

Replace `your-api-key-here` with the actual API key of your bot.

## Running the Bots

To start all the bots using the `main.py` script:

```bash
LC_ALL=ru_RU LOG_LEVEL=INFO python main.py
```

This script initializes and runs each bot configured as a submodule. To stop the bots, press `Ctrl+C` in the terminal.

## Managing Bots

- Each bot's code and configuration are managed independently within their respective submodules.
- Remember to commit and push changes within each bot's submodule and then update the reference in the main repository.

This multi-bot setup allows for centralized management while maintaining independent development and control for each bot.
