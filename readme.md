# Markdown to PDF API

A simple FastAPI service that converts Markdown text to PDF and uploads the resulting file to a remote server.

## Features

- Accepts Markdown text via a POST endpoint.
- Converts Markdown to HTML, then to PDF.
- Uploads the generated PDF to a specified remote endpoint with authentication.

## Requirements

- Python 3.7+
- [requirements.txt](requirements.txt) dependencies:
  - fastapi
  - uvicorn
  - markdown
  - pdfkit
  - requests

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Install wkhtmltopdf:**
   - `pdfkit` requires [wkhtmltopdf](https://wkhtmltopdf.org/) to be installed and available in your system's PATH.

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

## Notes

- Ensure `wkhtmltopdf` is installed for PDF generation.
- The `/tmp` directory is used for temporary PDF storage.
- The remote upload endpoint and authentication are hardcoded for demonstration.

## License

MIT License