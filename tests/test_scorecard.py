import unittest

from metric_loader import load_metric
from scorecard import generate_scorecard


class ScorecardTests(unittest.TestCase):
    def test_load_metric_returns_module_for_existing_metric(self):
        module = load_metric("answer_length_quality")
        self.assertTrue(hasattr(module, "evaluate"))
        self.assertEqual(module.METRIC_NAME, "answer_length")

    def test_answer_length_quality_metric_returns_explanation(self):
        module = load_metric("answer_length_quality")
        result = module.evaluate("Explain recursion clearly", "Recursion is when a function calls itself repeatedly")
        self.assertIn("score", result)
        self.assertIn("explanation", result)

    def test_generate_scorecard_pivots_results_by_model(self):
        result = [
            {"Model": "gpt-model-a", "Metric": "answer_length_quality", "Score": 85, "Explanation": "ok"},
            {"Model": "claude-model-b", "Metric": "answer_length_quality", "Score": 72, "Explanation": "ok"},
        ]

        scorecard = generate_scorecard(result)
        self.assertEqual(list(scorecard["Model"]), ["gpt-model-a", "claude-model-b"])
        self.assertEqual(scorecard.loc[0, "answer_length_quality"], 85)
        self.assertEqual(scorecard.loc[1, "answer_length_quality"], 72)
        self.assertEqual(scorecard.loc[0, "Overall Score"], 85)
        self.assertEqual(scorecard.loc[1, "Overall Score"], 72)

    def test_generate_scorecard_handles_failed_scores(self):
        result = [
            {"Model": "model-a", "Metric": "x", "Score": "FAILED", "Explanation": "error"},
            {"Model": "model-a", "Metric": "y", "Score": 90, "Explanation": "ok"},
            {"Model": "model-b", "Metric": "z", "Score": 80, "Explanation": "ok"},
        ]

        scorecard = generate_scorecard(result)
        self.assertEqual(scorecard.loc[scorecard["Model"] == "model-a", "Overall Score"].iloc[0], 90.0)
        self.assertEqual(scorecard.loc[scorecard["Model"] == "model-b", "Overall Score"].iloc[0], 80.0)


if __name__ == "__main__":
    unittest.main()
