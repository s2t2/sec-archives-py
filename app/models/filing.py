
from app.archives import ARCHIVES_URL

class Filing():

    def __init__(self, params):
        self.company_id = params["company_id"]
        self.company_name = params["company_name"]
        self.form_name = params["form_name"]
        self.date = params["date"]
        self.document_path = params["document_path"]

    def document_url(self):
        return f"{ARCHIVES_URL}/{self.document_path}"
