import os
import requests

ARCHIVES_URL = "https://www.sec.gov/Archives"
COMPANY_ID = "1018724" # AMAZON
FILING_TYPE = "10-K"

def parse_line(line):
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
        "path": values[4],
        "url": os.path.join(ARCHIVES_URL, values[4])
    }
    return filing

if __name__ == "__main__":

    year = "2013"
    quarter = "1"
    request_url = f"https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{quarter}/master.idx"

    print("URL:", request_url) #> https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx

    response = requests.get(request_url)

    print("RESPONSE:", response.status_code, type(response))

    lines = response.text.split("\n")

    print(f"FILINGS: {len(lines)}")

    company_lines = [line for line in lines if (COMPANY_ID in line and FILING_TYPE in line)]

    print(f"10-K FILINGS FOR COMPANY #{company_id}: {len(company_lines)}")

    for line in company_lines:
        filing = parse_line(line)
        #print(f"  + '{filing['company_name']}' {filing['path']}")
        print(filing)
