import uvicorn
import os

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
app = FastAPI()
templates = Jinja2Templates(directory=f"{ROOT_PATH}/static/templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/health-check")
async def health_check():
    return {"status": "ok"}


if __name__ == '__main__':

    cert_file = f'{ROOT_PATH}/cert.pem'
    key_file = f'{ROOT_PATH}/key.pem'

    for file in [cert_file, key_file]:
        if not os.path.exists(file):
            raise FileNotFoundError(f'Could not find file: {file}')

    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        ssl_certfile=cert_file,
        ssl_keyfile=key_file,
    )
