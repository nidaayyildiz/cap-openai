from typing import List, Dict, Any, Optional
from .image_utils import encode_image_to_base64


def format_open_vqa_input(base64_image: str) -> List[Dict[str, Any]]:
    return [
        {
            "type": "input_image",
            "image_url": f"data:image/jpeg;base64,{base64_image}"
        }
    ]


def prepare_unconstrained_prompt(prompt: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    return {
        "instructions": prompt,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_ocr_prompt(image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    return {
        "instructions": "You act as OCR model. Extract all text from the image and return only the text.",
        "input": format_open_vqa_input(base64_img)
    }


def prepare_vqa_prompt(prompt: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    return {
        "instructions": prompt,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_caption_prompt(image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    return {
        "instructions": "Describe the image briefly.",
        "input": format_open_vqa_input(base64_img)
    }


def prepare_detailed_caption_prompt(image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    return {
        "instructions": "Provide a detailed description of the image.",
        "input": format_open_vqa_input(base64_img)
    }


def prepare_classification_prompt(classes: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    instructions = (
        f"Classify the image into one of the following classes: {classes}. "
        "Return the response in the following JSON format strictly:\n"
        "{\n"
        "  \"class_name\": \"class\",\n"
        "  \"confidence\": 0.8\n"
        "}"
    )
    return {
        "instructions": instructions,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_multilabel_prompt(classes: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    instructions = (
        f"Identify all applicable classes from the following list in the image: {classes}. "
        "Return the response in the following JSON format strictly:\n"
        "{\n"
        "  \"predicted_classes\": [\n"
        "    {\"class\": \"cat\", \"confidence\": 0.9},\n"
        "    {\"class\": \"dog\", \"confidence\": 0.7}\n"
        "  ]\n"
        "}"
    )
    return {
        "instructions": instructions,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_object_detection_prompt(classes: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    instructions = (
        f"Detect objects in the image belonging to these classes: {classes}. "
        "Coordinates must be normalized between 0 and 1. "
        "Return the response in the following JSON format strictly:\n"
        "{\n"
        "  \"detections\": [\n"
        "    {\n"
        "      \"x_min\": 0.1,\n"
        "      \"y_min\": 0.2,\n"
        "      \"x_max\": 0.4,\n"
        "      \"y_max\": 0.5,\n"
        "      \"class_name\": \"object\",\n"
        "      \"confidence\": 0.9\n"
        "    }\n"
        "  ]\n"
        "}"
    )
    return {
        "instructions": instructions,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_structured_prompt(output_structure: str, image: Any) -> Dict[str, Any]:
    base64_img = encode_image_to_base64(image)
    instructions = (
        "Extract information from the image and format it according to the requested JSON structure strictly. "
        f"Output structure requested:\n{output_structure}"
    )
    return {
        "instructions": instructions,
        "input": format_open_vqa_input(base64_img)
    }


def prepare_prompt_only(prompt: str) -> Dict[str, Any]:
    return {
        "instructions": prompt,
        "input": []
    }
