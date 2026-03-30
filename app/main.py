from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import resume

app = FastAPI()

# Configure CORS
# In production, replace "*" with your exact GitHub Pages URL for security.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)