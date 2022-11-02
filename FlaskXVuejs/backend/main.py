from flask import Flask, render_template, jsonify, request
from api import api_bp

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
app.register_blueprint(api_bp)

info = []

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/post_info', methods=['POST'])
def get_info():
    post_data = request.get_json()


if __name__ == '__main__':
    app.run()