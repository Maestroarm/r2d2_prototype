#uvicorn main:app
#uvicorn main:app --reload

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

from functions.requests import generate_email_sequence

# Function imports
# ...

# App init
app = FastAPI()

# CORS origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    "https://r2-d2-prototype.vercel.app"
]

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# post bot email response
@app.get("/get-email/")
async def post_email(name: str, theme: str):
    # Generate personalized email text
    email_text = generate_email_sequence(name, theme)
    
    # Return the email text in the response
    return {"email_text": email_text}
