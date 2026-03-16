import os
import sys
import traceback

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.media.image import Image

from components.Openai.src.models.PackageModel import PackageModel
from components.Openai.src.utils.response import build_detailed_caption_response
from components.Openai.src.utils.prompt_builders import prepare_detailed_caption_prompt
from components.Openai.src.utils.openai_client import call_openai

class OpenaiDetailedCaption(Component):
    """
    Provides a detailed image description using OpenAI Vision models.
    """
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        
        configs = self.request.model.configs.executor.value.configs
        
        self.input_image = self.request.get_param("inputImage")
        self.model_version = configs.modelVersion.value
        self.api_key = configs.apiKey.value
        self.temperature = configs.temperature.value
        self.max_tokens = configs.maxTokens.value
        
        self.output_text = ""

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        try:
            img = Image.get_frame(img=self.input_image, redis_db=self.redis_db)
            
            prompt_data = prepare_detailed_caption_prompt(img.value)
            
            self.output_text = call_openai(
                model=self.model_version,
                api_key=self.api_key,
                instructions=prompt_data["instructions"],
                input_data=prompt_data["input"],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
        except Exception as e:
            traceback.print_exc()
            self.output_text = f"Error: {str(e)}"
            
        return build_detailed_caption_response(context=self)

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
