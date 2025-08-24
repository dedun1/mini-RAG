# mini - rag

this is a minimal implementation of the rag model for question answering 

# requirements

- python 3.8 or later

### install python using MiniConda

1) download and install Miniconda from [here] (url)
2) create a new env using following command : 
bash'''
$conda create -n mini-rag python=3.8
3) activate the environment:
'''bash
$conda activate mini-rag 

### (Optional) Setup you command line for better readablitiy

'''bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$"
'''

# Installation 

### Install the required packages
'''bash
pip install -r requirements.txt
'''

### Setup the environment variables

'''bash
$ cp .env.example .env
'''

#Set your environment vairables in the '.env' file Like 'OPENAI_API_KEY' value.

# RUN the FASTAPI server 

'''bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
'''
## POSTMAN COLLECTION

Download the postman collection from [/assets/mini-rag-app/postman_collection.json]