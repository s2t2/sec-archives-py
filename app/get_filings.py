import requests

year = "2013"
quarter = "1"
request_url = f"https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{quarter}/master.idx"
print("URL:", request_url) #> https://www.sec.gov/Archives/edgar/full-index/2013/QTR1/master.idx

response = requests.get(request_url)
print("RESPONSE:", response.status_code, type(response))

#company_id = "1018724" # AMAZON

# breakpoint()
# type(response.text) #> str

lines = response.text.split("\n")
print(f"FILINGS ({len(lines)}):")

for line in lines:
    print(line)
