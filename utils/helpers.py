import base64
from fastapi import HTTPException


def decode_photo(path, encode_string):
    """Decode file base64 encoded

    This function decode base64 encode image and put this image in temp_files directory. Then, this image will upload to s3

    Args:
        path (str): Directory where file is storage, its in temp_files directory
        encode_string (str): base64 string of a image

    Raises:
        HTTPException: Exception raise when base64 encoded is invalid.
    """
    with open(path, "wb") as f:
        try:
            f.write(base64.b64decode(encode_string.encode("utf-8")))
        except Exception as ex:
            raise HTTPException(400, "Invalid photo encoding")
