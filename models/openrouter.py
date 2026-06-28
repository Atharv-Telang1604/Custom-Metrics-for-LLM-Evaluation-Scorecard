import requests
from config import api_key
def query_model(api_key,model_name,prompt):

    url = ("https://openrouter.ai/api/v1/"
    "chat/completions")

    headers = {
        "Authorization": f"Bearer{api_key}",
        "Content-Type":"application/json"
    }

    payload = {
        "model": model_name,

        "messages":[
            {
                "role":"user",
                "content":prompt
            }
        ]
    }

    response = requests.post(
        url,
        headers = headers,
        json = payload
    )

    result = response.json()

    return result[
        "choices"
    ][0][
        "message"
    ] ["content"]