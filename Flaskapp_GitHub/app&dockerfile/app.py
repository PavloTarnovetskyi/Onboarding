import requests
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ID = "042ee935522c4ac7851c410321a8cbff"
ENDPOINT = "https://openexchangerates.org/api/latest.json"
CURRENCY_DEF_ENDPOINT = "https://openexchangerates.org/api/currencies.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
currency_definition = requests.get(f"{CURRENCY_DEF_ENDPOINT}").json()

exchange_rates = response.json()["rates"] 

@app.route('/', methods=['GET', 'POST'])
def home():
    currency = {}
    
    if request.method == 'POST':
        currency_name = request.form.get("currency")
        fcur = exchange_rates.get(currency_name)
        currency = { 'title': f'Actual exchange rate USD to {currency_name} ', 
                     'rates': f' 1 USD is {fcur:.3f} {currency_name}'
               }
        return render_template("home.jinja2", currency_definition=currency_definition, exchange_rates=exchange_rates, currency=currency)
    return render_template("home.jinja2", exchange_rates=exchange_rates, currency_definition=currency_definition, currency=currency)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

# use this command in terminal to run that app on your localhosh (you have to install python3):
# python3 app.py