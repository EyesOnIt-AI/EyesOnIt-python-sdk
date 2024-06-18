import base64
import io
from PIL import Image


def decode_image(base64_image):
    decoded_image = base64.b64decode(base64_image)
    image = Image.open(io.BytesIO(decoded_image))
    return image
