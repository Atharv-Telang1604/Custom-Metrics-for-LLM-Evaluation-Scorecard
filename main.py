from metric_loader import load_metric
from scorecard import generate_scorecard

models = [

    "meta-llama/llama-3-8b-instruct",

    "mistralai/mistral-7b-instruct"
]

requested_metrics = [

    "answer_length_quality"
]

prompt = (
    "Explain recursion"
)

results = []

for model in models:

    response = (
        "Recursion is when "
        "a function calls itself."
    )

    for metric_name in requested_metrics:

        try:

            metric = load_metric(
                metric_name
            )

            output = metric.evaluate(
                prompt,
                response
            )

            results.append({

                "Model": model,

                "Metric":
                metric_name,

                "Score":
                output["score"],

                "Explanation":
                output[
                    "explanation"
                ]
            })

        except Exception as e:

            results.append({

                "Model": model,

                "Metric":
                metric_name,

                "Score":
                "FAILED",

                "Explanation":
                str(e)
            })

scorecard = generate_scorecard(
    results
)

print(scorecard)