import os

from flask import Flask, render_template, request, send_file

from ocr import ocr_core, ocr_freq, ocr_count


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'jfif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/index')
def bengali_ocr():
    return render_template('index.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/download')
def download():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "data/image_result.txt"
    return send_file(path, as_attachment=True)



@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

            # call the OCR function on it
            word_freq  = ocr_freq(file)
            extracted_text = ocr_core(file)
            word_count = ocr_count(file)
            # for tst purposes
            # tst = oct_cmt(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed', word_freq= word_freq, word_count=word_count ,
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)