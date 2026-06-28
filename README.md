# Custom Metrics for LLM Evaluation Scorecard

A comprehensive Python framework for evaluating Large Language Models (LLMs) using custom metrics. This project provides a flexible and extensible system to assess model performance across multiple evaluation criteria and generate detailed scorecards.

## 📋 Overview

This project enables you to:
- **Evaluate multiple LLMs** against various custom metrics
- **Create extensible metrics** using simple Python modules
- **Generate scorecards** with aggregated scores across models and metrics
- **Track detailed explanations** for each evaluation result

## 🏗️ Project Structure

```
Custom-Metrics-for-LLM-Evaluation-Scorecard/
├── main.py                          # Entry point for the evaluation pipeline
├── config.py                        # Configuration and environment setup
├── metric_loader.py                 # Dynamic metric loader module
├── scorecard.py                     # Scorecard generation utility
├── requirements.txt                 # Project dependencies
├── custom_metrics/                  # Custom evaluation metrics
│   ├── answer_length_quality.py     # Evaluates response length quality
│   ├── answer_relevance.py          # Measures relevance of responses
│   └── format_correctness.py        # Validates response format
├── tests/                           # Test suite
│   └── test_scorecard.py            # Unit tests for metrics and scorecard
└── models/                          # (Placeholder) Model storage
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Atharv-Telang1604/Custom-Metrics-for-LLM-Evaluation-Scorecard.git
cd Custom-Metrics-for-LLM-Evaluation-Scorecard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Linux/macOS
export OPENROUTER_API_KEY="your_api_key_here"

# Windows PowerShell
$env:OPENROUTER_API_KEY = "your_api_key_here"
```

### Basic Usage

Run the evaluation pipeline:
```bash
python main.py
```

## 📊 Core Components

### 1. **main.py** - Evaluation Pipeline
The main entry point that orchestrates the evaluation process.

**Key Features:**
- Iterates through multiple LLM models
- Applies requested metrics to model responses
- Handles errors gracefully with try-catch blocks
- Aggregates results for scorecard generation

**Example:**
```python
models = ["meta-llama/llama-3-8b-instruct", "mistralai/mistral-7b-instruct"]
requested_metrics = ["answer_length_quality"]
prompt = "Explain recursion"
```

### 2. **metric_loader.py** - Dynamic Module Loader
Dynamically loads custom metric modules from the `custom_metrics/` directory.

**Features:**
- Validates metric existence
- Uses Python's `importlib` for dynamic loading
- Provides clear error messages for missing metrics

**Usage:**
```python
from metric_loader import load_metric
metric = load_metric("answer_length_quality")
result = metric.evaluate(prompt, response)
```

### 3. **scorecard.py** - Result Aggregation
Generates pivot tables and aggregated scorecards from evaluation results.

**Features:**
- Creates model × metric pivot tables
- Calculates overall scores per model
- Handles failed metrics gracefully
- Preserves order of models and metrics

**Output Structure:**
| Model | Metric 1 | Metric 2 | Overall Score |
|-------|----------|----------|---|
| Model A | 85 | 90 | 87.5 |
| Model B | 72 | 88 | 80 |

### 4. **config.py** - Configuration
Manages environment variables and API keys securely.

**Features:**
- Loads OpenRouter API key from environment
- Provides clear setup instructions
- Supports cross-platform environment variable setting

## 🧪 Custom Metrics

### Available Metrics

#### 1. **answer_length_quality.py**
Evaluates response quality based on word count.

**Scoring Logic:**
- **100 points**: 20-150 words (optimal range)
- **70 points**: 10-19 words (acceptable)
- **40 points**: < 10 words (too short)

**Output:**
```json
{
  "score": 100,
  "explanation": "Response contains 35 words"
}
```

#### 2. **answer_relevance.py**
Measures how relevant the response is to the prompt using keyword matching.

**Scoring Logic:**
- Calculates intersection of prompt and response keywords
- Score = (matched_keywords / total_prompt_keywords) × 100

