
from app.models.quarter import Quarter

def test_quarter():
    idx = Quarter(2013, 1)
    assert idx.yr == 2013
    assert idx.qtr == 1
    assert idx.url() == "https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx"
