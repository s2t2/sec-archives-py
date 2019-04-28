from app.get_filings import ARCHIVES_URL, parse_line

def test_archives_url():
    assert ARCHIVES_URL == "https://www.sec.gov/Archives"

def test_line_parser():
    line = "1018724|AMAZON COM INC|10-K|2013-01-30|edgar/data/1018724/0001193125-13-028520.txt"
    filing = {
        "company_id": "1018724",
        "company_name": "AMAZON COM INC",
        "form": "10-K",
        "date": "2013-01-30",
        "path": "edgar/data/1018724/0001193125-13-028520.txt",
        "url": "https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt"
    }
    assert parse_line(line) == filing
