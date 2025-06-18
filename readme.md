# Markdown to PDF API

A FastAPI service that converts Markdown text to PDF and uploads the resulting PDF to a remote server.

## Features

- Accepts Markdown text via a POST endpoint.
- Converts Markdown to HTML, then to PDF using WeasyPrint.
- Uploads the generated PDF to a remote endpoint with authentication.

## Requirements

- Python 3.7+
- [requirements.txt](requirements.txt) dependencies:
  - fastapi
  - uvicorn
  - markdown
  - requests
  - python-multipart
  - weasyprint

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Ensure WeasyPrint dependencies are installed:**
   - See [WeasyPrint installation docs](https://weasyprint.readthedocs.io/en/stable/install.html) for platform-specific requirements.

3. **Start the API server:**
   ```sh
   bash startup.sh
   ```
   The server will run on `http://0.0.0.0:8000`.

## Usage

### Endpoint

`POST /upload-pdf`

#### Form Data Parameters

- `md_text`: (string) The Markdown text to convert.
- `token`: (string) Bearer token for authentication with the remote server.
- `customer_id`: (string) Customer ID for the upload endpoint.

#### Example Request (using `curl`):

```sh
curl -X POST http://localhost:8000/upload-pdf \
  -F "md_text=# Hello World" \
  -F "token=Bearer <your_token>" \
  -F "customer_id=<customer_id>"
```

## File Structure

- [app/app.py](app/app.py): Main FastAPI application.
- [requirements.txt](requirements.txt): Python dependencies.
- [startup.sh](startup.sh): Script to start the server.
- [.github/workflows/master_ih-attachments.yml](.github/workflows/master_ih-attachments.yml): GitHub Actions workflow for Azure deployment.

## Notes

- Ensure WeasyPrint and its system dependencies are installed for PDF generation.
- The `/tmp` directory is used for temporary PDF storage.
- The remote upload endpoint and authentication are hardcoded for demonstration.

##