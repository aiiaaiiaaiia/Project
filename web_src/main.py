import os
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify, Response
from werkzeug.utils import secure_filename
from flask import send_from_directory
from rt_atrt_lib import RT_ATRT
import time
import dw_vdo_url
import threading

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
    global title

    res = {'title': title}
    return jsonify(res)

@app.route('/upload_vdo', methods=['GET', 'POST'])     
def upload_file():
    global file_name
    global title
    global inputlang
    file_name = 'None'
    # inputlang = ''

    # text = importpythonmodule.displaytext.generate_text()
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
        if file.filename == '':
            # flash('No selected file')
            pass
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_name = file.filename
            title = file_name
            # return redirect(url_for('uploaded_file', filename=filename))
            return redirect('/vdo_uploaded')
    return render_template('upload.html', processed_video = url_for('static', filename="uploadedvideo/"+file_name))
    
@app.route('/vdo_uploaded', methods=['GET', 'POST'])     
def set_process_param():
    global file_name
    global output_path
    global vdo_name
    global vdo_output
    if request.method == 'POST':
        # variable
        print("get pose from JS")
        print(request.form["text_position"])
        dict_form = request.form.to_dict(flat=False)
        vdo_name = file_name.split('.')[0]
        video = "static/uploadedvideo/"+ vdo_name + ".mp4"
        position = []
        language = []
        trans_language = []
        output_path = "static/process_output/"
        vdo_output = output_path + "processed_" + vdo_name + ".mp4"
        
        for element in dict_form:
            print(element)
            if element in ['english','chinese','french','thai','italian','japanese','korean','german','spanish','auto detect']:
                language.append(element)
            elif element in ['trans_thai']:
                trans_language.append('thai')
            elif element in ['trans_eng']:
                trans_language.append('english')
        
        position = dict_form['text_position'][0]
        
        print('video : ', video)
        print('position : ', position)
        print('language : ', language)
        print('trans_language : ', trans_language)
        print('output : ', output_path)
                
        ## Process Here
        # test_python.run_process(1,output_path)
        rt_atrt_process = RT_ATRT(video, position, language, trans_language, output_path)
        run_thread = threading.Thread(target=rt_atrt_process.run_process, name="rt_atrt_process", args=[])
        run_thread.start()
        ##
        return render_template('progress_bar.html', processed_video = url_for('static', filename="uploadedvideo/"+file_name),
                                processed_text = url_for('static', filename = "empty.txt"))

    return render_template('render_vdo.html', processed_video = url_for('static', filename="uploadedvideo/"+file_name), 
                            processed_text = url_for('static', filename = "empty.txt"))

@app.route('/finish_process')
def finish_process():
    global output_path
    global vdo_name
    return render_template('render_vdo.html', processed_video = url_for('static', filename = output_path + "processed_" + vdo_name + ".mp4"), 
                            processed_text = url_for('static', filename = output_path + vdo_name + "_text.txt"))

@app.route('/url_vdo', methods=['GET', 'POST'])
def process_url():
    global file_name
    global title
    global inputlang
    file_name = 'None'
    title = 'None'

    if request.method == 'POST':
        # variable
        url = request.form['yt_url']
        title, file_name = dw_vdo_url.video_link_url(url)
        file_name = file_name + '.mp4'
        return redirect('/vdo_uploaded')
    return render_template('link.html')

@app.route('/progress')
def progress():
    global output_path
    global vdo_name
    def generate():
        x = 0
        while x <= 100:
            f = open(output_path + vdo_name + "_progress.txt", 'r')
            x = int(f.read())
            f.close()
            yield "data:" + str(x) + "\n\n"
            time.sleep(1)
    return Response(generate(), mimetype= 'text/event-stream')

if __name__=="__main__":
    app.run(host='localhost', port=5000, debug=True)