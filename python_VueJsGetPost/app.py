from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 文字化け防止

products = [
    {'id': 1, 'name':'商品1', 'price':780},
    {'id': 2, 'name':'商品2', 'price':1280},
    {'id': 3, 'name':'商品3', 'price':1980},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def get_products():
    return jsonify({'products': products}) # JSONファイルにしてデータを返す

@app.route('/product', methods=['POST'])
def create_product():
    post_data = request.get_json() # get_json()でデータの受け取り
    new_product = {'id': products[-1]['id']+1}  # idのみの辞書を作成
    new_product.update(list(post_data.items())) # 上記で作成した辞書にpostで受けたデータを追加(update)
    products.append(new_product)
    return jsonify({'products': products})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')