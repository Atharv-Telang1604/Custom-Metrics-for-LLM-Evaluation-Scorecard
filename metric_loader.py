import importlib.util
from pathlib import Path


def load_metric(metric_name):
    file_path = Path(__file__).resolve().parent / "custom_metrics" / f"{metric_name}.py"

    if not file_path.exists():
        raise Exception(f'Metric "{metric_name}" not found')

    spec = importlib.util.spec_from_file_location(metric_name, file_path)

    if spec is None or spec.loader is None:
        raise Exception(f'Could not load metric "{metric_name}"')

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module