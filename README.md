# MSDUK Data Analyst Test


## DATA CLEANUP PLAN
The following steps can be taken in other to clean up our customer database:
- Data Analyis: A comprehensive analyisis with respect to the challenges (incomplete data, inconsistent data and inaccurate data) should be done on the customers data. This can be done using python/excel to identify affected records and give a clear overview of them in other to map out the next plan of action.

- Data Enrichment: This is one of the challenging aspect of the cleanup. Based on the identified records, we will need to enrich the affeted customer data from other source of data. The source of data will depend on the company policies but it can be done by connecting with other third party services like Google Places, YellowPages etc. through APIs if available or scraping the records.

- Data Processing: After we have gotten a secondary source of data for our affected records and they are validated, we can process them according to the challeges we are facing.
  - For incomplete data, they can be populated from the secondary soruce of data 
  - For inaccurate records, they can be fixed with the new source of data
  - And for inconsistent data, they can be normalized based on agreed upon standards.
  This can be done usinng python or excel.




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