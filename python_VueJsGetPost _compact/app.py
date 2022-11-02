from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False # 文字化け防止

files = []
idx = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file', methods=['POST'])
def create_file():
    global idx
    post_data = request.get_json()
    new_file = {'id': idx}
    new_file.update(list(post_data.items()))
    files.append(new_file)
    idx = idx + 1
    return jsonify({'files': files})

@app.route('/files')
def get_files():
    print(type(files))
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')