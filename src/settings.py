from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
REPORTS_PATH = BASE_DIR.joinpath('logs')
DATA_PATH = BASE_DIR.joinpath('data')
