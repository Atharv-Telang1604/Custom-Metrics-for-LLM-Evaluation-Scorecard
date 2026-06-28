METRIC_NAME = "format_correctness"

def evaluate(prompt,response):

    score = 100
    explanation = "Format is correct."

    prompt_lower = prompt.lower()

    if "exactly in 2 lines" in prompt_lower:

        lines = response.strip().split("\n")

        if len(lines)!=2:

            score = 0

            explanation= (
                f"Expected exactly 2 lines but got {len(lines)}."

            )

            return{
                "score": score,
                "explanation": explanation
            }
    
