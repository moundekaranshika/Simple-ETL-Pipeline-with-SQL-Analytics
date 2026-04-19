import pandas as pd
from sqlalchemy import create_engine

def load_data():
    engine = create_engine("sqlite:///sales.db")

    df = pd.read_csv("data/cleaned_sales.csv")
    df.to_sql("sales", engine, if_exists="replace", index=False)

    print("Data loaded into database!")

if __name__ == "__main__":
    load_data()
