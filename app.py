from flask import Flask, render_template

app = Flask(__name__)

# 商品資料
products = [
    {
        "name": "無線耳機",
        "amazon_url": "https://www.amazon.com/dp/XXXXX?tag=demo-20",
        "amazon_price": 59.99,
        "local_price": 1790,
        "image": "https://m.media-amazon.com/images/I/71p1kzZK%2BWL._AC_SL1500_.jpg"
    },
    {
        "name": "藍牙音箱",
        "amazon_url": "https://www.amazon.com/dp/YYYYY?tag=demo-20",
        "amazon_price": 89.99,
        "local_price": 2590,
        "image": "https://m.media-amazon.com/images/I/81Xc7%2BDuDkL._AC_SL1500_.jpg"
    }
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)  # 改成 5001

