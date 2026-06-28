METRIC_NAME = "answer_length"

def evaluate(prompt,response):

    length = len(response.split())

    if length>=20 or length<=150:
        score = 100

    elif length<20 or length>=10:
        score = 70

    else:
        score = 40

    return{
        "score": score,
        "explanation": f"Response contains {length} words"
    }