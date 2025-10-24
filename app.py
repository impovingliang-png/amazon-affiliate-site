from flask import Flask, render_template, send_from_directory, Response
import os

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

# 首頁
@app.route("/")
def index():
    return render_template("index.html", products=products)

# Sitemap route
@app.route("/sitemap.xml")
def sitemap():
    sitemap_xml = render_template("sitemap_template.xml", products=products)
    return Response(sitemap_xml, mimetype='application/xml')

# 提供 Google 驗證檔案
@app.route("/googlea58548c3e6f3d13d.html")
def google_verification():
    return send_from_directory(os.path.join(app.root_path, "static"), "googlea58548c3e6f3d13d.html")

# 啟動 Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
