from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from io import BytesIO
from file_generator import create_zip_with_files

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/generate-files")
async def generate_files():
    zip_buffer = create_zip_with_files()
    response = StreamingResponse(BytesIO(zip_buffer.getvalue()), media_type="application/x-zip-compressed")
    response.headers["Content-Disposition"] = "attachment; filename=files.zip"
    return response
