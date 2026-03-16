import cv2
import base64
import numpy as np
from typing import Union

def encode_image_to_base64(image: Union[np.ndarray, list, tuple]) -> str:
    """
    Converts a NumPy array image (e.g., from cv2 or NovaVision Image.value)
    into a base64 encoded JPEG string suitable for OpenAI Vision APIs.
    """
    if isinstance(image, (list, tuple)):
        image = np.array(image)

    # If the image has 4 channels (BGRA), convert it to 3 channels (BGR)
    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA@cvtColor2BGR)
        
    _, buffer = cv2.imencode('.jpg', image)
    base64_str = base64.b64encode(buffer).decode('utf-8')
    return base64_str
