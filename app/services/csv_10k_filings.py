import csv
import os
from pprint import pprint
import requests

from app.models.quarter import Quarter
from app.services.get_filings import get_filings

INPUTS_CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "inputs.csv")

FORM_NAME = "10-K"

search_terms = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain", "is"]

if __name__ == "__main__":

    print("-----------------------")
    print(f"FORM NAME: '{FORM_NAME}'")

    print("-----------------------")
    print(f"INPUTS:")

    inputs = []

    with open(INPUTS_CSV_FILEPATH, "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            pprint(dict(row))
            inputs.append(dict(row))

    years = list(set([i["year"] for i in inputs]))

    quarters = []

    for year in years:
        quarters.append(Quarter(year, 1))
        quarters.append(Quarter(year, 2))
        quarters.append(Quarter(year, 3))
        quarters.append(Quarter(year, 4))

    #for q in quarters:
#
    #    print("-----------------------")
    #    print(f"{q.yr} Q{q.qtr} ({q.filings_url()}):")
#
    #    metadata, filings = get_filings(q)
    #    matching_filings = [f for f in filings if (COMPANY_ID == f.company_id and FORM_NAME == f.form_name)]
    #    print(f"FOUND {len(matching_filings)} OUT OF {len(filings)} FILINGS")
#
    #    for filing in matching_filings:
    #        print("...")
    #        print("COMPANY:", filing.company_name)
    #        print("FILED ON:", filing.date)
    #        print("DOCUMENT URL:", filing.document_url())
    #        response = requests.get(filing.document_url())
#
    #        # TODO: write response to file
#
    #        print("DOCUMENT SEARCH:")
    #        for search_term in search_terms:
#
    #            n = response.text.count(search_term)
#
    #            print(" + ", search_term, n)
