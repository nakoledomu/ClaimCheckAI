# Credibly
AI agent used for verifying information and credibility of sources

## Disclaimer

This project is an experimental AI system designed to assist with evaluating the credibility of information sources and claims. It is intended for research, educational, and development purposes only.

The system:

- Uses large language models (LLMs) to analyze information.

- May rely on external data sources, search results, or model training knowledge.

- Can produce incorrect, incomplete, outdated, or misleading information.

- Does not guarantee factual accuracy.

This tool does not replace professional fact-checking, journalistic investigation, legal advice, academic research, or expert review.

Users are responsible for independently verifying any information before relying on it. The creators and contributors of this project are not liable for decisions made based on the system’s outputs.

Use at your own discretion.

## Installation

Please note these facts, before installing Credibly:
  - It will take some space. Disk space used on the device may vary depending on downloaded Ollama model

### Windows

This installation process will download Ollama model on your device. For more information about Ollama visit their [official site](https://ollama.com/)
1. Ollama installatinon
  You can try different model, that will be more compatible with your hardware, if you want. Please look at the [Recomended Ollama models](#recomended-ollama-models) section.
  ```
  irm https://ollama.com/install.ps1 | iex
  ollama pull llama3:8b # You can swap this with different model
  ```
2. Clone the repository
  ```
  git clone https://github.com/nakoledomu/Credibly.git
  cd Credibly
  ```
3. Setup python
  ```
  python -m venv .\venv\
  .\venv\Scripts\activate  
  pip install -r .\requirements.txt
  ```
4. Launch

  You can now launch Credible by running main.py in the `.\venv\` virtual environment (or install requirements and launch everything globaly)
  Go to your cloned Credibly repo and run this:
  ```
  .\venv\Scripts\activate
  .\main.py
  ```
  Credibly should launch. Performance of Credibly may very depending on your hardware.

## Recomended Ollama models

