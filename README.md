# ClaimCheckAI
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

# Installation

Please note these facts, before installing:
  - It will take some space. Disk space used on the device may vary depending on downloaded Ollama model

## Windows

This installation process will download [Ollama](https://ollama.com/) model on your device.
1. Ollama installatinon

  You can try different model, that will be more compatible with your hardware, if you want. Please look at the [Recommended Ollama models](#recommended-ollama-models) section.
  ```
  irm https://ollama.com/install.ps1 | iex
  ollama pull llama3:8b # You can swap this with different model
  ```
2. Clone the repository
  ```
  got clone https://github.com/nakoledomu/ClaimCheckAI.git
  cd ClaimCheckAI
  ```
3. Setup python
  ```
  python -m venv .\venv\
  .\venv\Scripts\activate  
  pip install -r .\requirements.txt
  ```
4. Launch

  You can now launch Credible by running main.py in the `.\venv\` virtual environment (or install requirements and launch everything globaly)
  Go to your cloned SourceLens repo and run this:
  ```
  .\venv\Scripts\activate
  .\main.py
  ```
  SourceLens should launch. Performance may very depending on your hardware.

# Recommended Ollama Models

This project runs locally using [Ollama](https://ollama.com/). For best results, choose a model with solid reasoning ability, since credibility evaluation requires structured analysis and nuance.

If unsure, start with `llama3:8b` — it provides the best overall performance for credibility and verification tasks in this project.

### Recommended (Balanced Performance)
  
  `llama3:8b`
  
  - Best balance between reasoning quality and hardware requirements
  
  - Good at structured, analytical responses
  
  - Works well on machines with 16GB RAM
  
  ```
  ollama pull llama3:8b
  ```

### Lightweight Option (Lower RAM)

  `mistral:7b`
  
  - Faster and more memory-efficient
  
  - Suitable for machines with 8GB RAM
  
  - Slightly weaker reasoning compared to Llama 3
  
  ```
  ollama pull mistral:7b
  ```
### Higher Reasoning Power (Stronger Hardware)

  `llama3:13b`
  
  - Better analytical depth and consistency
  
  - Recommended if you have 24GB+ RAM or a capable GPU
  
  ```
  ollama pull llama3:13b
  ```
