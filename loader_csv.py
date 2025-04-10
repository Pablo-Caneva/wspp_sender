import pandas as pd

def load_csv(file_path):
    """Loads a CSV file and checks if it contains the required columns."""
    df = pd.read_csv(file_path, dtype=str)

    required_columns = {"numbers", "names"}
    if not required_columns.issubset(df.columns):
        raise ValueError("El CSV debe contener las columnas 'numbers' y 'names'.")

    return df