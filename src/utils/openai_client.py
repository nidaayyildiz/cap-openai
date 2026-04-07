from openai import OpenAI, AzureOpenAI
from typing import List, Dict, Any, Optional, Union


def _build_input(
    instructions: str,
    input_data: List[Dict[str, Any]],
    prompt_role: Optional[str] = None,
) -> Union[str, List[Dict[str, Any]]]:

    if prompt_role:
        role = "developer" if prompt_role == "system" else prompt_role
        messages = [{"role": role, "content": instructions}]
        if input_data:
            messages.append({"role": "user", "content": input_data})
        return messages
    else:
        if input_data:
            content = [{"type": "input_text", "text": instructions}]
            content.extend(input_data)
            return [{"role": "user", "content": content}]
        else:
            return instructions


def _build_kwargs(
    input_data: Union[str, List[Dict[str, Any]]],
    model: str,
    temperature: float,
    max_completion_tokens: int,
    reasoning_effort: Optional[str],
    instructions: str,
) -> Dict[str, Any]:

    kwargs: Dict[str, Any] = {
        "model": model,
        "input": input_data,
        "temperature": temperature,
        "max_output_tokens": max_completion_tokens,
    }

    # Prompt açıkça JSON istiyorsa json_object modunu etkinleştir
    if "JSON format strictly" in instructions:
        kwargs["text"] = {"format": {"type": "json_object"}}

    # reasoning_effort: 'none' veya boş ise gönderilmez
    if reasoning_effort and reasoning_effort.lower() not in ("none", ""):
        kwargs["reasoning"] = {"effort": reasoning_effort.lower()}

    return kwargs



def call_openai(
    model: str,
    api_key: str,
    instructions: str,
    input_data: List[Dict[str, Any]],
    temperature: float = 0.7,
    max_completion_tokens: int = 1024,
    reasoning_effort: Optional[str] = None,
) -> str:

    client = OpenAI(api_key=api_key)

    input_payload = _build_input(instructions, input_data)
    kwargs = _build_kwargs(input_payload, model, temperature, max_completion_tokens, reasoning_effort, instructions)

    response = client.responses.create(**kwargs)
    return response.output_text



def call_azure_openai(
    deployment: str,
    api_key: str,
    api_version: str,
    azure_endpoint: str,
    instructions: str,
    input_data: List[Dict[str, Any]],
    temperature: float = 0.7,
    max_completion_tokens: int = 1024,
    reasoning_effort: Optional[str] = None,
    prompt_role: Optional[str] = None,
) -> str:

    client = AzureOpenAI(
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
    )

    input_payload = _build_input(instructions, input_data, prompt_role=prompt_role)
    kwargs = _build_kwargs(input_payload, deployment, temperature, max_completion_tokens, reasoning_effort, instructions)

    response = client.responses.create(**kwargs)
    return response.output_text



def call_novavision_openai(
    model: str,
    api_key: str,
    instructions: str,
    input_data: List[Dict[str, Any]],
    temperature: float = 0.7,
    max_completion_tokens: int = 1024,
    reasoning_effort: Optional[str] = None,
) -> str:

    NOVAVISION_BASE_URL = "https://alfa.suite.novavision.ai/v1"

    client = OpenAI(
        api_key=api_key,
        base_url=NOVAVISION_BASE_URL,
    )

    input_payload = _build_input(instructions, input_data)
    kwargs = _build_kwargs(input_payload, model, temperature, max_completion_tokens, reasoning_effort, instructions)

    response = client.responses.create(**kwargs)
    return response.output_text
