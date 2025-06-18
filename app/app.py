
from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import markdown
import pdfkit
import uuid
import os
import requests

app = FastAPI()

@app.post("/upload-pdf")
def upload_pdf(md_text: str = Form(...), token: str = Form(...), customer_id: str = Form(...)):
    try:
        # Step 1: Convert Markdown to HTML
        html_text = markdown.markdown(md_text)

        # Step 2: Save HTML as PDF
        pdf_filename = f"{uuid.uuid4()}.pdf"
        pdf_path = f"/tmp/{pdf_filename}"
        pdfkit.from_string(html_text, pdf_path)

        # Step 3: Upload PDF using requests
        url = f"https://ih-demo-dev.symphonyai.dev/v1/subjects/{customer_id}/Attachments"
        headers = {
            "Authorization": token
        }
        payload = {
            "organisationUnit": "GRO",
            "fileName": pdf_filename
        }
        with open(pdf_path, "rb") as f:
            files = [
                ("file", (pdf_filename, f, "application/pdf"))
            ]
            response = requests.post(url, headers=headers, data=payload, files=files)

        return JSONResponse(status_code=response.status_code, content={"message": response.text})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
