from flask import Flask, render_template, redirect, url_for, request, json
from flask_fontawesome import FontAwesome

app = Flask('Simple E-commerce', static_url_path='/static')
fa = FontAwesome(app)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/productList")
def productList():
	return render_template('productList.html')

@app.route("/productOverview")
def productOverview():
	return render_template('productOverview.html')

@app.route("/cart")
def cart():
	return render_template('cart.html')

@app.route("/checkout")
def checkout():
	return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)