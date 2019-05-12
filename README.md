
# SEC Archives (Python)

[![Build Status](https://travis-ci.com/s2t2/sec-archives-py.svg?branch=master)](https://travis-ci.com/s2t2/sec-archives-py)

## Prerequisites

Requires Anaconda, Python, and Pip versions 3.7.

## Setup

Create (first time only) and activate a virtual environment:

```sh
conda create -n sec-env python=3.7
conda activate sec-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### CSV-Based Multi-Quarter 10K Document Search

Specify desired years and company ids in "data/inputs.csv":

```csv
year, company_id
2013, 1018724
2014, 1018724
2015, 1018724
2013, 1288776
2014, 1288776
2015, 1288776
2013, 789019
2014, 789019
2015, 789019
```

Then run `python -m app.services.csv_10k_filings` to see results written to "data/outputs.csv":

```csv
year,company_id,company_name,filed_on,url,anticipate,believe,depend,fluctuate,indefinite,likelihood,possible,predict,risk,uncertain,is
2013,1018724,AMAZON COM INC,2013-01-30,https://www.sec.gov/Archives/edgar/data/1018724/0001193125-13-028520.txt,9,32,39,4,15,15,25,6,55,38,17838
2013,1288776,Google Inc.,2013-01-29,https://www.sec.gov/Archives/edgar/data/1288776/0001193125-13-028362.txt,34,46,20,16,7,6,23,14,91,25,21179
2013,789019,MICROSOFT CORP,2013-07-30,https://www.sec.gov/Archives/edgar/data/789019/0001193125-13-310206.txt,29,49,9996,1,1,3,34,1,162,45,50425
2014,1018724,AMAZON COM INC,2014-01-31,https://www.sec.gov/Archives/edgar/data/1018724/0001018724-14-000006.txt,9,26,27,4,15,15,23,6,59,40,12755
2014,1288776,Google Inc.,2014-02-12,https://www.sec.gov/Archives/edgar/data/1288776/0001288776-14-000020.txt,30,46,21,16,7,6,28,15,100,28,20685
2014,789019,MICROSOFT CORP,2014-07-31,https://www.sec.gov/Archives/edgar/data/789019/0001193125-14-289961.txt,20,39,53,0,0,2,17,2,127,35,20750
2015,1018724,AMAZON COM INC,2015-01-30,https://www.sec.gov/Archives/edgar/data/1018724/0001018724-15-000006.txt,9,26,29,5,24,15,23,6,66,43,17864
2015,1288776,Google Inc.,2015-02-09,https://www.sec.gov/Archives/edgar/data/1288776/0001288776-15-000008.txt,30,44,22,15,4,6,41,11,110,25,29547
2015,789019,MICROSOFT CORP,2015-07-31,https://www.sec.gov/Archives/edgar/data/789019/0001193125-15-272806.txt,18,37,51,1,0,2,15,4,127,34,23822
```


### Other Scripts

Get filings (optionally specifying search params):

```sh
python -m app.services.get_filings

COMPANY="1000180" python -m app.services.get_filings

COMPANY="1018724" YR="2013" QTR="1" python -m app.services.get_filings
```

Get 10-K filings for a given company:

```sh
python -m app.services.get_filings

COMPANY="1018724" python -m app.services.company_10k_filings
```

## Testing

Install pytest (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```
