import pandas as pd


def analyze_csv(file_path):

    try:
        df = pd.read_csv(file_path)

        result = {
            "Head": df.head().to_dict(orient="records"),
            "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict()
        }

        return result

    except FileNotFoundError:
        return "CSV file not found."

    except Exception as e:
        return f"Error analyzing CSV: {e}"