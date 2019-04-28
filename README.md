
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

Get filings:

```sh
python app/get_filings.py
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
