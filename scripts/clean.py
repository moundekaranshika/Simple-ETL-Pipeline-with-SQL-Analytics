import pandas as pd

def clean_data():
    df = pd.read_csv("data/sales.csv")

    # Remove missing values
    df.dropna(inplace=True)

    # Create new column
    df["revenue"] = df["price"] * df["quantity"]

    # Save cleaned data
    df.to_csv("data/cleaned_sales.csv", index=False)

    print("Data cleaned successfully!")

if __name__ == "__main__":
    clean_data()
