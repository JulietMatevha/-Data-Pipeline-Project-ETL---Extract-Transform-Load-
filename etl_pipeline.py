import pandas as pd

def extract(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data extracted successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Failure to extract data: {e}")
        return None
