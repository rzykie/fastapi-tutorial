from typing import Collection
from PIL import Image

from fastapi import HTTPException, UploadFile

from . import MIME_TYPE_TO_PIL_IDENTIFIER


def validate_image_format(
    file: UploadFile,
    error_code: str,
    allowed_mimetypes: Collection[str] = MIME_TYPE_TO_PIL_IDENTIFIER.values(),
):
    image_mimetype = file.content_type

    if not image_mimetype or image_mimetype not in allowed_mimetypes:
        msg = f"Invalid file format. Only: {', '.join(allowed_mimetypes)} are supported"
        raise HTTPException(status_code=error_code, detail=msg)
