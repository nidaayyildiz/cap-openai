from sdks.novavision.src.helper.package import PackageHelper
from components.Openai.src.models.PackageModel import (
    PackageModel, PackageConfigs, ConfigExecutor, DefaultOutputs, OutputsWithClasses,
    OutputText, OutputClasses, 
    UnconstrainedResponse, OpenaiUnconstrained,
    OcrResponse, OpenaiOcr,
    VqaResponse, OpenaiVqa,
    CaptionResponse, OpenaiCaption,
    DetailedCaptionResponse, OpenaiDetailedCaption,
    ClassificationResponse, OpenaiClassification,
    MultiLabelClassificationResponse, OpenaiMultiLabelClassification,
    ObjectDetectionResponse, OpenaiObjectDetection,
    StructuredAnsweringResponse, OpenaiStructuredAnswering,
    PromptOnlyResponse, OpenaiPromptOnly
)

def build_unconstrained_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = UnconstrainedResponse(outputs=outputs)
    executor = OpenaiUnconstrained(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_ocr_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = OcrResponse(outputs=outputs)
    executor = OpenaiOcr(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_vqa_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = VqaResponse(outputs=outputs)
    executor = OpenaiVqa(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_caption_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = CaptionResponse(outputs=outputs)
    executor = OpenaiCaption(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_detailed_caption_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = DetailedCaptionResponse(outputs=outputs)
    executor = OpenaiDetailedCaption(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_classification_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)
    outputs = OutputsWithClasses(output=output_text, classes=classes)
    response = ClassificationResponse(outputs=outputs)
    executor = OpenaiClassification(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_multi_label_classification_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)
    outputs = OutputsWithClasses(output=output_text, classes=classes)
    response = MultiLabelClassificationResponse(outputs=outputs)
    executor = OpenaiMultiLabelClassification(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_object_detection_response(context):
    output_text = OutputText(value=context.output_text)
    classes = OutputClasses(value=context.parsed_classes)  # Using parsed structures
    outputs = OutputsWithClasses(output=output_text, classes=classes)
    response = ObjectDetectionResponse(outputs=outputs)
    executor = OpenaiObjectDetection(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_structured_answering_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = StructuredAnsweringResponse(outputs=outputs)
    executor = OpenaiStructuredAnswering(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)

def build_prompt_only_response(context):
    output_text = OutputText(value=context.output_text)
    outputs = DefaultOutputs(output=output_text)
    response = PromptOnlyResponse(outputs=outputs)
    executor = OpenaiPromptOnly(value=response)
    config_executor = ConfigExecutor(value=executor)
    package_configs = PackageConfigs(executor=config_executor)
    
    package = PackageHelper(packageModel=PackageModel, packageConfigs=package_configs)
    return package.build_model(context)