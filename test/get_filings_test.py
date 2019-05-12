import os
import pytest

from app.services.get_filings import get_filings, parse_header_lines, new_filing
from app.models.filing import Filing
from app.models.quarter import Quarter

@pytest.mark.skipif(os.environ.get("CI") == "true", reason="avoids HTTP requests")
def test_get_filings():
    idx = Quarter(2013, 1)

    metadata, filings = get_filings(idx)

    assert metadata == master_idx_metadata
    assert len(filings) == 303618
    assert filings[0].company_id == "1000032"
    assert filings[0].company_name == "BINCH JAMES G"
    assert filings[-1].company_id == "99947"
    assert filings[-1].company_name == "TRUBEE, COLLINS & CO., INC."

master_idx_metadata = {
    "desc": "Master Index of EDGAR Dissemination Feed",
    "date": "March 31, 2013",
    "email": "webmaster@sec.gov",
    "ftp_url": "ftp://ftp.sec.gov/edgar/",
    "url": "https://www.sec.gov/Archives/"
}

def test_metadata():
    header_lines = [
        'Description:           Master Index of EDGAR Dissemination Feed',
        'Last Data Received:    March 31, 2013',
        'Comments:              webmaster@sec.gov',
        'Anonymous FTP:         ftp://ftp.sec.gov/edgar/',
        'Cloud HTTP:            https://www.sec.gov/Archives/',
        '',
        ' ',
        ' ',
        ' ',
        '--------------------------------------------------------------------------------',
        ''
    ]
    metadata = parse_header_lines(header_lines)
    assert metadata == master_idx_metadata

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

#def test_index_parser():
#    idx_filepath = os.path.join(os.path.dirname(__file__), "test", "mock_data", "master.idx")
