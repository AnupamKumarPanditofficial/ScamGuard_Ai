from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn
from model import get_risk_score

app = FastAPI(title="ScamGuard API")

# Enable CORS for the Chrome Extension
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to chrome-extension://<EXT_ID>
    allow_origin_regex="chrome-extension://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeRequest(BaseModel):
    text: str
    links: List[str]
    domain: str

class AnalyzeResponse(BaseModel):
    risk_score: int
    reasons: List[str]

@app.get("/")
async def root():
    return {"message": "ScamGuard API is running"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    result = get_risk_score(request.text, request.links, request.domain)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
