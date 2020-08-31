from app import app, models
import config

import os
from flask import render_template, request, redirect, abort, flash, jsonify, url_for


@app.route('/upload', methods=['POST'])
def upload_File():
    """File upload handler.
    

    """    
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'no file'
        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'no selected file'
        if file: # and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            return json.dumps(out) # pass table row partial or flash error message
    return