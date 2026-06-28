METRIC_NAME = "answer_relevance"

def evaluate(prompt,response):
    prompt_words = set(prompt.lower().split())
    response_words = set(response.lower().split())

    overlap = len(
        prompt_words &
        response_words
    )

    total = len(prompt_words)

    score = (overlap/total)*100

    return{
        "score": score,
        "explanation": f"{overlap} keywords matched"
    }