import getpass
import os
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("HUGGING_FACE_API_TOKEN"):
    os.environ["HUGGING_FACE_API_TOKEN"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_community.llms import HuggingFaceHub

llm = HuggingFaceHub(
    repo_id="fal-ai",
    model_kwargs={"temperature": 0.7, "max_length": 512}
)

result = llm.invoke("Explain quantum computing in simple terms.")


print(result)
