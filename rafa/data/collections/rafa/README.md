# RaFa: An Open-Source Framework for Enterprise AI 🚀 

## Introduction

Welcome to RaFa, an open-source project that's all about making life easier for those who are looking for a private GPT for their enterprise knowledge base 🧠

## Table of Contents
- [RaFa: An Open-Source Framework for Enterprise AI 🚀](#rafa-an-open-source-framework-for-enterprise-ai-)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [How RaFa Works 🛠️](#how-rafa-works-️)
  - [RaFa Architecture](#rafa-architecture)
  - [Getting Started 🏁](#getting-started-)
    - [Running it locally 🏃‍♂️](#running-it-locally-️)
    - [Running it using Docker 🐳](#running-it-using-docker-)
    - [Changing the environment setup (optional) 🛠️](#changing-the-environment-setup-optional-️)
    - [Prompt templating (optional) 🛠](#prompt-templating-optional-)
    - [Tips and Tricks 🎩](#tips-and-tricks-)
  - [How to use RaFa 🚀](#how-to-use-rafa-)
    - [Ciao friday 👋](#ciao-friday-)
    - [Create a knowledge base 📂](#create-a-knowledge-base-)
    - [Ask questions 🤔](#ask-questions-)
    - [Build your AI 🤖](#build-your-ai-)
  - [Deploy to Cloud ☁️](#deploy-to-cloud-️)
  - [Work in Progress 🚧](#work-in-progress-)
  - [Contributing 🤝](#contributing-)
  - [License 📜](#license-)

## Features

- A private GPT for your *enterprise knowledge base* 
- A RAG framework that's built on top of *open-source LLM's and framework's*
- A private GPT that *runs securely* on your cloud or on-premise infrastructure
- *Continously growing RAG framework* along with the latest trends in AI
  
It's designed to be production-ready, so you can deploy RaFa-powered applications on your cloud or on-premise environments. No sweat! 💪

## How RaFa Works 🛠️

*For non-technical users*, simply deploy RaFa on your infrastructure and let the AI agents automatically select the optimal architecture for your needs.

*For tech-savvy users*, customize your experience by tweaking the config file to your needs. With RaFa, flexibility meets simplicity, empowering users to focus on their specific use-cases without unnecessary complexity.🇨🇭

## RaFa Architecture

RaFa's architecture is designed to be modular and flexible, allowing users to easily integrate new frameworks and layers as needed. The current architecture includes the following components:

<p align="center">
<img src="rafa_as_is.drawio.png">
</p>

## Getting Started 🏁

Ready to take Rafa for a spin? Check out the installation and usage instructions in the documentation. It's as easy as pie! 🥧

### Running it locally 🏃‍♂️
1. Pre-requisites:
   
   - RaFA is built using **Python 3.8** or higher and **Poetry** for dependence management. Make sure you have Python installed on your system. You can download it from the official Python website.
  
     - Python 3.6 or higher
     - Pip (Optional)
     - Poetry

2. Clone the repository:
   > **Note:** You can also download it directly from Github
   
   ```bash
   git clone https://github.com/rajnavakoti/rafa.git
    ```

3. Download and Install Ollama:
   - For MAC and Windows users, you can download the latest version of Ollama from the [official website](https://ollama.com/download).
   - For Linux users, you can Install with a single command:
  
     ```bash
     curl -fsSL https://ollama.com/install.sh | sh
     ```
4. Install your model:
   - You can install your choice of model using ollama commands. You can find the list of models available on the [Ollama website](https://ollama.com/library). RaFA by default setup for LLama3_8b:Instruct model
   
     ```bash
     ollama run <model>
     ```
5. Setup environment:
   - To run it locally the 'IS_DOCKER' environment variable should be commented in the .env in the root folder. By default it is commented. so double check before running it locally 👇
  
     ![alt text](image.png)

6. Run RaFA:
    - To run RaFA locally, you can use the following command from the root folder of the project:
  
  > **Note:** If you run in to permission issues while running the script, you can run **chmod +x run_rafa.sh** first to give the script execution permissions.
 
      ./run_rafa.sh

### Running it using Docker 🐳

1. Pre-requisites:
   
   - RaFA is built using **Python 3.8** or higher and **Poetry** for dependence management. Make sure you have Python installed on your system. You can download it from the official Python website.
  
     - Python 3.6 or higher
     - Pip (Optional)
     - Poetry
     - Docker

2. Clone the repository:
   > **Note:** You can also download it directly from Github
   
   ```bash
   git clone https://github.com/rajnavakoti/rafa.git
    ```

3. Setup environment:
   - To run it using docker the 'IS_DOCKER' environment variable should be **un-commented** in the .env in the root folder 👇

      ![alt text](image-1.png)

4. Run docker-compose:

   - To run RaFA using docker, you can use the following command from the root folder of the project:
  
     ```bash
     docker-compose up
     ```
5. Install your model:
   - You can install your choice of model using ollama commands inside the ollama docker container. You can find the list of models available on the [Ollama website](https://ollama.com/library). RaFA by default setup for LLama3_8b:Instruct model
   
     ```bash
     1. Get the ollama container id using the following command:
        docker ps
     2. Run the following command to get into the ollama container:
        docker exec -it <container_id> /bin/bash
      3. Run the following command to install the model:
         ollama run <model>
     ```
2. Use Streamlit to interact with RaFA:
   - Once the docker-compose is up and running, you can access the Streamlit app by navigating to the following URL in your browser:
  
     ```bash
     http://localhost:8501
     ```
   
   - You can now interact with RaFA using the Streamlit app. Have fun! 🎉

### Changing the environment setup (optional) 🛠️

You can change the default environment setup by changing the values in the .env file in the root folder. The following are the default values in the .env file:

- Default Environment Variables

| Variable                | Description                                      | Default                | Options                                                                 |
|-------------------------|--------------------------------------------------|------------------------|-------------------------------------------------------------------------|
| IS_DOCKER               | Choice to run it locally or using docker         | commented              | comment, uncomment                                                      |
| STORAGE_TYPE            | Type of storage you would like to store          | chromadb               | in-memory, chromadb (vector), Neo4j (graph)                              |
| CHUNK_SIZE              | ChunkSize controls the max size of the final documents (in terms of number of characters) | 256                    |                                                                         |
| CHUNK_OVERLAP           | ChunkOverlap specifies how much overlap there should be between chunks | 5                      |                                                                         |
| EMBED_MODEL             | Text embedding model                             | bge-small-en-v1.5      | Any model supported by llama-index                                       |
| LLM_MODEL               | Your LLM                                         | llama3:instruct_8b     | Any model supported by ollama                                            |
| CHAT_MEOMRY_TOKEN_LIMIT | How much chat history you want to include in your prompt | 3900 token         |                                                                         |
| OLLAMA_SERVER_TIMEOUT   | How long RaFA should wait for a response from the ollama server | 90sec           |                                                                         |
| CHAT_MODE               | llama-index options for your chat engine          | condense_plus_context  | best, condense_question, context, condense_plus_context, simple, react, openai |

You can change these values to suit your needs. Once you've made the changes, you can run RaFA using the instructions provided above. 🚀

> **Note:** You are also free to add or change any environment variables as needed. Just make sure to update the .env file accordingly. 🎈

### Prompt templating (optional) 🛠

If you  want to change the  defualt  prompt templates . you can make in the changes in  default_prompt_templates.py file in the rafa folder under prompts directory. Prompt templates depeneds on the model you are using.


### Tips and Tricks 🎩

**1. Use smaller models for testing:**

  When you're testing RaFA, it's a good idea to use smaller models to speed up the process. You can change the model in the .env file to a smaller one to get faster results.

  By default, RaFA uses the llama3:instruct_8b model, which is a large model. With a good local machine configuration, you can use this model without any issues. However, if you're running into performance issues, you can switch to a smaller model like llama3:instruct_1b or llama3:instruct_2b or Phi-3 Mini is a 3.8B model.

**2, Check your docker settings:**
  
  If you're running RaFA using Docker, make sure you have enough resources allocated to the Docker container. You can adjust the resources in the Docker settings to allocate more CPU and memory to the container.

  ![alt text](image-2.png)

**3. Docker cache issues:**
  
  If you're running into cache issues while building the Docker container, you can try running the following command to clear the cache:
  
    ```bash
    docker-compose build --no-cache
    ```
  This will rebuild the Docker container without using the cache, which can help resolve cache-related issues.

  Alternatively, you can all the containers and prune the system to remove all the unused containers and images. You can do this by running the following commands:
  
    ```bash
    docker compose down
    docker prune -a
    ```

**4. Use the Streamlit app for easy interaction:**

  The Streamlit app provides an easy-to-use interface for interacting with RaFA. You can use the app to input your prompts and get responses from RaFA in real-time. It's a great way to test RaFA and see how it performs with different prompts.

## How to use RaFa 🚀

Now everything is set up, you can start using RaFa and build your AI. Here is the way to go 🛴

### Ciao friday 👋

RaFa framework comes with a default AI app '**friday**'. It's a simple streamlit web app that helps you get started with RaFa.

You can access the Friday app by navigating to the following URL in your browser: http://localhost:8501

Once you're in the app, you can interact with RaFa by entering your prompts in the input box and clicking the 'Ask' button. RaFa will generate a response based on your prompt and display it in the app. You can continue to ask questions and get responses from RaFa in real-time. It's like having your own private GPT at your fingertips! 🎉

You can also upload your data (documents) using the '**create collection**' and '**add document**' buttons. This will allow RaFa to generate responses based on the created knowledge base.

![alt text](<screen-capture (4).gif>)

### Create a knowledge base 📂

Knowledge base is the heart of the RaFa framework. It's where you store all your documents and data that RaFa uses to generate responses to your queries.

The framework is by default using the *chromadb* for storing the documents. You can upload your documents using the '*create collection*' and '*add document*' options in the Friday app

> **Note:** Please see the [chromadb documentation](https://cookbook.chromadb.dev/) for better understanding of database, collection and document relationship.

![alt text](<screen-capture (6).gif>)

### Ask questions 🤔

Now you are ready to chat with friday. You have 2 toggle options you can choose from:

1. **Chat Mode:** You can choose the 'chat mode' toogle to switch between QA and chat:
   - **QA**: This mode is used for asking questions and getting answers, no chat history is included in the prompt.
   - **chat**: This mode is used for chat history, where the chat history is included in the prompt and friday will respond based on the chat history.

2. **Using knowledge base:** You can choose the 'Use knowledge base' toggle to switch between, whether friday has to use the your knowledge base to answer the questions or not.

### Build your AI 🤖

This is the fun part you are waiting for. sorry for the long wait, it's important to understand the basics before you start building your AI.

Building your own AI app is simple plug and play. The interaction of the framework techinically starts with http proxy serverit's is the entry point.

1. **Simple app integration**:

   ![alt text](build_your_app.drawio.png)

2. **Advanced app integration**:

If you are looking for customizations, you can check the websocker server code in the **rafa/websocket_server.py** file. You can customize the code to suit your needs and build your own AI app.

## Deploy to Cloud ☁️

RaFa is designed to be cloud-ready, so you can easily deploy it on your favorite cloud provider. You can use the same Docker setup to deploy RaFa on the cloud. Just follow the instructions provided above, and you'll be up and running in no time! 🚀

Sample deployment scripts for popular cloud providers like AWS, GCP, and Azure are coming soon. Stay tuned for more updates! 🎉

## Work in Progress 🚧

We are continuously working on improving RaFa and adding new features. Here are some of the features we are working on:

1. *Advanced RAG:* We are going to add more advanced RAG practices to the framework that can improve the document embedding, retrieval, AI reasoning, self-reflection, and more.
2. *Kick-ass UI:* friday deserves a better design and we are working on it!
3. *multi model framework*

## Contributing 🤝

RaFa is an open-source project, and we love getting help from our community. It's like a potluck dinner - the more, the merrier! Check out the [contribution guidelines](/CONTRIBUTING.md) for more information.

## License 📜

RaFa is licensed under MIT. For more details, please refer to the LICENSE file in the repository. It's like the rule book of our potluck dinner. 😉

So, what are you waiting for? Dive in and start exploring Rafa today! 🏊‍♀️🎈