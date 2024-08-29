# ollama-api
An API wrapper for Ollama


## Getting Started

## Doing More

1. Install Ollama

[https://ollama.com/](https://ollama.com/)

2. Pull a model

```bash
ollama run llama3.1
```

3. Make an environment and have fun

### Windows

```bash
# make an environment
python -m venv .

# activate environment
./bin/Activate.ps1
```

### Linux & MacOS

```bash
# make an environment
python -m venv .

# activate environment
source ./bin/activate
```

## Want more?

Local alternative to GitHub Copilot

See here for using models from Ollama to create a self-hosted version of GitHub Copilot

[https://llama.meta.com/docs/integration-guides/meta-code-llama](https://llama.meta.com/docs/integration-guides/meta-code-llama)

Doing this requires a VSCode extension, "Continue". This link shows an example config 
file for choosing a locally available model.

[https://gist.github.com/pythoninthegrass/9ec5d6e9e05b96272bb21d8a8ce2ca11](https://gist.github.com/pythoninthegrass/9ec5d6e9e05b96272bb21d8a8ce2ca11)

Run this to check which ollama models are available:

```bash
ollama list
```