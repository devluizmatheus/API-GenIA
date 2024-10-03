import google.generativeai as genai
from google.generativeai.types import HarmCategory
from google.generativeai.types import HarmBlockThreshold


MODEL_NAME = "gemini-1.5-flash"

genai.configure(api_key='AIzaSyAagaJHflo26iAiGIggajVQx2IyU5Nc7Rg')

generation_config = {
    "temperature": 0.5,
    "top_k": 0,
    "top_p": 0.95,
    "max_output_tokens": 1000
}

safety_settings={
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}


model = genai.GenerativeModel(
    model_name = MODEL_NAME,
    generation_config = generation_config,
    safety_settings = safety_settings
)
