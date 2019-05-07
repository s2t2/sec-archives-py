
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

Get filings (optionally specifying search params):

```sh
python -m app.get_filings

COMPANY="1000180" python -m app.get_filings

COMPANY="1018724" YR="2013" QTR="1" python -m app.get_filings
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