**Output:**
```json
{
  "score": 75.5,
  "explanation": "3 keywords matched"
}
```

#### 3. **format_correctness.py**
Validates response format compliance.

**Scoring Logic:**
- Checks if prompt specifies format requirements (e.g., "exactly 2 lines")
- **100 points**: Format matches requirements
- **0 points**: Format doesn't match

**Output:**
```json
{
  "score": 100,
  "explanation": "Format is correct."
}
```

### Creating Custom Metrics

Create a new file in `custom_metrics/` with the following structure:

```python
METRIC_NAME = "your_metric_name"

def evaluate(prompt, response):
    """
    Evaluate a response against a prompt.
    
    Args:
        prompt (str): The input prompt
        response (str): The model's response
        
    Returns:
        dict: {"score": float, "explanation": str}
    """
    # Your evaluation logic here
    score = 85  # 0-100
    explanation = "Your evaluation explanation"
    
    return {
        "score": score,
        "explanation": explanation
    }
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

Or use unittest:
```bash
python -m unittest tests.test_scorecard -v
```

### Test Coverage

The `test_scorecard.py` includes tests for:
- ✅ Dynamic metric loading
- ✅ Metric evaluation functionality
- ✅ Scorecard pivot table generation
- ✅ Overall score calculations
- ✅ Handling of failed metrics

## 📈 Example Workflow

```python
from metric_loader import load_metric
from scorecard import generate_scorecard

# 1. Define models and metrics
models = ["model-a", "model-b"]
metrics = ["answer_length_quality", "answer_relevance"]

# 2. Get responses from models
responses = {
    "model-a": "Recursion is when a function calls itself.",
    "model-b": "Recursion: A technique where a function invokes itself with modified arguments."
}

# 3. Evaluate each response
results = []
for model in models:
    for metric_name in metrics:
        metric = load_metric(metric_name)
        score = metric.evaluate(prompt, responses[model])
        results.append({
            "Model": model,
            "Metric": metric_name,
            "Score": score["score"],
            "Explanation": score["explanation"]
        })

# 4. Generate scorecard
scorecard = generate_scorecard(results)
print(scorecard)
```

## 🔧 Dependencies

Key Python packages required:
- **pandas**: Data manipulation and pivot tables
- **importlib**: Dynamic module loading
- **pathlib**: Cross-platform file path handling

See `requirements.txt` for complete list.

## 📝 Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Your OpenRouter API key for LLM access

### Model Selection
Edit `main.py` to change evaluated models:
```python
models = [
    "meta-llama/llama-3-8b-instruct",
    "mistralai/mistral-7b-instruct"
    # Add more models here
]
```

### Metric Selection
Add or remove metrics from the `requested_metrics` list:
```python
requested_metrics = [
    "answer_length_quality",
    "answer_relevance",
    "format_correctness"
]
```

## 🎯 Use Cases

- 📊 **Model Benchmarking**: Compare multiple LLMs across custom metrics
- 🔍 **Quality Assurance**: Validate model output quality automatically
- ���� **Performance Tracking**: Monitor model improvements over time
- 🛠️ **Fine-tuning Evaluation**: Assess impact of fine-tuning on specific metrics

## 🚧 Known Limitations

- Format correctness metric currently only checks line count
- Answer relevance uses basic keyword matching
- Error handling reports failures but continues evaluation

## 🔮 Future Enhancements

- [ ] Add semantic similarity metrics using embeddings
- [ ] Implement GPT-based evaluation metrics
- [ ] Add support for batch processing
- [ ] Create web UI for visualization
- [ ] Add metric caching for performance
- [ ] Support for custom score aggregation strategies

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-metric`)
3. Commit your changes (`git commit -m 'Add new metric'`)
4. Push to the branch (`git push origin feature/new-metric`)
5. Open a Pull Request

## 📧 Contact & Support

For questions, issues, or suggestions, please open an issue on the GitHub repository.
