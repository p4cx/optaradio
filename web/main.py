from flask import *
from web.globals import *
from web.app.forms import StationForm
from web.app import helpers
from web.app import addStation
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/")
def index():
    station_form = StationForm()
    countries = helpers.load_country_choices()
    success = False

    return render_template('index.html', form=station_form, countries=countries, success=success)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        if 'station_cover' not in request.files:
            print('No file part')
            return render_template('report.html', success=False, message="No file selected for uploading.")
        file = request.files['station_cover']
        if file.filename == '':
            print('No file selected for uploading')
            return render_template('report.html', success=False, message="No file selected for uploading.")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(TEMP_PATH, filename))
            print('File successfully uploaded')
            success, message = addStation.add_station(request.form, os.path.join(TEMP_PATH, filename))
            return render_template('report.html', success=success, message=message)
        else:
            print('Allowed file types are png')
            return render_template('report.html', success=False, message="Wrong file format.")


@app.route("/stations")
def stations():
    return render_template('stations.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
