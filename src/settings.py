from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
REPORTS_PATH = BASE_DIR.joinpath('logs')
DATA_PATH = BASE_DIR.joinpath('data')
JSON_FILE = DATA_PATH.joinpath('operations.json')
CSV_FILE = DATA_PATH.joinpath('transactions.csv')
XLSX_FILE = DATA_PATH.joinpath('transactions_excel.xlsx')
