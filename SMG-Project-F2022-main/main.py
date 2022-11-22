"""
from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
app.config['FILE_UPLOADS'] = 'C:\\Users\\zelax\\Downloads\\SMG-Project-F2022-main\\pdffiles'
from werkzeug.utils import secure_filename
@app.route("/Transcript%20Reader", methods = ["POST","GET"])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        if file.filename == '':
            print("File name is not valid")
            return redirect(request.url)
        filename = secure_filename(file.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir,app.config['FILE_UPLOADS'], filename))
        return render_template("TR.HTML", filename = filename)
    return render_template("TR.HTML")
@app.route('/display/<filename>')
def display_file(filename):
        return redirect(url_for(filename = '/pdffiles/'+filename), code = 301)
"""
"""
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
app = Flask(__name__)

@app.route('/action_page.php', endpoint= 'upload.html')
def upload_file():
   return render_template('upload.html')
	
@app.route('/Transcript%20Reader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
"""
from website import app
if __name__ == '__main__':
    app.run(debug=True)
