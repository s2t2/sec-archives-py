import csv
import os
from pprint import pprint
import requests

from app.models.quarter import Quarter
from app.services.get_filings import get_filings

INPUTS_CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "inputs.csv")
OUTPUTS_CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "outputs.csv")

FORM_NAME = "10-K"

search_terms = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain", "is"]

if __name__ == "__main__":

    print("-----------------------")
    print(f"FORM NAME: '{FORM_NAME}'")

    #
    # READ INPUTS FROM FILE
    #

    print("-----------------------")
    print(f"INPUTS:")

    inputs = []

    with open(INPUTS_CSV_FILEPATH, "r") as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)

        for row in reader:
            pprint(dict(row))
            inputs.append(dict(row))

    #
    # DETERMINE REQUESTED QUARTERS AND COMPANIES
    #

    company_ids = [i["company_id"] for i in inputs]
    company_ids = list(set(company_ids)) #> []

    quarters = []

    years = [i["year"] for i in inputs]
    years = list(set(years)) #>[2013, 2014, 2015]

    for year in years:
        quarters.append(Quarter(year, 1))
        quarters.append(Quarter(year, 2))
        quarters.append(Quarter(year, 3))
        quarters.append(Quarter(year, 4))

    #
    # GET FILINGS FOR REQUESTED QUARTERS
    #

    results = []

    for q in quarters:

        print("-----------------------")
        print(f"{q.yr} Q{q.qtr} ({q.filings_url()}):")

        metadata, filings = get_filings(q)
        matching_filings = [f for f in filings if (f.company_id in company_ids and f.form_name == FORM_NAME)]
        print(f"FOUND {len(matching_filings)} OUT OF {len(filings)} FILINGS")

        for filing in matching_filings:
            print("...")
            print("COMPANY:", filing.company_name)
            print("FILED ON:", filing.date)
            print("DOCUMENT URL:", filing.document_url())

            result = {
                "year": q.yr,
                "company_id": filing.company_id,
                "company_name": filing.company_name,
                "filed_on": filing.date,
                "url": filing.document_url()
            }

            response = requests.get(filing.document_url())

            # TODO: write response to file

            print("DOCUMENT SEARCH:")
            for search_term in search_terms:
                n = response.text.count(search_term)
                print(" + ", search_term, n)
                result[search_term] = n

            results.append(result)

    #
    # WRITE RESULTS TO FILE
    #

    headers = ["year", "company_id", "company_name", "filed_on", "url"]
    for search_term in search_terms:
        headers.append(search_term)

    with open(OUTPUTS_CSV_FILEPATH, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()

        for result in results:
            writer.writerow(result)
