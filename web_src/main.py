import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import importpythonmodule

UPLOAD_FOLDER = 'static/uploadedvideo'
# UPLOAD_FOLDER = os.path.dirname('./uploadedvideo')
ALLOWED_EXTENSIONS = {'avi', 'wmv', 'mpeg', 'mov', 'divx', 'dat', 'flv', 'mp4', 'avchd', 'webm', 'mkv'}   

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template') 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/vdo_info',methods = ['GET'])
def vdo_info_handle():
    global file_name
    res = {'file_name': file_name}
    return jsonify(res)

# @app.route('/button', methods=['POST'])
# def button():
#     global inputlang
#     global tranlang
#     inputlang = request.json['from']
#     tranlang = request.json['to']
#     return jsonify(result=...)

@app.route('/videofromupload', methods=['GET', 'POST'])     
def upload_file():
    global file_name
    global inputlang
    file_name = 'None'
    # inputlang = ''

    text = importpythonmodule.displaytext.generate_text()
    # if request.method == "GET":
    #     autodetect = 'autodetect'
    #     return redirect(request.url)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            # flash('No file part')
            pass
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            # flash('No selected file')
            pass
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_name = file.filename
            # return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html', processed_video = url_for('static', filename="uploadedvideo/"+file_name)
                            , echo_text = text)

# @app.route('/videofromlink', methods=['GET', 'POST'])
# def home():
#     return render_template("link.html")

if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)