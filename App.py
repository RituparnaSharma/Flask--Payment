from flask import Flask, render_template, request
from preprocess import verify

GateWays = ['PremiumPaymentGateway', 'ExpensivePaymentGateway', 'CheapPaymentGateway']
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/Submit", methods=["post"])
def greet():
    info = {'CreditCardNumber': request.form.get("CcdNo"),
            'CardHolder': request.form.get("CardHolder"),
            'ExpirationDate': request.form.get("ExpirationDate"),
            'SecurityCode': request.form.get("SecurityCode"),
            'Amount': request.form.get("Amount")}
    print(verify.ProcessPayment(**info))
    if not verify.ProcessPayment(**info):
        return render_template('greet.html', error_val=200)
    elif verify.ProcessPayment(**info) is "Error500":
        return render_template('greet.html', error_val=500)
    else:
        return render_template('greet.html')


app.run()
