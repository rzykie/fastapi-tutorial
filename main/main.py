import io

from typing import Union
from PIL import Image

from fastapi import FastAPI, UploadFile, File

from main.validators import validate_image_format

from . import FILE_MIME_TYPES, CHUNK_SIZE


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    validate_image_format(file, 400, FILE_MIME_TYPES)
    try:
        with open(file.filename, "wb") as file_upload:
            # load the file into memory in chunks and process the data
            # one chunk at a time
            while contents := file.file.read(CHUNK_SIZE):
                file_upload.write(contents)

    except Exception as error:
        return {"message": f"Error uploading a file: {error}"}

    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
