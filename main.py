from fastapi import FastAPI, UploadFile, Form
from risk_engine import calculate_risk, overall_score
from metadata import extract_metadata
from pdf_report import generate_pdf
from emailer import send_report

app = FastAPI()

@app.post("/analyze")
async def analyze(
    file: UploadFile,
    client_name: str = Form(...),
    transaction_ref: str = Form(...),
    email: str = Form(...)
):
    scores = calculate_risk()
    overall = overall_score(scores)
    meta = extract_metadata(file)

    pdf_path = "report.pdf"
    generate_pdf(pdf_path, client_name, transaction_ref, scores, overall, meta)
    send_report(email, pdf_path)

    return {"status": "Report generated and emailed"}