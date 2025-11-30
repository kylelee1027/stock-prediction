from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]  # quant-ml-beginner/
DATA_DIR = PROJECT_ROOT / "data"
SPY_DIR = DATA_DIR / "spy"

SPY_2024_PRESENT = SPY_DIR / "spy_2024_present.csv"
SPY_FEATURES = SPY_DIR / "spy_features.csv"  # or wherever you save