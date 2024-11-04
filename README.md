# version-control-exercise

## Set Up

Create and activate a virtual environment

```sh
conda create -n reports-env python=3.12
```

Activate the environment:
```
conda activate reports-env
```

Install packages:
```sh
pip install -r requirements.txt
```

## Usage

Run the example script:

```sh
python app/script.py
```

Run the unemployment report:
```sh
ALPHAVANTAGE_API_KEY="..." python app/unemployment.py
```