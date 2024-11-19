# version-control-exercise

## Set Up

Create and activate a virtual environment

```sh
conda create -n reports-env python=3.12
```

Activate the environment:
```sh
conda activate reports-env
```

Install packages:
```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
ALPHAVANTAGE_API_KEY = "..."
```

For email functionalities, add:
```sh
MAILGUN_SENDER_ADDRESS = "..."
MAILGUN_DOMAIN = "..."
MAILGUN_API_KEY = "..."
```

## Usage

Run the example script:

```sh
python app/script.py
```

Run the unemployment report:
```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py
#python app/unemployment.py
python -m app.unemployment
```

Run the stocks report:
```sh
# python app/stocks.py
python -m app.stocks
```

Run the email program:
```sh
python -m app.email
```

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app

flask run
```