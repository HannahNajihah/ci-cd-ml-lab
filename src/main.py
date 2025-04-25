import pandas as pd

def load_data():
    # Example DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = load_data()
    print(df)
