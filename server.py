# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import os

import detect_anju
import make_score

app = Flask(__name__)


# ----------------------------------
# upload file
# ----------------------------------
# 파일 업로드 처리
@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    program_id = 'server.py'

    if request.method == 'POST':

        # ----------------------------
        # Save the file to ./uploads
        f = request.files['file']
        file_name = secure_filename(f.filename)
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', file_name)
        f.save(file_path)
        return_msg = '파일저장 완료!'
        print('[5]return_msg :', return_msg)

        labels = detect_anju.detect(file_name)
        score, desc, anju, alcohol, anju_score, alcohol_score = make_score.scoring(labels)

        return_msg = '분석완료 !'
        print('[6]return_msg :', return_msg)

        return render_template('index.html', return_msg=return_msg, labels=labels, result_img=file_name, score=score, desc=desc, anju=anju, alcohol=alcohol, anju_score=anju_score, alcohol_score=alcohol_score)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host="0.0.0.0", port=5000)  # debug=True causes Restarting with stat