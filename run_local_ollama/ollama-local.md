# Reroute OpenAI API calls to your local Ollama server. It is a drop-in replacement to OpenAI GPT models. 

## ENV VARIABLES
```sh
$OPENAI_API_BASE='http://localhost:11434/v1'
$OPENAI_MODEL_NAME='crewai-llama3'  
$OPENAI_API_KEY=''
```

## CHANGE IN CODE

In the client application, replace "OPEN_AI_API", "model" and "base_url" to your Ollama API (default: "http://localhost:11434/v1")

```py
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model = "crewai-llama3",
    base_url = "http://localhost:11434/v1")
```
`
## Create Model - "crewai-llama3"

`./create-llama3.sh`
(ollama create crewai-llama3 -f Modelfile)

## Launch Tool

Ex. python ./1MathProfessor_ollama_crewai-llama3/MathProfessor.py
