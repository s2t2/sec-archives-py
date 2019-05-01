
# SEC Archives (Python)

## Prerequisites

Requires Anaconda, Python, and Pip versions 3.7.

## Setup

Create (first time only) and activate a virtual environment:

```sh
conda create -n soup-env
conda activate soup-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Get filings (optionally specifying search params):

```sh
python -m app.get_filings

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
