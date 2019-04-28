
import os

base_url = "https://www.sec.gov/Archives"
document_path = "edgar/data/1018724/0001193125-13-028520.txt"
request_url = os.path.join(base_url, document_path)
print("URL:", request_url) #> https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt
