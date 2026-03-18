# Credibly
AI agent used for verifying information and credibility of sources
## Installation
Please note these facts, before installing Credibly:
  **Firstly**, it will take some space, because of downloading the ollama model on your device.
  **Secondly**, 
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
