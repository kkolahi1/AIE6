from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# We define a wrapper class to make it easier to use the OpenAI API and handle environment variables
class ChatOpenAI:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if self.openai_api_key is None:
            raise ValueError("OPENAI_API_KEY is not set")
# We default to text only so we don't have to parse the JSON response (e.g. token usage, metadata, etc.)
    def run(self, messages, text_only: bool = True, **kwargs):
        if not isinstance(messages, list):
            raise ValueError("messages must be a list")

        client = OpenAI()
        response = client.chat.completions.create(
            model=self.model_name, messages=messages, **kwargs
        )

        if text_only:
            return response.choices[0].message.content

        return response
