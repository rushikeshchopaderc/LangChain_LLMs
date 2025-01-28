# DeepSeek Model importing

## 1) Always use a virtual environment for the repository
Steps: (In the Command line)
- !python3.13 -m venv .venv
- source .venv/bin/activate
(Download all the requirements given in the requirements.txt file to import deepseek model using langchain)

## 2) Download Ollama for windows/mac from the official website and choose the model you want to use 
For the deepseek model, run the command in the terminal
$ ollama run deepseek-r1:1.5b

To list all the models, run the command
$ ollama list

To remove a model, run the command: 
$ ollama rm deepseek-r1:1.5b
