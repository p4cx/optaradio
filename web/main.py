from flask import *
from web.globals import *
from optaradio.globals import *
from web.app.forms import StationForm
from web.app import helpers
from web.app import addStation, getStations
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
            return render_template('report.html', success=False, message="No file selected for uploading.", station=[])
        file = request.files['station_cover']
        if file.filename == '':
            print('No file selected for uploading')
            return render_template('report.html', success=False, message="No file selected for uploading.", station=[])
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(TEMP_PATH, filename))
            print('File successfully uploaded')
            success, message, station = addStation.add(request.form, os.path.join(TEMP_PATH, filename))
            return render_template('report.html', success=success, message=message, station=station)
        else:
            print('Allowed file types are png')
            return render_template('report.html', success=False, message="Wrong file format.", station=[])


@app.route('/image/<path:filename>')
def download_file(filename):
    return send_from_directory(THUMBS_PATH, filename, as_attachment=True)


@app.route("/stations")
def stations():
    station_list = getStations.get()
    print(station_list[0])
    return render_template('stations.html', station_list=getStations.get())


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
