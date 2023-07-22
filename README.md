# MSDUK Data Analyst Test


### TASk 1: SCRIPT TO FILTER DATA

- To run script first install the requirements with
```
pip3 install -r requirements.txt
```

- The script can then be run with 
```
python3 filter_script.py
```

- Input Data: `./data/BasicCompanyData-2023-07-01-part7_7.csv`
- Output Data: `./output/filtered_data.csv`


### TASk 2: CONSUME NAMSOR API

- To run script first install the requirements with
```
pip3 install -r requirements.txt
```

- Add your Namsor API Key in the .env file following the .env.example format. You can generate one using
```
cp .env.example .env
```

- Initate Namsor API consumption with:
```
python3 populate_ethnicity.py
```
- Input Data: `./data/Names_List.xlsx`
- Output Data: `./output/Names_List_Updated.xlsx`