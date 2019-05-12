import os
import requests

from app.models.filing import Filing
from app.models.quarter import Quarter

FORM_NAME = "10-K"
COMPANY_ID = os.environ.get("COMPANY", "1018724") # defaults to Amazon
YR = os.environ.get("YR", "2013") # your digit year
QTR = os.environ.get("QTR", "1") # quarter 1, 2, 3 or 4

search_terms = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain", "is"]

def new_filing(line):
    """
    assumes each line has the same five pipe-separated values
    @param line: a string like '1018724|AMAZON COM INC|10-K|2013-01-30|edgar/data/1018724/0001193125-13-028520.txt'
    """
    values = line.split("|") #> ['1018724', 'AMAZON COM INC', '10-K', '2013-01-30', 'edgar/data/1018724/0001193125-13-028520.txt']
    filing_params = {
        "company_id": values[0],
        "company_name": values[1],
        "form_name": values[2],
        "date": values[3],
        "document_path": values[4]
    }
    return Filing(filing_params)

if __name__ == "__main__":

    print("--------")
    print(f"YEAR: '{YR}'")
    print(f"QUARTER: '{QTR}'")
    idx = Quarter(YR, QTR)
    request_url = idx.url()
    print("FILINGS INDEX:", request_url) #> https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx

    response = requests.get(request_url)
    #print("RESPONSE:", response.status_code, type(response))
    lines = response.text.split("\n")
    print(f"FOUND {len(lines)} FILINGS")
    print(f"COMPANY: '{COMPANY_ID}'")
    print(f"FORM NAME: '{FORM_NAME}'")
    filings = [new_filing(line) for line in lines if (COMPANY_ID in line and FORM_NAME in line)]
    print(f"FOUND {len(filings)} MATCHING FILINGS:")

    for filing in filings:
        print("--------")
        print("COMPANY:", filing.company_name)
        print("FILED ON:", filing.date)
        print("DOCUMENT URL:", filing.document_url())
        response = requests.get(filing.document_url())
        #print("RESPONSE:", response.status_code, type(response))

        # TODO: write response to file

        print("DOCUMENT SEARCH:")
        for search_term in search_terms:

            n = response.text.count(search_term)

            print(" + ", search_term, n)
