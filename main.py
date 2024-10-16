import uvicorn
import os

from fastapi import FastAPI

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
app = FastAPI()


@app.get("/")
async def hello():
    return {"success": True}


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
