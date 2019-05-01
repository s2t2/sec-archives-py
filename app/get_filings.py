import os
import requests
from dotenv import load_dotenv

ARCHIVES_URL = "https://www.sec.gov/Archives"
FILING_TYPE = "10-K"

load_dotenv()

COMPANY_ID = os.environ.get("COMPANY_ID", "1018724") # defaults to Amazon
YR = os.environ.get("YR", "2013") # your digit year
QTR = os.environ.get("QTR", "1") # quarter 1, 2, 3 or 4

def document_url(filing):
    """
    compiles a url where the filing document can be found and parsed
    @param filing: a dict with keys "company_id", "company_name", "form", "date", and "path"
    """
    return os.path.join(ARCHIVES_URL, filing["path"])

def new_filing(line):
    """
    assumes each line has the same five pipe-separated values
    @param line: a string like '1018724|AMAZON COM INC|10-K|2013-01-30|edgar/data/1018724/0001193125-13-028520.txt'
    """
    values = line.split("|") #> ['1018724', 'AMAZON COM INC', '10-K', '2013-01-30', 'edgar/data/1018724/0001193125-13-028520.txt']
    filing = {
        "company_id": values[0],
        "company_name": values[1],
        "form": values[2],
        "date": values[3],
        "path": values[4]
    }
    return filing

if __name__ == "__main__":

    request_url = f"https://www.sec.gov/Archives/edgar/full-index/{YR}/QTR{QTR}/master.idx"

    print("--------")
    print("ARCHIVES URL:", request_url) #> https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx

    response = requests.get(request_url)

    print("RESPONSE:", response.status_code, type(response))

    lines = response.text.split("\n")

    print(f"FILINGS: {len(lines)}")

    filings = [new_filing(line) for line in lines if (COMPANY_ID in line and FILING_TYPE in line)]

    print("--------")
    print(f"COMPANY #{COMPANY_ID} '10-K' FORMS:")

    for filing in filings:
        print("...", filing["date"], document_url(filing))
