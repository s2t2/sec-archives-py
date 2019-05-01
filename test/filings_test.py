from app.get_filings import new_filing
from app.models.filing import ARCHIVES_URL, Filing

#filing_params = {
#    "company_id": "1018724",
#    "company_name": "AMAZON COM INC",
#    "form_name": "10-K",
#    "date": "2013-01-30",
#    "path": "edgar/data/1018724/0001193125-13-028520.txt",
#}

def test_archives_url():
    assert ARCHIVES_URL == "https://www.sec.gov/Archives"

def test_new_filing():
    filing_line = "1018724|AMAZON COM INC|10-K|2013-01-30|edgar/data/1018724/0001193125-13-028520.txt"

    filing = new_filing(filing_line)

    assert isinstance(filing, Filing)
    assert filing.company_id == "1018724"
    assert filing.company_name == "AMAZON COM INC"
    assert filing.form_name == "10-K"
    assert filing.date == "2013-01-30"
    assert filing.document_path == "edgar/data/1018724/0001193125-13-028520.txt"
    assert filing.document_url() == "https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt"
