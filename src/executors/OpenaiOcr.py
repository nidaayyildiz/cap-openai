import os
import sys
import traceback

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.capsule import Capsule
from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.media.image import Image

from capsules.Openai.src.models.PackageModel import PackageModel
from capsules.Openai.src.utils.response import build_ocr_response
from capsules.Openai.src.utils.prompt_builders import prepare_ocr_prompt
from capsules.Openai.src.utils.openai_client import call_openai, call_azure_openai, call_novavision_openai


class OpenaiOcr(Capsule):
    """
    Optical Character Recognition using OpenAI Vision models.
    """
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))

        self.input_image   = self.request.get_param("inputImage")
        self.model_version = self.request.get_param("ModelVersion")
        self.temperature   = self.request.get_param("Temperature")
        self.max_tokens    = self.request.get_param("MaxTokens")

        self.api_type         = self.request.get_param("ApiType")
        self.api_key          = self.request.get_param("ApiKey")
        self.api_version      = self.request.get_param("ApiVersion")
        self.azure_deployment = self.request.get_param("AzureDeployment")
        self.azure_endpoint   = self.request.get_param("AzureEndpoint")

        _re1 = self.request.get_param("ReasoningEffort")
        _re2 = self.request.get_param("ReasoningEffort2")
        _re3 = self.request.get_param("ReasoningEffort3")
        _re4 = self.request.get_param("ReasoningEffort4")
        if _re1 is not None:
            self.reasoning_effort = _re1
        elif _re2 is not None:
            self.reasoning_effort = _re2
        elif _re3 is not None:
            self.reasoning_effort = _re3
        elif _re4 is not None:
            self.reasoning_effort = _re4
        else:
            self.reasoning_effort = None

        self.output_text = ""

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        try:
            img = Image.get_frame(img=self.input_image, redis_db=self.redis_db)
            prompt_data = prepare_ocr_prompt(img.value)

            if self.api_type == "AzureApi":
                self.output_text = call_azure_openai(
                    deployment=self.azure_deployment,
                    api_key=self.api_key,
                    api_version=self.api_version,
                    azure_endpoint=self.azure_endpoint,
                    instructions=prompt_data["instructions"],
                    input_data=prompt_data["input"],
                    temperature=self.temperature,
                    max_completion_tokens=self.max_tokens,
                    reasoning_effort=self.reasoning_effort,
                )
            elif self.api_type == "NovavisionApi":
                self.output_text = call_novavision_openai(
                    model=self.model_version,
                    api_key=self.api_key,
                    instructions=prompt_data["instructions"],
                    input_data=prompt_data["input"],
                    temperature=self.temperature,
                    max_completion_tokens=self.max_tokens,
                    reasoning_effort=self.reasoning_effort,
                )
            else:  # OpenAiApi
                self.output_text = call_openai(
                    model=self.model_version,
                    api_key=self.api_key,
                    instructions=prompt_data["instructions"],
                    input_data=prompt_data["input"],
                    temperature=self.temperature,
                    max_completion_tokens=self.max_tokens,
                    reasoning_effort=self.reasoning_effort,
                )

        except Exception as e:
            traceback.print_exc()
            self.output_text = f"Error: {str(e)}"

        return build_ocr_response(context=self)


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
