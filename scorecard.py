import pandas as pd


def generate_scorecard(result):
    df = pd.DataFrame(result)

    df["Score"] = pd.to_numeric(df["Score"], errors="coerce")
    df["Overall Score"] = df.groupby("Model")["Score"].transform("mean")

    model_order = list(dict.fromkeys(df["Model"]))
    metric_order = list(dict.fromkeys(df["Metric"]))

    scorecard = (
        df.pivot_table(
            index="Model",
            columns="Metric",
            values="Score",
            aggfunc="first"
        )
        .reindex(index=model_order)
        .reindex(columns=metric_order)
        .reset_index()
    )
    scorecard["Overall Score"] = df.groupby("Model")["Score"].mean().reindex(scorecard["Model"]).to_numpy()

    return scorecard