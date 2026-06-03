from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from classifier import EmailClassifier
from extractor import FieldExtractor
from models import ExtractionResult

app = FastAPI(title="Email Segregation API")
app.mount("/static", StaticFiles(directory="static"), name="static")

classifier = EmailClassifier()
extractor = FieldExtractor()

class EmailRequest(BaseModel):
    """Request body for email extraction."""
    email_text: str

class EmailResponse(BaseModel):
    """Response format for extraction result."""
    category: str
    confidence: float
    data: dict

@app.get("/")
def serve_frontend():
    """Serve the main HTML page."""
    return FileResponse("static/index.html")

@app.post("/extract", response_model=EmailResponse)
def extract_email(request: EmailRequest) -> EmailResponse:
    """
    Classify email and extract fields.
    
    Args:
        request: EmailRequest with raw email_text
        
    Returns:
        EmailResponse with category, confidence, and extracted data
    """
    email_text = request.email_text.strip()
    
    if not email_text:
        return EmailResponse(
            category="unknown",
            confidence=0.0,
            data={}
        )
    
    category, confidence = classifier.classify(email_text)
    
    if category != 'unknown':
        data = extractor.extract(email_text, category)
    else:
        data = {}
    
    return EmailResponse(
        category=category,
        confidence=confidence,
        data=data
    )

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)