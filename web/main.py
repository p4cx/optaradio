from flask import *
from flask_socketio import SocketIO, send
from globals_web import *
from app.forms import *
from app import helpers, station_model
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "super secret key"
socket_io = SocketIO(app)


@app.route("/station_form")
def station_form(station=None):
    form_station = AddStationForm()
    if station is not None:
        form_station.station_name.data = station[1]
        form_station.station_url.data = station[2]
        form_station.station_desc.data = station[3]
        form_station.station_country.data = station[5]
    countries = helpers.load_country_choices()

    return render_template('station_form.html', form=form_station, countries=countries)


@app.route('/add_station', methods=['POST'])
def add_station():
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
            success, message, station = station_model.add(request.form, os.path.join(TEMP_PATH, filename))
            return render_template('report.html', success=success, message=message, station=station)
        else:
            print('Allowed file types are png')
            return render_template('report.html', success=False, message="Wrong file format.", station=[])


@app.route('/mod_station/<string:old_station>', methods=['POST'])
def mod_station(old_station):
    if request.method == 'POST':
        print(request.form)
        old_name = old_station
        if 'station_cover' in request.files:
            file = request.files['station_cover']
            if file.filename != '' and file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(TEMP_PATH, filename))
                success, message, station = station_model.modify_station(request.form, os.path.join(TEMP_PATH, filename), old_name)
                return render_template('report.html', success=success, message=message, station=station)
        filename = request.form['station_name'] + ".png"
        old_file = os.path.join(THUMBS_PATH, old_name + ".png")
        new_file = os.path.join(THUMBS_PATH, filename)
        os.rename(old_file, new_file)
        success, message, station = station_model.modify_station(request.form, filename, old_name)
        return render_template('report.html', success=success, message=message, station=station)


@app.route('/action_station', methods=['POST'])
def action_station():
    if request.method == 'POST':
        for key, value in request.form.items():
            if key == "del_radio_station":
                return render_template('del_station.html', station=station_model.crawl_station_list(value))
            elif key == "mod_radio_station":
                return station_form(station_model.crawl_station_list(value))


@app.route('/del_station', methods=['POST'])
def del_station():
    if request.method == 'POST':
        for key, value in request.form.items():
            if value[:6] == "Delete":
                station_model.delete_station(key)
                return render_template('report.html', success=True, message="Is deleted.", station=[])
    return render_template('report.html', success=False, message="Something went wrong.", station=[])


@app.route('/image/<path:filename>')
def download_file(filename):
    return send_from_directory(THUMBS_PATH, filename, as_attachment=True)


@app.route("/")
def stations():
    return render_template('stations.html', station_list=station_model.get())


def send_message():
    print("send hello")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png']


if __name__ == "__main__":
    socket_io.run(app, host='0.0.0.0', port=80)


application = app

