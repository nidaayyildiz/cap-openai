from openai import OpenAI
from typing import List, Dict, Any, Optional

def call_openai(
    model: str,
    api_key: str,
    instructions: str,
    input_data: List[Dict[str, Any]],
    temperature: float,
    max_tokens: int,
    reasoning_effort: Optional[str] = None
) -> str:
    """
    Calls the OpenAI API with the given parameters and instructions.
    Returns the mapped output text from the response.
    """
    client = OpenAI(api_key=api_key)
    
    # Map input data properly if image input is not provided
    messages = []
    
    if instructions:
        if input_data:
            # Multi-modal payload
            content = [{"type": "text", "text": instructions}]
            content.extend(input_data)
            messages.append({"role": "user", "content": content})
        else:
            # Text-only payload
            messages.append({"role": "user", "content": instructions})
            
    # Depending on model versions, developer/system roles may be structured differently.
    # We will use "user" for all to be universally compatible.
    
    # We may need to pass reasoning_effort if it's set and not none/auto
    kwargs = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_completion_tokens": max_tokens if hasattr(client.chat.completions, "create") else max_tokens, # handle differing SDK versions appropriately
    }
    
    # Compatibility with 'max_tokens' vs 'max_completion_tokens' for older/newer openai versions
    import openai
    if int(openai.__version__.split('.')[0]) < 1:
        # Fallback for very old openai versions (though we expect 1.x.x)
        kwargs.pop("max_completion_tokens", None)
        kwargs["max_tokens"] = max_tokens
    else:
        # modern openai defaults to top-level max_tokens
        kwargs.pop("max_completion_tokens", None)
        kwargs["max_tokens"] = max_tokens

    if reasoning_effort and reasoning_effort.lower() not in ("none", "", "auto"):
        # For latest reasoning-effort capable models (o1/o3)
        kwargs["reasoning_effort"] = reasoning_effort.lower()

    # Determine if we should force JSON response based on the prompt signature requesting JSON
    if "JSON format strictly" in instructions:
        kwargs["response_format"] = {"type": "json_object"}

    response = client.chat.completions.create(**kwargs)
    
    return response.choices[0].message.content
