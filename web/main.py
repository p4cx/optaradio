from flask import *


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/stations")
def stations():
    return render_template('stations.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
