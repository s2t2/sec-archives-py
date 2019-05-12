from app.models.filing import Filing

def test_filing():
    filing_params = {
        "company_id": "1018724",
        "company_name": "AMAZON COM INC",
        "form_name": "10-K",
        "date": "2013-01-30",
        "document_path": "edgar/data/1018724/0001193125-13-028520.txt",
    }

    filing = Filing(filing_params)

    assert isinstance(filing, Filing)
    assert filing.company_id == "1018724"
    assert filing.company_name == "AMAZON COM INC"
    assert filing.form_name == "10-K"
    assert filing.date == "2013-01-30"
    assert filing.document_path == "edgar/data/1018724/0001193125-13-028520.txt"
    assert filing.document_url() == "https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt"
