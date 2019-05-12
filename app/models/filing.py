import os

ARCHIVES_URL = "https://www.sec.gov/Archives"

class Filing():

    def __init__(self, params):
        """
        params: a dict with keys "company_id", "company_name", "form_name", "date", and "document_path"
        """
        self.company_id = params["company_id"]
        self.company_name = params["company_name"]
        self.form_name = params["form_name"]
        self.date = params["date"]
        self.document_path = params["document_path"]

    def document_url(self):
        """
        compiles a url where the filing document can be found and parsed
        """
        return os.path.join(ARCHIVES_URL, self.document_path)
