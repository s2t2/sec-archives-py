


from app.archives import ARCHIVES_URL

class Quarter():
    """
    idx = Quarter(2013, 1)
    """

    def __init__(self, yr, qtr):
        self.yr = yr
        self.qtr = qtr

    def filings_url(self):
        return f"{ARCHIVES_URL}/edgar/full-index/{self.yr}/QTR{self.qtr}/master.idx"
