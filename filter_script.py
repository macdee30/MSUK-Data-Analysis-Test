import pandas as pd
import os


INPUT_DATA = "./data/BasicCompanyData-2023-07-01-part7_7.csv"
OUTPUT_FOLDER = "./output"
OUTPUT_DATA = f"{OUTPUT_FOLDER}/filtered_data.csv"


if __name__ == "__main__":

    df = pd.read_csv(INPUT_DATA, low_memory=False)
    filtered_df = df[
        (df["CompanyStatus"] == "Active")
        & (df["CompanyCategory"] == "Private Limited Company")
        & (
            (df["Accounts.AccountCategory"] == "SMALL")
            | (df["Accounts.AccountCategory"] == "MEDIUM")
        )
    ]

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    filtered_df.to_csv(OUTPUT_DATA, index=None)
    print(f"> Generated filtered data in: {OUTPUT_DATA}")
