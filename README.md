# RAG_API Question Answering System using FastAPI

This is a FastAPI application that provides a question-answering system using a pre-trained model ([`distilbert-base-uncased-distilled-squad`](https://huggingface.co/distilbert/distilbert-base-uncased-distilled-squad)) and fuzzy matching for document retrieval. `distilbert-base-uncased-distilled-squad` is a pre-trained model from Hugging Face. It is a distilled version of BERT (Bidirectional Encoder Representations from Transformers) fine-tuned on the SQuAD (Stanford Question Answering Dataset) dataset. This model is designed for question-answering tasks.

 The application includes a web interface for inputting questions and receiving answers.


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


### Files Description
| File/Folder            | Description                              |
|------------------------|------------------------------------------|
| `Api.py`               | Main FastAPI application file            |
| `take_input_web.py`    | Web input form application file          |
| `requirements.txt`     | List of dependencies                     |
| `Dockerfile`           | Dockerfile to build the Docker image     |
| `docker-compose.yml`   | Docker Compose file for multiple services|
| `new_data.txt`         | Data file for document retrieval         |
| `README.md`            | Project documentation                   |
