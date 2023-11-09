# Console-GPT Chatbot

## Your Backup for ChatGPT Downtimes

### Overview

This repository hosts an interactive chatbot, designed as a dependable fallback when ChatGPT faces outages. Powered by OpenAI's GPT models and utilizing the still-operational OpenAI API, it ensures ongoing, AI-driven dialogues. Ideal for scenarios demanding continuous AI interactions, this chatbot offers a context-aware and responsive communication experience, capable of handling diverse queries with human-like insights.
### Features

- **Asynchronous Design**: Built with Python's `asyncio`, ensuring a non-blocking, efficient chat experience.
- **Context-Aware Conversations**: Maintains session data to provide relevant and continuous dialogue, preserving context over the course of a conversation.
- **Flexible and Scalable**: Easy to adapt for various OpenAI GPT models. For a full list of available models, check [OpenAI's model documentation](https://platform.openai.com/docs/models).
- **Environment-Friendly Configuration**: Securely configure your OpenAI API key through environment variables.

### Getting Started

Dive into AI-powered conversations in just a few steps. Clone the repository, set your OpenAI API key, and experience one of the most advanced chatbots built with cutting-edge AI technology.

# Installation Guide for GPT Chatbot

This guide will walk you through the process of setting up and running the GPT Chatbot. If you want to run it in Docker, please follow the steps tagged with "Advanced".

## (Simple) Prerequisites 
Before starting, ensure you have the following installed:

- Python 3.8 or higher
- 
## (Advanced) Prerequisites 

Before you begin, make sure you have the following installed:

- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (https://docs.docker.com/compose/install/) (optional, for easier management)

## Step 1: Clone the Repository

Clone or download the repository to your local machine. Open your terminal and change to the directory where you've cloned the repository.

## Step 2: Set Up Environment Variables

Create and edit `.env` file in the root directory of the project to include your OpenAI API key:

    OPENAI_API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual OpenAI API key.

## (Simple) Step 3: Install Dependencies 
Install the required Python packages:

    pip install -r requirements.txt

This will install all necessary dependencies listed in `requirements.txt`.

## (Simple) Step 4: Run the Chatbot

Start the chatbot by running the main Python script:

    python main.py

## (Advanced) Step 3: Build the Docker Image

Build the Docker image using the following command:

    docker build -t console-gpt .

This command builds a Docker image named `console-gpt` based on the instructions in your Dockerfile.


## (Advanced) Step 4: Run the Container 

Run the Docker container with the following command:

    docker run -it --env-file .env -p 4000:80 console-gpt

This command runs the `console-gpt` image in interactive mode, loads environment variables from the `.env` file, and maps port 4000 on your host to port 80 in the container.

## Step 5: Interact with the Chatbot

Once the container is running, you should see a prompt:

    GPT Chatbot. Type 'quit' to exit.

You can now start interacting with the chatbot. Type your queries and press Enter to get a response.

## Stopping the Container or Exiting the Chatbot

To exit the chatbot, type `quit`. To stop the Docker container, press `Ctrl+C` in your terminal if you're running in interactive mode.

---

This guide assumes a basic understanding of terminal or command-line operations. Adjust the guide to fit the specifics of your setup or audience as necessary.


### Contribution

Contributions are welcome! If you'd like to improve the Console-GPT or add features, please feel free to fork the repository, make your changes, and submit a pull request.

### License

This project is open source and available under the MIT License.

### Note on OpenAI API Key Usage and Costs

Please be aware that the use of the OpenAI API key in this project may incur costs. OpenAI provides API access on a pay-per-use basis, and charges can vary based on the amount and type of usage. It is the responsibility of the user to understand and manage their usage and associated costs. For more information, please refer to OpenAI's pricing page and documentation.

### Disclaimer

This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held liable for any damages arising from the use of this software. Users should use this software in compliance with all applicable laws and regulations, including but not limited to OpenAI's use case policies and guidelines.

The use of the OpenAI API and any results generated from it are the responsibility of the user. The authors of this software do not claim any ownership over the content generated from the OpenAI API and are not responsible for any direct or indirect outcomes of using the generated content.

By using this software, you acknowledge that you have read and understand these terms, and agree to use the software in accordance with them.
