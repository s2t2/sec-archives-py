
from app.models.quarter import Quarter

def test_quarter():
    idx = Quarter(2013, 1)
    assert idx.yr == 2013
    assert idx.qtr == 1
    assert idx.url() == "https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx"

#def test_index_parser():
#    idx_filepath = os.path.join(os.path.dirname(__file__), "test", "mock_data", "master.idx")
#
#    idx, filings = parse_idx(idx_filepath)
#
#    assert idx == {
#        "desc": "Master Index of EDGAR Dissemination Feed",
#        "date": "March 31, 2013",
#        "email": "webmaster@sec.gov",
#        "ftp_url": "ftp://ftp.sec.gov/edgar/",
#        "url": "https://www.sec.gov/Archives/"
#    }
#
#    assert filings = []
#
