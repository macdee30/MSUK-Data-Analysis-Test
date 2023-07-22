import os, shutil, json
import pandas as pd
import requests
from dotenv import dotenv_values

# pull environment variables (NAMSOR API KEY) from .env file
config = dotenv_values(".env")

INPUT_DATA = "./data/Names_List.xlsx"
OUTPUT_FOLDER = "./output"
OUTPUT_DATA = f"{OUTPUT_FOLDER}/Names_List_Updated.xlsx"

API_URL = "https://v2.namsor.com/NamSorAPIv2/api2/json/diasporaBatch"


def save_response(resp_json, first_name, last_name):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    filename = f"{first_name}_{last_name}.txt"
    full_path = f"{OUTPUT_FOLDER}/{filename}"

    with open(full_path, "w") as file:
        json.dump(resp_json, file, indent=4)


def get_response(firstname, lastname):
    payload = {
        "personalNames": [
            {
                "id": "e630dda5-13b3-42c5-8f1d-648aa8a21c42",
                "firstName": firstname,
                "lastName": lastname,
            }
        ]
    }
    headers = {
        "X-API-KEY": config.get("NAMSOR_API_KEY"),
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()


def parse_response(resp_json):
    """Returns Ethnicity and Alternate Ethnicity from response"""

    personal_records = resp_json.get("personalNames")
    unit_record = personal_records[0] if personal_records else {}
    ethnicity = unit_record.get("ethnicity")
    alt_ethnicity = unit_record.get("ethnicityAlt")

    return ethnicity, alt_ethnicity


def gen_ethnicity(firstname, lastname):
    """Extracts ethnicity and alternate of name"""
    print(f"> Updating Ethnicity for {firstname} {lastname}")
    resp = get_response(firstname, lastname)
    save_response(resp, firstname, lastname)
    return parse_response(resp)


if __name__ == "__main__":
    xls = pd.ExcelFile(INPUT_DATA)
    names_df = pd.read_excel(xls, "Sheet3")

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    names_df[["Ethnicity", "Alternate Ethnicity"]] = names_df.apply(
        lambda x: gen_ethnicity(x["First Name"], x["Last Name"]),
        axis="columns",
        result_type="expand",
    )

    shutil.copyfile(INPUT_DATA, OUTPUT_DATA)

    with pd.ExcelWriter(
        OUTPUT_DATA,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace",
    ) as output_writer:
        names_df.to_excel(output_writer, sheet_name="Sheet3", index=False)

    print(f"Updated Ethnicity for names in: {OUTPUT_FOLDER}")
