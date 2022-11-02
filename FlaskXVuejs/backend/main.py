from flask import Flask, render_template, jsonify, request
from api import api_bp

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.register_blueprint(api_bp)

files = []
idx   = 0

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
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
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run()