import config
from langchain.chat_models import init_chat_model
import os
import dotenv


def get_chat_model(model_spec: str) -> init_chat_model:
    return init_chat_model(model_spec, api_key=config.API_KEY)


if __name__ == "__main__":
    model = get_chat_model(config.CHAT_MODEL)
    response = model.invoke("What is the airspeed of a laden swallow?")
    print(response.content)