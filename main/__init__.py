# PIL-supported file formats as found here:
# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
# Dict structure: {<mime-type>: <PIL-identifier>}
MIME_TYPE_TO_PIL_IDENTIFIER = {
    "image/png": "PNG",
    "image/jpeg": "JPEG",
    "application/pdf": "PDF",
    # "image/avif": "AVIF",
    # "image/bmp": "BMP",
    # "image/dcx": "DCX",
    # "image/eps": "EPS",
    # "image/gif": "GIF",
    # "image/pcd": "PCD",
    # "image/pcx": "PCX",
    # "image/x-ppm": "PPM",
    # "image/psd": "PSD",
    # "image/tiff": "TIFF",
    # "image/x-xbitmap": "XBM",
    # "image/x-xpm": "XPM",
    # "image/webp": "WEBP",
}

FILE_MIME_TYPES = [
    "image/png",
    "image/jpeg",
    "application/pdf",
]

CHUNK_SIZE = 1024 * 1024  # 1 mb
