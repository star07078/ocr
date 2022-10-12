# @author star07078

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './bb'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

      result = ocr.ocr(f"{app.config['UPLOAD_FOLDER']}/{secure_filename(f.filename)}", cls=True)
      s = ''
      for line in result:
         s += line[1][0] + '\r\n'
      return s

if __name__ == '__main__':
   app.run()
