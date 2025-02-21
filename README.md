# FastAPI Question Answering System

This is a FastAPI application that provides a question-answering system using a pre-trained model and fuzzy matching for document retrieval. The application includes a web interface for inputting questions and receiving answers.

## Project Structure



## Setup and Running the Application

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run the Application

1. **Clone the Repository**:
     git clone https://github.com/habibsifat/RAG_API.git<br>
     cd RAG_API
2. **Build and Run the Docker Containers**:
     docker compose build
     docker compose up
3. **Access the Application**:
    API service: http://127.0.0.1:8000
    Web input form: http://127.0.0.1:8001


**Files Description**

     Api.py : Main FastAPI application file.<br>
     take_input_web.py : Web input form application file.<br>
     requirements.txt : List of dependencies.<br>
     Dockerfile : Dockerfile to build the Docker image.<br>
     docker-compose.yml : Docker Compose file to manage multiple services.<br>
     new_data.txt : Data file for document retrieval.<br>
