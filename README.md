
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

### Parsing 10Ks given CSV Inputs

Specify desired years and company ids in "data/inputs.csv":

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

Then run `python -m app.services.csv_10k_filings` to see results written to "data/outputs.csv":


    TODO


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
