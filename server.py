from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Response 200', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
