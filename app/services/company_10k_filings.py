
import os
from pprint import pprint
import requests

from app.models.quarter import Quarter
from app.services.get_filings import get_filings

FORM_NAME = "10-K"
COMPANY_ID = os.environ.get("COMPANY", "1018724")

search_terms = ["anticipate", "believe", "depend", "fluctuate", "indefinite", "likelihood", "possible", "predict", "risk", "uncertain", "is"]

if __name__ == "__main__":

    print("-----------------------")
    print(f"FORM NAME: '{FORM_NAME}'")
    print(f"COMPANY: '{COMPANY_ID}'")

    quarters = [
        Quarter(2013,1),
        Quarter(2013,2),
        Quarter(2013,3),
        Quarter(2013,4),
        #Quarter(2014,1),
        #Quarter(2014,2),
        #Quarter(2014,3),
        #Quarter(2014,4),
        #Quarter(2015,1),
        #Quarter(2015,2),
        #Quarter(2015,3),
        #Quarter(2015,4),
        #Quarter(2016,1),
        #Quarter(2016,2),
        #Quarter(2016,3),
        #Quarter(2016,4),
        #Quarter(2017,1),
        #Quarter(2017,2),
        #Quarter(2017,3),
        #Quarter(2017,4),
        #Quarter(2018,1),
        #Quarter(2018,2),
        #Quarter(2018,3),
        #Quarter(2018,4),
    ]

    for q in quarters:

        print("-----------------------")
        print("YEAR:", q.yr)
        print("QTR:", q.qtr)
        print("FILINGS INDEX:", q.filings_url())

        metadata, filings = get_filings(q)
        matching_filings = [f for f in filings if (COMPANY_ID == f.company_id and FORM_NAME == f.form_name)]
        print(f"FOUND {len(matching_filings)} OUT OF {len(filings)} FILINGS")

        for filing in matching_filings:

            print("  -----------------")
            print("  COMPANY:", filing.company_name)
            print("  FILED ON:", filing.date)
            print("  DOCUMENT URL:", filing.document_url())
            response = requests.get(filing.document_url())

            # TODO: write response to file

            print("  DOCUMENT SEARCH:")
            for search_term in search_terms:

                n = response.text.count(search_term)

                print("   + ", search_term, n)
