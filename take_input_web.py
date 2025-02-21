from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import requests

print("Take Input from Web")
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Question Form</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
            }
            input[type="text"] {
                width: 100%;
                padding: 8px;
                margin-bottom: 20px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            .response {
                margin-top: 20px;
            }
            .response p {
                background-color: #e7f3fe;
                padding: 10px;
                border: 1px solid #b3d4fc;
                border-radius: 4px;
            }
            .back-link {
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #4CAF50;
            }
            .back-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Ask a Question</h1>
            <form action="/submit" method="post">
                <label for="question">Question:</label>
                <input type="text" id="question" name="question" required>
                <input type="submit" value="Submit">
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, question: str = Form(...)):
    url = "http://0.0.0.0:8000/ask"
    data = {"question": question}
    response = requests.post(url, json=data)
    response_data = response.json()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Response</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                margin-bottom: 20px;
            }}
            .response {{
                margin-top: 20px;
            }}
            .response p {{
                background-color: #e7f3fe;
                padding: 10px;
                border: 1px solid #b3d4fc;
                border-radius: 4px;
            }}
            .back-link {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #4CAF50;
            }}
            .back-link:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Response:</h1>
            <div class="response">
                <p>{response_data['answer']}</p>
            </div>
            <a href="/" class="back-link">Go back</a>
        </div>
    </body>
    </html>
    """