from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from transformers import pipeline
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os

# Suppress TensorFlow informational logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define your Pydantic models
class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

# Initialize the question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Define a function to generate answers using the question-answering model
def generate_answer(question: str, context: str) -> str:
    return qa_pipeline(question=question, context=context)["answer"]

# Optimize the document retrieval function with fuzzy matching
def retrieve_documents(question: str) -> List[str]:
    documents = []
    try:
        with open("/Users/habibsifat/Desktop/FastApi/new_data.txt", "r") as file:
            lines = file.readlines()
            # Use fuzzy matching to find the best matching lines
            matches = process.extract(question, lines, scorer=fuzz.partial_ratio, limit=50)
            for match in matches:
                if match[1] > 50:  # Only include matches with a score above 50
                    documents.append(match[0].strip())
        print(f"Retrieved documents for question '{question}': {documents}")  # Debug print
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading documents: {str(e)}")
    return documents

@app.get("/")
async def root():
    return {"message": "Welcome to the Question Answering System!"}

@app.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    try:
        # Retrieve relevant documents
        documents = retrieve_documents(query.question)
        
        # Combine documents into a single context
        context = ' '.join(documents)
        
        # Check if context is empty
        if not context:
            return Answer(answer="\n\nNo relevant documents found.\n\nPlease try another question.")
        
        # Generate answer using the question-answering model
        answer = generate_answer(query.question, context)
        
        return Answer(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents", response_model=List[str])
async def get_documents():
    try:
        # Retrieve relevant documents
        documents = retrieve_documents("sample question")
        return documents
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)