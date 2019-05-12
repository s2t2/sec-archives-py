import os
import requests
from pprint import pprint

from app.models.filing import Filing
from app.models.quarter import Quarter

FORM_NAME = "10-K"
COMPANY_ID = os.environ.get("COMPANY", "1018724") # defaults to Amazon
YR = os.environ.get("YR", "2013") # your digit year
QTR = os.environ.get("QTR", "1") # quarter 1, 2, 3 or 4

search_terms = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain", "is"]

HEADER_LINE = "CIK|Company Name|Form Type|Date Filed|Filename"

def get_filings(idx):
    response = requests.get(idx.filings_url())
    #print("RESPONSE:", response.status_code, type(response))
    lines = response.text.split("\n") #> 303630 lines

    filing_lines = [l for l in lines if l.count("|") == 4] #> 303619 lines
    filing_lines = [l for l in filing_lines if l != HEADER_LINE]
    filings = [new_filing(l) for l in filing_lines]

    header_lines = [l for l in lines if l.count("|") != 4]
    metadata = parse_header_lines(header_lines)

    return metadata, filings

def parse_header_lines(lines):
    metadata = {
        "desc": "Master Index of EDGAR Dissemination Feed", # "Description:"
        "date": "March 31, 2013", # "Last Data Received"
        "email": "webmaster@sec.gov", # "Comments:"
        "ftp_url": "ftp://ftp.sec.gov/edgar/", # "Anonymous FTP:"
        "url": "https://www.sec.gov/Archives/" # "Cloud HTTP:"
    } # TODO: parse header lines for presence of keywords, then split on the keyword and use a cleaned version of the second split value
    return metadata


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

    print("----------------------------------------------")
    print(f"YEAR: '{YR}'")
    print(f"QUARTER: '{QTR}'")
    print(f"COMPANY: '{COMPANY_ID}'")
    print(f"FORM NAME: '{FORM_NAME}'")
    print("----------------------------------------------")

    idx = Quarter(YR, QTR)
    print("FILINGS INDEX:", idx.filings_url()) #> https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx

    metadata, filings = get_filings(idx)
    print(f"CONTAINS {len(filings)} FILINGS...")
    pprint(metadata)

    print("----------------------------------------------")
    filings = [f for f in filings if (COMPANY_ID == f.company_id and FORM_NAME == f.form_name)]
    print(f"FOUND {len(filings)} FILINGS...")

    for filing in filings:
        print("---------------")
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
