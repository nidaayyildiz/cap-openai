# Openai
 
> A GPT vision & language **capsule built for [NovaVision](https://github.com/novavision-ai)**.
 
## Overview
 
**Openai** is a NovaVision capsule that brings OpenAI's GPT vision and language models into the NovaVision pipeline. It exposes a set of ready-to-use tasks — captioning, OCR, classification, detection, VQA, and free-form prompting — each backed by the same underlying client and configurable model, API backend, and generation parameters.
 
## Tasks
 
| Executor | Task |
|----------|------|
| `OpenaiCaption` | Short image caption. |
| `OpenaiDetailedCaption` | Detailed image description. |
| `OpenaiOcr` | Extract all text from an image. |
| `OpenaiClassification` | Single-label classification into a given class list (JSON). |
| `OpenaiMultiLabelClassification` | Multi-label classification with per-class confidence (JSON). |
| `OpenaiObjectDetection` | Bounding-box detection with normalized coordinates (JSON). |
| `OpenaiVqa` | Visual question answering — answer a prompt about an image. |
| `OpenaiStructuredAnswering` | Extract image info into a user-defined JSON structure. |
| `OpenaiUnconstrained` | Free-form prompt + image, unconstrained output. |
| `OpenaiPromptOnly` | Text-only prompt, no image. |
 
## API Backends
 
The capsule can route requests through three backends, selected via `ApiType`:
 
- **OpenAI** — the standard OpenAI API (`ApiKey`).
- **Azure OpenAI** — Azure-hosted deployments (`ApiKey`, `ApiVersion`, `AzureDeployment`, `AzureEndpoint`).
- **NovaVision** — NovaVision-hosted models via an OpenAI-compatible endpoint.
## Configuration
 
Common parameters across tasks:
 
| Config | Description |
|--------|-------------|
| `ModelVersion` | Target GPT model (e.g. `gpt-5.4`, `gpt-5-mini`, `gpt-4.1`). |
| `Temperature` | Sampling temperature. |
| `MaxTokens` | Max output tokens. |
| `ReasoningEffort` | Reasoning effort: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`. |
| `ApiType` | Backend selector: OpenAI / Azure / NovaVision. |
 
Task-specific configs include `ConfigClasses` (classification & detection), `ConfigPrompt` (VQA, unconstrained, prompt-only), and `ConfigOutputStructure` (structured answering). Tasks that request JSON automatically enable the model's `json_object` output mode.
 
## Structure
 
```
src/
├── executors/                 # One executor per task (caption, OCR, VQA, detection, ...)
├── models/PackageModel.py     # Pydantic schemas: inputs, outputs, model & backend configs
└── utils/
    ├── openai_client.py       # OpenAI / Azure / NovaVision client wrappers
    ├── prompt_builders.py     # Per-task instruction & input builders
    ├── image_utils.py         # Base64 image encoding
    └── response.py            # Response builder
```
 
## Install
 
```bash
pip install .
```
 
Requires **Python 3.6+**, the `openai` SDK, OpenCV (`opencv-python-headless`), and the NovaVision `sdk`. Designed to run inside the NovaVision runtime. Provide a valid API key (and Azure/NovaVision endpoint details when using those backends) via the task configuration.
 
## License
 
[MIT](LICENSE)
 
