#!/bin/sh

# Set env variables for Ollama as a drop-in replacement for OpenAI API

echo "********************************************"
echo " *------SETTING OLLAMA ENV VARIABLES------*"
echo "********************************************                 

export OPENAI_API_BASE='http://localhost:11434/v1'
export OPENAI_MODEL_NAME='crewai-llama3'
export OPENAI_API_KEY='' 

# No need to use an API key

# Run 'ollama create crewai-llama3 -f Modelfile' to create the "crewai-llama3" model.





