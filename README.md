# pineconeless-babyagi

This is a modification of baby agi to remove all dependency on pinecone

# Objective
This Python script is an example of an AI-powered task management system. The system uses OpenAI's natural language processing (NLP) capabilities to create, prioritize, and execute tasks. The main idea behind this system is that it creates tasks based on the result of previous tasks and a predefined objective. The script uses local CSV and JSON files to store and retrieve embeddings for context.

This README will cover the following:

How the script works
How to use the script
Warning about running the script continuously

# How It Works
The script works by running an infinite loop that does the following steps:

Pulls the first task from the task list.
Sends the task to the execution agent, which uses OpenAI's API to complete the task based on the context.
Enriches the result and stores it in a local JSON file.
Creates new tasks and reprioritizes the task list based on the objective and the result of the previous task.
The execution_agent() function is where the OpenAI API is used. It takes two parameters: the objective and the task. It then sends a prompt to OpenAI's API, which returns the result of the task. The prompt consists of a description of the AI system's task, the objective, and the task itself. The result is then returned as a string.

The task_creation_agent() function is where OpenAI's API is used to create new tasks based on the objective and the result of the previous task. The function takes four parameters: the objective, the result of the previous task, the task description, and the current task list. It then sends a prompt to OpenAI's API, which returns a list of new tasks as strings. The function then returns the new tasks as a list of dictionaries, where each dictionary contains the name of the task.

The prioritization_agent() function is where OpenAI's API is used to reprioritize the task list. The function takes one parameter, the ID of the current task. It sends a prompt to OpenAI's API, which returns the reprioritized task list as a numbered list.

Finally, the script uses local CSV and JSON files to store and retrieve embeddings for context. The script reads a CSV file containing the embeddings and corresponding task names, and a JSON file containing additional metadata. When a task is completed, the script stores the result and metadata in the JSON file, and updates the embeddings CSV file. The embeddings for a task are used to create context when creating new tasks and prioritizing the task list.

# How to Use
To use the script, you will need to follow these steps:

Install the required packages: pip install -r requirements.txt
Copy the .env.example file to .env: cp .env.example .env. This is where you will set the following variables.
Set your OpenAI API key in the OPENAI_API_KEY variable.
Set the objective of the task management system in the OBJECTIVE variable. Alternatively, you can pass it to the script as a quote argument.
./babyagi.py ["<objective>"]
Set the first task of the system in the FIRST_TASK variable.
Run the script.

# Warning
This script is designed to be run continuously as part of a task management system. Running this script continuously can result in high API usage, so please use it responsibly. Additionally, the script requires the OpenAI API to be set up correctly, so make sure you have set up the API before running the script.